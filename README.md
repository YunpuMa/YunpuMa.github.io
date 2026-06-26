# Research Group Website

A minimal academic group website built with Jekyll and the
[al-folio](https://github.com/alshedivat/al-folio) theme.

## Local preview

```bash
docker compose pull
docker compose up
```

Open <http://localhost:8080>.

## Updating content

- Edit the group introduction in `_pages/about.md`.
- Add dated updates as Markdown files in `_news/`.
- Maintain publications in `_bibliography/papers.bib`.
- Maintain members in `_data/people.yml` and put photos in `assets/img/`.

### Publication thumbnails

Map bibliography keys to arXiv IDs in `_data/publication_sources.yml`, then run:

```bash
bin/extract-arxiv-figures --all
```

The script keeps source archives and ranked figure shortlists in
`/tmp/al-folio-arxiv-figures`. Copy selected images into
`assets/img/publication_preview/` and set the entry's `preview` field in
`_bibliography/papers.bib`. Teaser-named figures receive the highest shortlist
priority.

Before deploying to GitHub Pages, set `url` and `baseurl` in `_config.yml`.
