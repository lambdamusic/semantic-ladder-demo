# Claude Code: project instructions

An experiment on how much an LLM gains from being told what data means. It asks the same questions over the same invented data in different forms (CSV, RDF, ontology as Turtle or Markdown, OWL and SHACL axioms, rules already executed), reading the rows or writing SQL and SPARQL over them, and grades the answers by code. It's meant to become a public repo and a blog post. Built by Michele Pasin. It started as a clean copy of the semantics-ladder folder in `~/dev2/credit-graph-lab_2026`, which is a separate project.

Read `README.md` for the layout and commands, `PLAN.md` for the phases and what's left, `RESULTS.md` for every run's findings in order, and the newest note in `backlog/log/` for where the last session stopped. Open work is in `backlog/TODO.md`, managed with the `backlog` skill. The backlog is gitignored, so it stays local.

## Working here

- **Python:** the virtualenv `~/Envs/semantics-ladder` (Python 3.13), created by Michele. Run everything with `~/Envs/semantics-ladder/bin/python` from the repo root: the scripts are in `src/` (`src/run.py`, `src/query.py`), a domain's build scripts in its folder. Never use `workon` or `source`. If a package is missing, add it to `requirements.txt` (pinned) and ask Michele to install it, rather than making another env.
- **Models:** called through the `claude` command line in print mode, from an empty directory with no tools (`providers.py`). This costs nothing extra. Gemini is a later, secondary step: its key goes in the `GEMINI_API_KEY` environment variable, never in a file. Opus and Gemini are set aside for now, by Michele's decision.
- **All data is invented and must stay labelled so:** the companies, LEIs, ratings, Valdoria and Corvenia, and the works, people and institutions. Don't present any of it as a rating agency's or a bibliographic database's data or definitions.
- **Git:** pushed to https://github.com/lambdamusic/semantic-ladder-demo (private until it goes public, `backlog` #10). Commit as you go, and push when Michele asks, with results committed once a run finishes. `site/` is the generated static site: Michele checks and commits it himself. `docs/` is for Markdown documentation.
- **Paths:** the macOS username is `michele.pasin`, so check every `/Users/` path.
- **Runs take time.** A reading run takes 10 to 30 minutes, and a query run with six conditions takes about an hour. Run them in the background and don't edit a domain's files while a run on that domain is going. Prompts are frozen at the start of a run, but query mode reads the store's data at each session.
- **Web app:** `tools/run-web` serves http://127.0.0.1:8030. Michele usually runs it himself, so don't start or stop his server. `tools/site-dump` uses its own server on port 8031 and writes `site/`. `.github/workflows/pages.yml` publishes `site/` to GitHub Pages on a push to `main`.
- **Docs are for readers who only know this repo:** the README, plan, results log and web pages describe the experiment as it stands, not what changed from the pilot that came before it.

## Conventions

- Every key is computed from the data by the domain's `build_questions.py`, and checked against a key written by hand in the base domains. Never edit `questions.json` by hand.
- Each run folder keeps its own `questions.json`, prompts and `meta.json` (with the commit). Regrading (`src/run.py --regrade <run>`) uses the run's own questions, because keys change when a domain does.
- A domain's meaning lives in `ontology.ttl`. `ontology.md` is generated from it by `src/ontology_to_md.py`, and must never be edited by hand.
- The web pages' text lives in `src/web/content/<domain>/<section>.md`. The numbers in a page's text don't update themselves, but the tables below the text do.
