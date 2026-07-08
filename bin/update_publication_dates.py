#!/usr/bin/env python3
"""Update sort_month/sort_day (and month) in papers.bib from venue or arXiv release dates.

Venue papers (entries with `abbr`) always use the venue release date.
arXiv-only papers (no `abbr`) use the arXiv `published` date.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BIB_FILE = ROOT / "_bibliography" / "papers.bib"
VENUE_DATES_FILE = ROOT / "_data" / "venue_dates.yml"
ARXIV_SOURCES_FILE = ROOT / "_data" / "publication_sources.yml"

MONTH_NUM_TO_BIB = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
}

MONTH_NAME_TO_NUM = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}

ATOM_NS = {"a": "http://www.w3.org/2005/Atom"}


@dataclass(frozen=True)
class ReleaseDate:
    month: int
    day: int
    source: str

    @property
    def sort_month(self) -> str:
        return f"{self.month:02d}"

    @property
    def sort_day(self) -> str:
        return f"{self.day:02d}"

    @property
    def month_bib(self) -> str:
        return MONTH_NUM_TO_BIB[self.month]


def fetch_text(url: str, timeout: int = 20) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "LabPage publication-date updater (mailto:cognitive.yunpu@gmail.com)"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> dict:
    return json.loads(fetch_text(url))


def parse_fields(entry_body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in re.finditer(r"(\w+)=\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", entry_body):
        fields[match.group(1)] = match.group(2)
    return fields


def split_bib_entries(content: str) -> list[tuple[str, str, str]]:
    """Return (entry_type, cite_key, full_entry_text) tuples."""
    entries: list[tuple[str, str, str]] = []
    for match in re.finditer(
        r"(@\w+\{([^,\s]+),)(.*?)(?=\n@|\Z)",
        content,
        flags=re.DOTALL,
    ):
        header = match.group(1)
        key = match.group(2)
        body = match.group(3)
        entry_type = re.match(r"@(\w+)", header).group(1)  # type: ignore[union-attr]
        entries.append((entry_type, key, header + body))
    return entries


def extract_arxiv_id(entry_fields: dict[str, str], cite_key: str, arxiv_sources: dict[str, str]) -> str | None:
    if cite_key in arxiv_sources:
        return arxiv_sources[cite_key].split("v", 1)[0]

    for field in ("note", "pdf", "eprint"):
        value = entry_fields.get(field, "")
        match = re.search(r"arxiv[:\s]*(\d{4}\.\d{4,5})", value, flags=re.I)
        if match:
            return match.group(1)

    return None


def extract_doi(entry_fields: dict[str, str]) -> str | None:
    if "doi" in entry_fields:
        return entry_fields["doi"]
    pdf = entry_fields.get("pdf", "")
    for pattern in (
        r"doi\.org/([^\s/?#]+)",
        r"/doi/(?:pdf|abs|fullHtml|epdf)/(10\.\d+/[^\s?#]+)",
        r"/doi/(10\.\d+/[^\s?#]+)",
    ):
        match = re.search(pattern, pdf, flags=re.I)
        if match:
            return match.group(1)
    return None


def extract_acl_paper_id(pdf_url: str) -> str | None:
    match = re.search(r"aclanthology\.org/([^/?#]+?)(?:\.pdf)?/?(?:\?|#|$)", pdf_url, flags=re.I)
    if not match:
        return None
    paper_id = match.group(1)
    if paper_id.endswith(".pdf"):
        paper_id = paper_id[:-4]
    return paper_id


def parse_quantum_url(pdf_url: str) -> ReleaseDate | None:
    match = re.search(r"q-(\d{4})-(\d{2})-(\d{2})-", pdf_url)
    if not match:
        return None
    year, month, day = (int(match.group(i)) for i in range(1, 4))
    return ReleaseDate(month=month, day=day, source=f"quantum-journal ({year})")


def clean_title(title: str) -> str:
    return re.sub(r"[{}]", "", title).strip()


def prefer_more_precise(left: ReleaseDate | None, right: ReleaseDate | None) -> ReleaseDate | None:
    if left is None:
        return right
    if right is None:
        return left
    if right.day and not left.day:
        return right
    if left.day and not right.day:
        return left
    return right


def merge_dates(primary: ReleaseDate | None, fallback: ReleaseDate | None) -> ReleaseDate | None:
    if primary is None:
        return fallback
    if fallback is None:
        return primary
    if primary.day:
        return primary
    if fallback.day and primary.month == fallback.month:
        return ReleaseDate(
            month=primary.month,
            day=fallback.day,
            source=f"{primary.source}+{fallback.source}",
        )
    if fallback.day:
        return fallback
    return primary


def parse_acl_month_day(bib_text: str) -> ReleaseDate | None:
    month_match = re.search(r"month\s*=\s*([a-z]+)", bib_text, flags=re.I)
    if not month_match:
        return None
    month = MONTH_NAME_TO_NUM.get(month_match.group(1).lower())
    if not month:
        return None

    day_match = re.search(r'day\s*=\s*"?(\d{1,2})"?,', bib_text, flags=re.I)
    day = int(day_match.group(1)) if day_match else 0
    return ReleaseDate(month=month, day=day, source="aclanthology")


def fetch_acl_xml_date(pdf_url: str) -> ReleaseDate | None:
    paper_id = extract_acl_paper_id(pdf_url)
    if not paper_id:
        return None
    xml_text = fetch_text(f"https://aclanthology.org/{paper_id}.xml")
    match = re.search(r"<dateIssued>(\d{4})-(\d{2})(?:-(\d{2}))?</dateIssued>", xml_text)
    if not match:
        return None
    month = int(match.group(2))
    day = int(match.group(3)) if match.group(3) else 0
    return ReleaseDate(month=month, day=day, source="aclanthology")


def fetch_acl_date(pdf_url: str) -> ReleaseDate | None:
    date = fetch_acl_xml_date(pdf_url)
    if date:
        return date
    paper_id = extract_acl_paper_id(pdf_url)
    if not paper_id:
        return None
    bib_text = fetch_text(f"https://aclanthology.org/{paper_id}.bib")
    return parse_acl_month_day(bib_text)


def fetch_crossref_by_title(title: str, container: str | None = None) -> ReleaseDate | None:
    params: dict[str, str] = {"query.title": clean_title(title), "rows": "5"}
    if container:
        params["query.container-title"] = container
    data = fetch_json(f"https://api.crossref.org/works?{urllib.parse.urlencode(params)}")
    query_title = clean_title(title).lower()
    for item in data.get("message", {}).get("items", []):
        item_titles = item.get("title") or []
        if not item_titles:
            continue
        item_title = item_titles[0].lower()
        if query_title not in item_title and item_title not in query_title:
            continue
        for key in ("published", "published-print", "issued", "created"):
            parts = item.get(key, {}).get("date-parts", [[]])
            if parts and parts[0]:
                nums = parts[0]
                month = int(nums[1]) if len(nums) > 1 else 0
                day = int(nums[2]) if len(nums) > 2 else 0
                if month:
                    doi = item.get("DOI", "unknown")
                    return ReleaseDate(month=month, day=day, source=f"crossref-title ({doi})")
    return None


def fetch_crossref_date(doi: str) -> ReleaseDate | None:
    data = fetch_json(f"https://api.crossref.org/works/{doi}")
    message = data.get("message", {})
    for key in ("published", "published-print", "issued", "created"):
        parts = message.get(key, {}).get("date-parts", [[]])
        if parts and parts[0]:
            nums = parts[0]
            month = int(nums[1]) if len(nums) > 1 else 0
            day = int(nums[2]) if len(nums) > 2 else 0
            if month:
                return ReleaseDate(month=month, day=day, source=f"crossref ({doi})")
    return None


def fetch_arxiv_date(arxiv_id: str) -> ReleaseDate | None:
    xml_text = fetch_text(f"https://export.arxiv.org/api/query?id_list={arxiv_id}")
    root = ET.fromstring(xml_text)
    entry = root.find("a:entry", ATOM_NS)
    if entry is None:
        return None
    published = entry.find("a:published", ATOM_NS)
    if published is None or not published.text:
        return None
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})", published.text)
    if not match:
        return None
    return ReleaseDate(
        month=int(match.group(2)),
        day=int(match.group(3)),
        source=f"arxiv ({arxiv_id})",
    )


def lookup_venue_date(abbr: str, venue_dates: dict[str, dict]) -> ReleaseDate | None:
    record = venue_dates.get(abbr)
    if not record:
        return None
    return ReleaseDate(
        month=int(record["month"]),
        day=int(record.get("day", 0)),
        source=f"venue_dates ({abbr})",
    )


def fetch_venue_date(entry_fields: dict[str, str], venue_dates: dict[str, dict]) -> ReleaseDate | None:
    pdf_url = entry_fields.get("pdf", "")
    abbr = entry_fields.get("abbr", "")
    title = entry_fields.get("title", "")
    date: ReleaseDate | None = None

    if "aclanthology.org" in pdf_url:
        date = fetch_acl_date(pdf_url)

    if "quantum-journal.org" in pdf_url:
        date = prefer_more_precise(date, parse_quantum_url(pdf_url))

    doi = extract_doi(entry_fields)
    if doi:
        date = prefer_more_precise(date, fetch_crossref_date(doi))

    if "ojs.aaai.org" in pdf_url and title:
        date = prefer_more_precise(
            date,
            fetch_crossref_by_title(title, "Proceedings of the AAAI Conference on Artificial Intelligence"),
        )

    if abbr:
        date = merge_dates(date, lookup_venue_date(abbr, venue_dates))

    return date


def remove_field(entry_text: str, field: str) -> str:
    pattern = rf"(?<![\w]){re.escape(field)}=\{{[^{{}}]*\}},?\s*"
    return re.sub(pattern, "", entry_text)


def upsert_field(entry_text: str, field: str, value: str) -> str:
    pattern = rf"(?<![\w]){re.escape(field)}=\{{[^{{}}]*\}},?\s*"
    replacement = f"{field}={{{value}}}, "
    if re.search(pattern, entry_text):
        return re.sub(pattern, replacement, entry_text, count=1)
    year_match = re.search(r"(year=\{[^{}]+\},)", entry_text)
    if year_match:
        insert_at = year_match.end()
        return entry_text[:insert_at] + f" {field}={{{value}}}," + entry_text[insert_at:]
    return entry_text


def apply_date_to_entry(entry_text: str, date: ReleaseDate) -> str:
    updated = upsert_field(entry_text, "sort_month", date.sort_month)
    updated = upsert_field(updated, "sort_day", date.sort_day)
    updated = upsert_field(updated, "month", date.month_bib)
    return remove_field(updated, "day")


def resolve_date(
    entry_type: str,
    cite_key: str,
    entry_fields: dict[str, str],
    venue_dates: dict[str, dict],
    arxiv_sources: dict[str, str],
) -> ReleaseDate | None:
    if entry_fields.get("abbr"):
        return fetch_venue_date(entry_fields, venue_dates)

    arxiv_id = extract_arxiv_id(entry_fields, cite_key, arxiv_sources)
    if arxiv_id:
        return fetch_arxiv_date(arxiv_id)

    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing papers.bib")
    parser.add_argument("--key", action="append", help="Only update specific cite key(s)")
    args = parser.parse_args()

    if not BIB_FILE.exists():
        print(f"Missing bibliography file: {BIB_FILE}", file=sys.stderr)
        return 1

    venue_dates = yaml.safe_load(VENUE_DATES_FILE.read_text()) if VENUE_DATES_FILE.exists() else {}
    arxiv_sources = yaml.safe_load(ARXIV_SOURCES_FILE.read_text()) if ARXIV_SOURCES_FILE.exists() else {}

    content = BIB_FILE.read_text()
    entries = split_bib_entries(content)
    if not entries:
        print("No BibTeX entries found.", file=sys.stderr)
        return 1

    updated_blocks: list[str] = []
    changed = 0
    skipped = 0

    for entry_type, cite_key, entry_text in entries:
        if args.key and cite_key not in args.key:
            updated_blocks.append(entry_text)
            continue

        fields = parse_fields(entry_text)
        try:
            date = resolve_date(entry_type, cite_key, fields, venue_dates, arxiv_sources)
        except (urllib.error.URLError, TimeoutError, ET.ParseError, yaml.YAMLError) as exc:
            print(f"WARN {cite_key}: fetch failed ({exc})", file=sys.stderr)
            date = None

        if not date:
            print(f"SKIP {cite_key}: no date resolved")
            skipped += 1
            updated_blocks.append(entry_text)
            continue

        new_text = apply_date_to_entry(entry_text, date)
        old_month = fields.get("sort_month")
        old_day = fields.get("sort_day")
        if (
            old_month == date.sort_month
            and old_day == date.sort_day
            and fields.get("month") == date.month_bib
            and "day" not in fields
        ):
            print(f"OK   {cite_key}: {date.sort_month}/{date.sort_day} ({date.source})")
        else:
            print(
                f"SET  {cite_key}: {old_month or '??'}/{old_day or '??'} -> "
                f"{date.sort_month}/{date.sort_day} month={date.month_bib} ({date.source})"
            )
            changed += 1
        updated_blocks.append(new_text)

    print(f"\nSummary: {changed} updated, {skipped} skipped, {len(entries)} total")

    if args.dry_run:
        print("Dry run: not writing papers.bib")
        return 0

    if changed == 0:
        return 0

    preamble_match = re.match(r"^(.*?)(?=@)", content, flags=re.DOTALL)
    preamble = preamble_match.group(1) if preamble_match else ""
    new_content = preamble + "\n\n".join(block.strip() for block in updated_blocks) + "\n"
    BIB_FILE.write_text(new_content)
    print(f"Wrote {BIB_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
