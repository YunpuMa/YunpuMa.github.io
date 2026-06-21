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
- Edit institutional details in `_pages/contact.md`.

Before deploying to GitHub Pages, set `url` and `baseurl` in `_config.yml`.
