# docs

The text of the web pages, in Markdown: `intro.md`, `findings.md` and `results.md` for the experiment's own pages, and a folder per dataset (`credit/`, `credit_300/`, `credit_paths/`, `research/`) with its `intro.md`, `data.md`, `questions.md`, `ontology.md` and `results.md`. The web app in `src/web/` reads them when a page opens, and adds the tables, data and runs below the text. Links in them are the site's own paths, so they work on the site rather than on GitHub.

The static site is not here: `tools/site-dump` writes it to `site/`, and `.github/workflows/pages.yml` publishes it.
