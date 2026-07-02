---
layout: page
permalink: /publications/
title: Publications
description: Selected publications from the group.
nav: true
nav_order: 3
---

<script>
  if (window.location.hash) document.documentElement.classList.add("bibsearch-pending");
</script>

For the full list, see my [Google Scholar page]({{ site.google_scholar_url }}).

<style>
  .post-title {
    font-family: 'Libre Baskerville', serif;
    font-weight: 700;
    letter-spacing: 0.01em;
  }
  .post-description {
    font-size: 0.82rem;
    font-variant: small-caps;
    letter-spacing: 0.1em;
    color: var(--global-text-color-light);
    margin: 0.4rem 0 0;
  }
  .post-header {
    padding-bottom: 1.5rem;
    border-bottom: 1px solid var(--global-divider-color);
    margin-bottom: 2rem;
  }
  .publications .links { display: flex; gap: 0.22rem; align-items: center; flex-wrap: wrap; }
  .publications .links .bibtex { order: 2; }
  .publications .links a.btn {
    padding: 0.12rem 0.34rem;
    border: 1px solid color-mix(in srgb, var(--global-theme-color) 18%, transparent) !important;
    border-radius: 0.25rem;
    background: transparent !important;
    color: color-mix(in srgb, var(--global-theme-color) 58%, var(--global-text-color-light)) !important;
    font-size: 0.66rem;
    font-weight: 400;
    line-height: 1.2;
    letter-spacing: 0.01em;
    text-transform: none;
    box-shadow: none !important;
  }
  .publications .links a.btn:hover,
  .publications .links a.btn:focus-visible {
    border-color: color-mix(in srgb, var(--global-theme-color) 34%, transparent) !important;
    background: color-mix(in srgb, var(--global-theme-color) 5%, transparent) !important;
    color: var(--global-theme-color) !important;
    box-shadow: none !important;
  }
  .publications .abbr {
    transform-origin: center;
    transition: transform 0.2s ease;
  }
  .publications .abbr .badge {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.12rem 0.22rem;
    font-size: 0.64rem;
    white-space: normal;
    line-height: 1.05;
    overflow-wrap: normal;
    word-break: normal;
    text-align: center;
  }
  .publications .abbr figure picture {
    display: block;
    aspect-ratio: 6 / 5;
    overflow: hidden;
    border-radius: 0.25rem;
  }
  .publications .abbr figure picture .preview {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
    cursor: zoom-in;
  }
  #publication-image-lightbox {
    max-width: none;
    max-height: none;
    padding: 0;
    border: 0;
    overflow: visible;
    background: transparent;
    cursor: zoom-out;
  }
  #publication-image-lightbox::backdrop {
    background: color-mix(in srgb, var(--global-bg-color) 94%, transparent);
  }
  #publication-image-lightbox img {
    display: block;
    width: auto;
    height: auto;
    max-width: 92vw;
    max-height: 92vh;
    object-fit: contain;
    border-radius: 0.25rem;
    box-shadow: 0 0.5rem 2rem rgba(0, 0, 0, 0.25);
    cursor: default;
  }
  #publication-image-lightbox button {
    position: fixed;
    top: 1rem;
    right: 1rem;
    border: 0;
    background: transparent;
    color: var(--global-text-color);
    font-size: 2rem;
    line-height: 1;
    cursor: pointer;
  }
  /* Ghost year on h2 itself: styled from first paint so no reformat when JS wraps it in a span */
  .publications h2.bibliography {
    font-size: 5rem;
    font-weight: 700;
    line-height: 1;
    letter-spacing: -0.01em;
    color: rgba(78, 111, 163, 0.12);
    margin: 3rem 0 -3.5rem;
    padding: 1rem 0 0; /* reserve height for the absolute-positioned badge above the year */
    border: none;
    user-select: none;
    position: relative;
    /* gem's text-align:right is kept: pre-aligns inline year text to right edge before JS runs */
  }
  /* dark mode for year text before JS (h2 inline text) and after JS (.bib-year-num span) */
  html[data-theme=dark] .publications h2.bibliography { color: rgba(124, 160, 197, 0.15); }
  html[data-theme=dark] .publications .bib-year-num { color: rgba(124, 160, 197, 0.15); }
  /* Badge: absolute so it never shifts the h2 height; fades in after JS positions it */
  .publications .bib-header {
    position: absolute;
    top: 1.72rem;
    left: 0;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 2.1rem;
    height: 2.1rem;
    font-size: 1.25rem;
    font-family: 'DM Sans', sans-serif;
    font-weight: 400;
    letter-spacing: 0;
    text-transform: none;
    color: rgba(78, 111, 163, 0.3);
    opacity: 0;
    white-space: nowrap;
    cursor: pointer;
    pointer-events: auto;
    transition: transform 0.36s ease, opacity 0.2s ease, color 0.36s ease;
  }
  .publications h2.bibliography.collapsed .bib-header { display: none !important; }
  /* When collapsed the whole h2 is clickable — show pointer */
  .publications h2.bibliography.collapsed { cursor: pointer; }
  /* Hit-area extension around the ghost triangle */
  .publications .bib-header::before {
    content: '';
    position: absolute;
    inset: -0.45rem;
  }
  /* Ghost year span: must override gem's span rule (font-size:1.5rem and color:global-text) */
  .publications .bib-year-num {
    display: block;
    width: max-content;
    font-size: 5rem;
    color: rgba(78, 111, 163, 0.12);
    transition: transform 0.36s ease, color 0.36s ease;
  }
  /* Year becomes more prominent when sliding to collapsed position (class toggled by JS at slide time) */
  .publications .bib-year-num.bib-year-dim { color: rgba(78, 111, 163, 0.38); }
  html[data-theme=dark] .publications .bib-year-num.bib-year-dim { color: rgba(124, 160, 197, 0.45); }
  /* Badge children inherit the badge's gray and font-size — overrides gem's span rules */
  .publications .bib-header span { color: inherit; font-size: inherit; }
  .publications h2.bibliography.arrow-ready:hover .bib-header { opacity: 0.72 !important; }
  .publications h2.bibliography.arrow-ready .bib-header:hover { opacity: 0.9 !important; }
  html[data-theme=dark] .publications .bib-header { color: rgba(124, 160, 197, 0.36); }
  /* Glass filter input */
  #bibsearch {
    display: block;
    width: 100%;
    margin: 0 0 2.5rem;
    padding: 0.62rem 1rem 0.62rem 2.4rem;
    font-size: 0.88rem;
    font-family: 'DM Sans', sans-serif;
    letter-spacing: 0.02em;
    color: var(--global-text-color);
    background:
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='none' stroke='%234e6fa3' stroke-opacity='.45' stroke-width='1.6' stroke-linecap='round'%3E%3Ccircle cx='8.5' cy='8.5' r='5.5'/%3E%3Cpath d='m14 14 3.5 3.5'/%3E%3C/svg%3E") no-repeat 0.8rem center / 1rem,
      color-mix(in srgb, var(--global-bg-color) 60%, transparent);
    backdrop-filter: blur(16px) saturate(1.4);
    -webkit-backdrop-filter: blur(16px) saturate(1.4);
    border: 1px solid color-mix(in srgb, var(--global-theme-color) 20%, transparent);
    border-radius: 0.5rem;
    box-shadow:
      0 2px 12px rgba(78, 111, 163, 0.07),
      inset 0 1px 0 rgba(255, 255, 255, 0.6);
    outline: none;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }
  #bibsearch::placeholder { color: var(--global-text-color-light); opacity: 0.7; }
  #bibsearch:focus {
    border-color: color-mix(in srgb, var(--global-theme-color) 40%, transparent);
    box-shadow:
      0 2px 16px rgba(78, 111, 163, 0.13),
      inset 0 1px 0 rgba(255, 255, 255, 0.6),
      0 0 0 3px rgba(78, 111, 163, 0.07);
  }
  html[data-theme=dark] #bibsearch {
    background:
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='none' stroke='%237a9fc4' stroke-opacity='.45' stroke-width='1.6' stroke-linecap='round'%3E%3Ccircle cx='8.5' cy='8.5' r='5.5'/%3E%3Cpath d='m14 14 3.5 3.5'/%3E%3C/svg%3E") no-repeat 0.8rem center / 1rem,
      color-mix(in srgb, var(--global-bg-color) 35%, transparent);
    border-color: color-mix(in srgb, var(--global-theme-color) 22%, transparent);
    box-shadow:
      0 2px 14px rgba(0, 0, 0, 0.18),
      inset 0 1px 0 rgba(255, 255, 255, 0.07);
  }
  html[data-theme=dark] #bibsearch:focus {
    border-color: color-mix(in srgb, var(--global-theme-color) 45%, transparent);
    box-shadow:
      0 2px 18px rgba(0, 0, 0, 0.22),
      inset 0 1px 0 rgba(255, 255, 255, 0.07),
      0 0 0 3px rgba(122, 159, 196, 0.09);
  }
  .publications ol.bibliography { overflow: hidden; transition: max-height 0.36s ease; }
  .publications ol.bibliography > li {
    position: relative;
    padding: 0.4rem 0.5rem;
    border-radius: 1rem;
    overflow: hidden;
    transition: background 0.15s ease, box-shadow 0.2s ease;
  }
  .publications ol.bibliography > li > .row {
    background: transparent !important;
    background-color: transparent !important;
  }
  .publications ol.bibliography > li > .row > div:not(.abbr) {
    transform-origin: center;
    transition: transform 0.2s ease;
  }
  .publications ol.bibliography > li:hover {
    background: var(--global-code-bg-color) !important;
    background-color: var(--global-code-bg-color) !important;
    box-shadow: none;
    position: relative;
    z-index: 1;
  }
  html[data-theme=dark] .publications ol.bibliography > li:hover {
    background: color-mix(in srgb, var(--global-theme-color) 18%, transparent) !important;
    background-color: color-mix(in srgb, var(--global-theme-color) 18%, transparent) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22);
  }
  .publications ol.bibliography > li:hover > .row > div:not(.abbr) {
    transform: scale(1.012);
  }
  .publications ol.bibliography > li:hover .abbr {
    transform: scale(1.035);
  }
  html.bibsearch-pending .publications {
    visibility: hidden;
  }
  /* Hide the Abs button; toggle is on the whole row */
  .publications a.abstract { display: none !important; }
  /* Abstract collapsed — reserve border/padding space to prevent shift on expand */
  .publications .abstract.hidden {
    max-height: 0 !important;
    overflow: hidden !important;
    opacity: 0;
    margin: 0 !important;
    padding: 0 0 0 0.75rem !important;
    border: none !important;
    border-left: 2px solid transparent !important;
    background: none !important;
    transition: max-height 0.28s ease, margin 0.28s ease, opacity 0.16s ease, border-color 0.2s ease !important;
  }
  /* Abstract expanded */
  .publications ol.bibliography > li.abstract-open .abstract.hidden {
    max-height: var(--abstract-height, 600px) !important;
    opacity: 1;
    margin: 0.5rem 0 0.25rem 0 !important;
    border-left: 2px solid var(--global-divider-color) !important;
    color: var(--global-text-color-light) !important;
  }
  .publications div.bibtex.hidden {
    display: block !important;
    max-height: 0 !important;
    overflow: hidden !important;
    opacity: 0;
    margin: 0 !important;
    transition: max-height 0.28s ease, margin 0.28s ease, opacity 0.16s ease !important;
  }
  .publications ol.bibliography > li.bibtex-open div.bibtex.hidden {
    max-height: var(--bibtex-height, 600px) !important;
    opacity: 1;
    margin: 0.5rem 0 0.25rem 0 !important;
  }
  /* Hover hint — JS adds .has-abstract; ::after always in DOM so transition is smooth */
  .publications ol.bibliography > li.has-abstract::after {
    content: "Click to read the abstract";
    position: absolute;
    bottom: 0.5rem;
    right: 0.75rem;
    font-size: 0.72rem;
    color: var(--global-text-color-light);
    opacity: 0;
    transition: opacity 0.2s ease;
    pointer-events: none;
    white-space: nowrap;
    z-index: 2;
  }
  .publications ol.bibliography > li.has-abstract.abstract-open::after {
    content: "Click to close the abstract";
  }
  /* Instantly hide when suppressed */
  .publications ol.bibliography > li.hint-suppress::after {
    opacity: 0 !important;
    transition: none !important;
  }
  /* Show expand hint */
  .publications ol.bibliography > li.has-abstract:not(.abstract-open):not(.hint-suppress):not(:has(a:hover)):hover::after {
    opacity: 0.8;
    transition: opacity 0.2s ease 0.5s;
  }
  /* Show collapse hint */
  .publications ol.bibliography > li.has-abstract.abstract-open:not(.hint-suppress):not(:has(a:hover)):not(:has(.abstract:hover)):hover::after {
    opacity: 0.8;
    transition: opacity 0.2s ease 0.5s;
  }
  @media (prefers-reduced-motion: reduce) {
    .publications ol.bibliography > li > .row > div:not(.abbr) {
      transition: none;
    }
    .publications ol.bibliography > li:hover > .row > div:not(.abbr) {
      transform: none;
    }
    .publications ol.bibliography > li:hover .abbr {
      transform: none;
    }
  }
  @media (max-width: 575.98px) {
    .publications .abbr,
    .publications .abbr + [class*="col-sm-"] {
      flex: 0 0 100%;
      max-width: 100%;
    }
    .publications .abbr {
      margin-bottom: 0.75rem;
    }
    .publications .abbr figure picture {
      aspect-ratio: 16 / 9;
    }
  }
</style>

{% include bib_search.liquid %}

<div class="publications">
{% bibliography %}
</div>

<dialog id="publication-image-lightbox" aria-label="Publication figure">
  <button type="button" aria-label="Close figure">&times;</button>
  <img alt="">
</dialog>

<script>
  const TOPIC_MAP = {
    {%- for topic in site.data.research_topics %}
    {{ topic.slug | jsonify }}: {{ topic.papers | jsonify }}{% unless forloop.last %},{% endunless %}
    {%- endfor %}
  };
  const TOPIC_LABELS = {
    {%- for topic in site.data.research_topics %}
    {{ topic.slug | jsonify }}: {{ topic.label | jsonify }}{% unless forloop.last %},{% endunless %}
    {%- endfor %}
  };
  // Reverse lookup: lowercase label or slug → slug
  const TOPIC_SLUG_MAP = {};
  for (const [slug, label] of Object.entries(TOPIC_LABELS)) {
    TOPIC_SLUG_MAP[slug] = slug;
    TOPIC_SLUG_MAP[label.toLowerCase()] = slug;
  }
</script>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const lightbox = document.getElementById("publication-image-lightbox");
    const fullImage = lightbox.querySelector("img");
    const closeButton = lightbox.querySelector("button");
    const thumbnails = document.querySelectorAll(".publications img.preview");

    const closeLightbox = () => {
      if (lightbox.open) lightbox.close();
    };

    const resetLightbox = () => {
      fullImage.removeAttribute("src");
    };

    thumbnails.forEach((thumbnail) => {
      thumbnail.removeAttribute("data-zoomable");
      thumbnail.addEventListener("click", () => {
        fullImage.src = thumbnail.src;
        fullImage.alt = thumbnail.alt;
        lightbox.showModal();
        closeButton.focus();
      });
    });

    closeButton.addEventListener("click", closeLightbox);
    lightbox.addEventListener("close", resetLightbox);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) closeLightbox();
    });

    // Add Boolean queries while retaining /pattern/flags as an escape hatch.
    // Precedence is NOT, then AND, then OR; parentheses can override it.
    const buildSearchPredicate = (query) => {
      const regexQuery = query.match(/^\/(.+)\/([dgimsuvy]*)$/);
      if (regexQuery) {
        try {
          const expression = new RegExp(regexQuery[1], regexQuery[2].replace(/[gy]/g, ""));
          return (text) => expression.test(text);
        } catch {
          return null;
        }
      }

      if (!/(^|\s)(?:AND|OR|NOT)(?=\s|$)|[()]/i.test(query)) return null;
      const tokens = [];
      const syntax = /\(|\)|\bAND\b|\bOR\b|\bNOT\b/gi;
      let textStart = 0;
      for (const match of query.matchAll(syntax)) {
        const term = query.slice(textStart, match.index).trim();
        if (term) tokens.push({ type: "TERM", value: term.toLowerCase() });
        tokens.push({ type: match[0].toUpperCase() });
        textStart = match.index + match[0].length;
      }
      const finalTerm = query.slice(textStart).trim();
      if (finalTerm) tokens.push({ type: "TERM", value: finalTerm.toLowerCase() });

      let position = 0;
      const parsePrimary = () => {
        const token = tokens[position];
        if (token?.type === "TERM") {
          position += 1;
          return { type: "TERM", value: token.value };
        }
        if (token?.type === "(") {
          position += 1;
          const expression = parseOr();
          if (!expression || tokens[position]?.type !== ")") return null;
          position += 1;
          return expression;
        }
        return null;
      };
      const parseNot = () => {
        if (tokens[position]?.type === "NOT") {
          position += 1;
          const operand = parseNot();
          return operand ? { type: "NOT", operand } : null;
        }
        return parsePrimary();
      };
      const parseAnd = () => {
        let expression = parseNot();
        if (!expression) return null;
        while (tokens[position]?.type === "AND") {
          position += 1;
          const right = parseNot();
          if (!right) return null;
          expression = { type: "AND", left: expression, right };
        }
        return expression;
      };
      function parseOr() {
        let expression = parseAnd();
        if (!expression) return null;
        while (tokens[position]?.type === "OR") {
          position += 1;
          const right = parseAnd();
          if (!right) return null;
          expression = { type: "OR", left: expression, right };
        }
        return expression;
      }

      const tree = parseOr();
      if (!tree || position !== tokens.length) return null;
      const evaluate = (node, text) => {
        if (node.type === "TERM") return text.includes(node.value);
        if (node.type === "NOT") return !evaluate(node.operand, text);
        if (node.type === "AND") return evaluate(node.left, text) && evaluate(node.right, text);
        return evaluate(node.left, text) || evaluate(node.right, text);
      };
      return (text) => evaluate(tree, text.toLowerCase());
    };

    const applyTopicFilter = (slug) => {
      const keys = TOPIC_MAP[slug];
      if (!keys) return;
      const keySet = new Set(keys);
      document.querySelectorAll(".bibliography, .unloaded").forEach((el) => el.classList.remove("unloaded"));
      document.querySelectorAll("ol.bibliography > li").forEach((item) => {
        const citeKey = item.querySelector("div[id]")?.id ?? "";
        item.classList.toggle("unloaded", !keySet.has(citeKey));
      });
      document.querySelectorAll("h2.bibliography").forEach((heading) => {
        let sibling = heading.nextElementSibling;
        let hasVisible = false;
        while (sibling && sibling.tagName !== "H2") {
          if (sibling.tagName === "OL") {
            const has = Boolean(sibling.querySelector(":scope > li:not(.unloaded)"));
            sibling.classList.toggle("unloaded", !has);
            hasVisible ||= has;
          }
          sibling = sibling.nextElementSibling;
        }
        heading.classList.toggle("unloaded", !hasVisible);
      });
    };

    const syncBibSearchFromHash = () => {
      const input = document.getElementById("bibsearch");
      if (!input || !window.location.hash) return;
      const hash = decodeURIComponent(window.location.hash.substring(1));
      if (hash.startsWith("topic:")) return;
      input.value = hash;
    };

    const applyEnhancedBibSearch = () => {
      const input = document.getElementById("bibsearch");
      const query = input?.value.trim() || "";
      const matchesQuery = buildSearchPredicate(query);
      if (!matchesQuery) return;

      document.querySelectorAll(".bibliography, .unloaded").forEach((element) => element.classList.remove("unloaded"));
      document.querySelectorAll("ol.bibliography > li").forEach((item) => {
        item.classList.toggle("unloaded", !matchesQuery(item.textContent || ""));
      });

      document.querySelectorAll("h2.bibliography").forEach((heading) => {
        let sibling = heading.nextElementSibling;
        let hasVisiblePapers = false;
        while (sibling && sibling.tagName !== "H2") {
          if (sibling.tagName === "OL") {
            const hasVisibleInList = Boolean(sibling.querySelector(":scope > li:not(.unloaded)"));
            sibling.classList.toggle("unloaded", !hasVisibleInList);
            hasVisiblePapers ||= hasVisibleInList;
          }
          sibling = sibling.nextElementSibling;
        }
        heading.classList.toggle("unloaded", !hasVisiblePapers);
      });
    };

    let shouldSyncBibSearchFromHash = Boolean(window.location.hash);
    const finishBibSearch = () => {
      const hash = window.location.hash ? decodeURIComponent(window.location.hash.substring(1)) : "";
      if (hash.startsWith("topic:")) {
        const slug = hash.slice(6);
        const input = document.getElementById("bibsearch");
        if (input) input.value = "topic: " + (TOPIC_LABELS[slug] || slug);
        applyTopicFilter(slug);
        CSS.highlights?.delete("search");
        updateYearCounts();
        document.documentElement.classList.remove("bibsearch-pending");
        return;
      }
      if (shouldSyncBibSearchFromHash) {
        syncBibSearchFromHash();
        shouldSyncBibSearchFromHash = false;
      }
      applyEnhancedBibSearch();
      CSS.highlights?.delete("search");
      updateYearCounts();
      document.documentElement.classList.remove("bibsearch-pending");
    };
    const scheduleFinishedBibSearch = () => setTimeout(finishBibSearch, 0);

    // Capture phase: runs before the gem's bubble-phase filterItems listener.
    // Routes topic: queries to applyTopicFilter and stops propagation so the gem
    // never receives them. Non-topic input falls through to the gem normally.
    document.getElementById("bibsearch")?.addEventListener("input", function (event) {
      const val = this.value.trim();
      const lower = val.toLowerCase();
      if (lower.startsWith("topic:")) {
        event.stopImmediatePropagation();
        const query = lower.replace(/^topic:\s*/, "");
        const slug = TOPIC_SLUG_MAP[query] || query;
        if (TOPIC_MAP[slug]) {
          applyTopicFilter(slug);
        } else {
          document.querySelectorAll(".bibliography, .unloaded").forEach((el) => el.classList.remove("unloaded"));
        }
        updateYearCounts();
        return;
      }
      // Non-topic: clear any residual topic hash, then let gem + enhanced search run
      const hash = window.location.hash ? decodeURIComponent(window.location.hash.substring(1)) : "";
      if (hash.startsWith("topic:")) history.replaceState(null, "", window.location.pathname + window.location.search);
      scheduleFinishedBibSearch();
    }, true);
    window.addEventListener("hashchange", () => {
      shouldSyncBibSearchFromHash = true;
      document.documentElement.classList.add("bibsearch-pending");
      scheduleFinishedBibSearch();
    });
    setTimeout(finishBibSearch, 0);

    // Click-to-expand abstract: move panel before .links, toggle on click
    const pubRows = [];
    const selectionAtMouseDown = new WeakMap();
    document.querySelectorAll(".publications ol.bibliography > li").forEach((li) => {
      const panel = li.querySelector(".abstract.hidden");
      if (!panel || !panel.querySelector("p")) return;
      const linksDiv = li.querySelector(".links");
      if (linksDiv) linksDiv.parentNode.insertBefore(panel, linksDiv);
      const syncAbstractHeight = () => {
        panel.style.setProperty("--abstract-height", `${panel.scrollHeight}px`);
      };
      syncAbstractHeight();
      li.classList.add("has-abstract");
      pubRows.push(li);

      let mdX = 0, mdY = 0;
      li.addEventListener("mousedown", (e) => {
        // A selection from the previous gesture must not consume this click.
        // Remember it so its collapse cannot be mistaken for a new selection.
        delete li.dataset.hadSelection;
        selectionAtMouseDown.set(li, window.getSelection()?.toString() || "");
        mdX = e.clientX;
        mdY = e.clientY;
      });

      li.addEventListener("click", (e) => {
        const dragged = Math.hypot(e.clientX - mdX, e.clientY - mdY) > 4;
        const hadSel = !!li.dataset.hadSelection;
        delete li.dataset.hadSelection;
        if (e.target.closest("a")) return;
        if (e.target.closest(".abstract, .bibtex")) return;
        if (hadSel || dragged) return;
        syncAbstractHeight();
        li.classList.toggle("abstract-open");
        li.classList.add("hint-suppress");
        requestAnimationFrame(() => requestAnimationFrame(() => li.classList.remove("hint-suppress")));
      });
    });

    // selectionchange: set hadSelection when text is selected in a row.
    // Keep it through the current gesture because the browser may clear the
    // selection before click fires; the next mousedown starts a fresh gesture.
    document.addEventListener("selectionchange", () => {
      const sel = window.getSelection();
      const hasText = sel && sel.toString().length > 0;
      pubRows.forEach((li) => {
        const active = hasText && li.contains(sel.anchorNode);
        li.classList.toggle("hint-suppress", active);
        if (active && sel.toString() !== selectionAtMouseDown.get(li)) {
          li.dataset.hadSelection = "1";
        }
      });
    });

    // Once a selection gesture ends, pointer location determines hint visibility.
    // The CSS still hides the close hint while the abstract itself is hovered.
    document.addEventListener("mouseup", () => {
      pubRows.forEach((li) => li.classList.remove("hint-suppress"));
    });

    // Capture-phase click: clear hadSelection for rows not involved in this click,
    // so stale flags don't suppress future clicks after clicking elsewhere.
    document.addEventListener("click", (e) => {
      pubRows.forEach((li) => {
        if (!li.contains(e.target)) delete li.dataset.hadSelection;
      });
    }, true);

    document.querySelectorAll(".publications ol.bibliography > li").forEach((li) => {
      const bibPanel = li.querySelector("div.bibtex.hidden");
      const bibButton = li.querySelector(".links a.bibtex");
      if (!bibPanel || !bibButton) return;

      const syncBibtexHeight = () => {
        bibPanel.style.setProperty("--bibtex-height", `${bibPanel.scrollHeight}px`);
      };
      syncBibtexHeight();

      bibButton.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        syncBibtexHeight();
        li.classList.toggle("bibtex-open");
      }, true);
    });

    // Year ghost triangles (updates on search too via finishBibSearch)
    const updateYearCounts = () => {
      document.querySelectorAll(".publications h2.bibliography").forEach((h2) => {
        let next = h2.nextElementSibling;
        let count = 0;
        while (next && next.tagName !== "H2") {
          if (next.tagName === "OL") count += next.querySelectorAll(":scope > li:not(.unloaded)").length;
          next = next.nextElementSibling;
        }
        h2.dataset.count = count;
        const bibHeader = h2.querySelector(".bib-header");
        if (bibHeader) {
          bibHeader.firstChild.textContent = "◂";
          if (count === 0) {
            bibHeader.style.display = "none";
          } else {
            bibHeader.style.display = "";
            bibHeader.style.opacity = h2.classList.contains("collapsed") ? "0" : "0.46";
            if (!h2.classList.contains("collapsed")) h2._bibSnap?.();
          }
        }
      });
    };

    // Year section: a ghost triangle appears beside the year; the year itself toggles.
    document.querySelectorAll(".publications h2.bibliography").forEach((h2) => {
      const ol = h2.nextElementSibling?.tagName === "OL" ? h2.nextElementSibling : null;
      // Count directly from DOM — data-count is set async so we can't rely on it here
      const initialCount = ol ? ol.querySelectorAll(":scope > li").length : 0;

      // Wrap the year text node in .bib-year-num so it can slide independently
      const textNode = Array.from(h2.childNodes).find(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim());
      const yearSpan = document.createElement("span");
      yearSpan.className = "bib-year-num";
      yearSpan.textContent = textNode ? textNode.textContent.trim() : h2.textContent.trim();
      if (textNode) textNode.replaceWith(yearSpan); else { h2.textContent = ""; h2.appendChild(yearSpan); }

      // Inject .bib-header BEFORE the year span
      const header = document.createElement("span");
      header.className = "bib-header";
      const arrow = document.createElement("span");
      arrow.textContent = "◂";
      arrow.setAttribute("aria-hidden", "true");
      header.appendChild(arrow);
      if (initialCount === 0) header.style.display = "none";
      h2.insertBefore(header, yearSpan);

      const arrowOffset = 0.15 * parseFloat(getComputedStyle(document.documentElement).fontSize);

      // Snap year to the right edge and triangle just outside it (noop when collapsed)
      function snapRight() {
        if (h2.classList.contains("collapsed")) return;
        const w = h2.offsetWidth;
        header.style.transition = yearSpan.style.transition = "none";
        const yearX = w - yearSpan.offsetWidth;
        yearSpan.style.transform = `translateX(${yearX}px)`;
        header.style.transform = `translateX(${w + arrowOffset}px)`;
        header.offsetHeight; // force reflow
        header.style.transition = yearSpan.style.transition = "";
      }
      snapRight();
      // Fade in badge after it is positioned (badge starts at opacity:0 in CSS)
      requestAnimationFrame(() => {
        header.style.opacity = initialCount === 0 ? "0" : "0.46";
        if (initialCount !== 0) h2.classList.add("arrow-ready");
      });
      h2._bibSnap = snapRight; // expose so updateYearCounts can re-snap after label changes
      new ResizeObserver(snapRight).observe(h2);

      // No fixed max-height when expanded — abstracts inside must be free to grow.
      // Before collapsing we freeze to the actual rendered height, so the CSS transition
      // always has a real px value to animate from regardless of what's open inside.
      if (ol) ol.style.maxHeight = "none";

      // Sequential toggle:
      //   Collapse → ol hides first, then year slides left
      //   Expand   → year slides right first, then ol shows
      // Uses setTimeout (not transitionend) so clearTimeout always works even when
      // the CSS value hasn't changed (transitionend wouldn't fire in that case).
      const DUR = 360; // matches CSS transition durations
      const ARROW_DELAY = 120;
      let pendingTimer = null, unclipTimer = null, arrowTimer = null;
      function clearPending() {
        clearTimeout(pendingTimer); pendingTimer = null;
        clearTimeout(unclipTimer); unclipTimer = null;
        clearTimeout(arrowTimer); arrowTimer = null;
      }
      function toggle() {
        clearPending();
        const collapsing = !h2.classList.contains("collapsed");
        h2.classList.toggle("collapsed");
        const dur = window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : DUR;
        if (collapsing) {
          if (ol) {
            // Freeze to actual rendered height before animating to 0.
            // getBoundingClientRect().height gives the real on-screen height even
            // when max-height is "none" or the element is mid-animation.
            const currentH = ol.getBoundingClientRect().height;
            ol.style.transition = "none";
            ol.style.maxHeight = currentH + "px";
            ol.offsetHeight; // force reflow so transition:none takes effect
            ol.style.transition = "";
            ol.style.maxHeight = "0";
          }
          pendingTimer = setTimeout(() => {
            yearSpan.classList.add("bib-year-dim");
            h2.classList.remove("arrow-ready");
            header.style.transform = yearSpan.style.transform = "translateX(0)";
            header.style.opacity = "0";
          }, dur);
        } else {
          const w = h2.offsetWidth;
          const expandedH = ol ? ol.scrollHeight : 0;
          yearSpan.classList.remove("bib-year-dim");
          h2.classList.remove("arrow-ready");
          const yearX = w - yearSpan.offsetWidth;
          header.style.opacity = "0";
          yearSpan.style.transform = `translateX(${yearX}px)`;
          header.style.transform = `translateX(${w + arrowOffset}px)`;
          arrowTimer = setTimeout(() => {
            h2.classList.add("arrow-ready");
            header.style.opacity = "0.46";
          }, dur + ARROW_DELAY);
          pendingTimer = setTimeout(() => {
            if (ol) {
              ol.style.maxHeight = expandedH + "px";
              // Once the expand animation finishes, lift the cap so abstracts can grow freely
              unclipTimer = setTimeout(() => {
                unclipTimer = null;
                if (!h2.classList.contains("collapsed")) ol.style.maxHeight = "none";
              }, DUR);
            }
          }, dur);
        }
      }
      header.addEventListener("click", (e) => { e.stopPropagation(); toggle(); });
      h2.addEventListener("click", (e) => {
        if (!e.target.closest(".bib-header")) toggle();
      });
    });

    // Re-snap after webfonts load so translateX uses real font metrics
    document.fonts.ready.then(() => {
      document.querySelectorAll(".publications h2.bibliography").forEach(h2 => h2._bibSnap?.());
    });

  });
</script>
