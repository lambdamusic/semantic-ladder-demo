# Claude Code: project instructions

An experiment on how much an LLM gains from being told what data means. It asks the same questions over the same invented data in different forms (CSV, RDF, ontology as Turtle or Markdown, OWL and SHACL axioms, rules already executed), reading the rows or writing SQL and SPARQL over them, and grades the answers by code. The results are on the website, https://semantic-ladder.michelepasin.org.

Read `README.md` for what it is and the layout, `BUILDING.md` for every command (running, building, checking, the website), and `notes/lab-notebook.md` (the lab notebook, a working log) for every run's findings in order. The open experiments are listed under Future work at the end of `docs/conclusions.md`. Personal or machine-specific instructions, if any, go in `CLAUDE.local.md`, which is gitignored.

## Working here

- **Run everything from the repo root** with Python 3.13 and the packages in `requirements.txt`: the scripts are in `src/` (`src/run.py`, `src/query.py`), a domain's build scripts in its folder.
- **Models:** called through the `claude` command line in print mode, from an empty directory with no tools (`src/providers.py`).
- **All data is invented and must stay labelled so:** the companies, LEIs, ratings, Valdoria and Corvenia, and the works, people and institutions. Don't present any of it as a rating agency's or a bibliographic database's data or definitions.
- **The repo is public,** so everything committed is published. Commit results once a run finishes. `site/` is the generated website, written by `tools/site-dump`.
- **Runs take time.** A reading run on a base dataset takes 10 to 40 minutes, a query run with six conditions about an hour, and runs on the larger datasets two to four hours. Run them in the background and don't edit a domain's files while a run on that domain is going. Prompts are frozen at the start of a run, but query mode reads the store's data at each session. `--resume <run>` takes the run's domain, model, conditions and questions from its folder; `--regrade` still needs `--domain`.
- **Refusals and breakdowns happen.** The API sometimes refuses a session ("safeguards flagged this message"): resume the run to ask it again. A model sometimes answers only part of the questions, or writes a SPARQL query as tool-call markup and ends with no answers. Those are kept as they are and reported, not re-asked.
- **GraphDB** (optional): runs with `--store graphdb` use a repository of their own, `semantics-ladder`, cleared and loaded each session, at `GRAPHDB_URL` (default `localhost:7200`). Leave any other repository on the server alone.
- **Docs are for readers who only know this repo:** the README, `BUILDING.md` and the web pages describe the experiment as it stands, not its history. The lab notebook is the one place for history.

## Conventions

- Every key is computed from the data by the domain's `build_questions.py`, and checked against a key written by hand in the base domains. Never edit `questions.json` by hand. When a key is found wrong, fix the rule, rebuild the questions, write the new key into the affected runs' own `questions.json`, and regrade them.
- Each run folder keeps its own `questions.json`, prompts and `meta.json` (with the commit). Regrading (`src/run.py --domain <d> --regrade <run>`) uses the run's own questions, because keys change when a domain does.
- After changing a domain, the grading or the report format, run `tools/rebuild --check`: it rebuilds every dataset and regrades every run in a scratch copy of the last commit, and should report that it matches file for file.
- A domain's meaning lives in `ontology/ontology.ttl`, beside `axioms.ttl` (checked against the keys by the domain's `check_axioms.py`) and the decoy `padding.md`. `ontology.md` is generated from it by `src/ontology_to_md.py`, and must never be edited by hand. The scaled copies (`credit_300`, `credit_paths`, `research_850`) get their ontology files copied by the build script, so don't regenerate theirs: they have no converter, and the column names would drop out. `data/inferred.ttl`, the graph after the SHACL rules, is a cache, gitignored and rebuilt on demand.
- The web pages' text lives in `docs/`: `docs/goals.md`, `method.md`, `scores.md` and `conclusions.md`, and `docs/<dataset>/<section>.md` (a dataset's `scores.md` goes under its table on the scores page). The numbers in a page's text don't update themselves, but the tables do: one column per model, mode and store, filled from the latest runs on the current questions. Conditions a dataset leaves out on purpose are listed in `LEFT_OUT` in `src/web/apps/lab/files.py`.
- Score cells on the Scores and Conclusions pages are shaded by `src/web/static/js/site.js`, from any table cell holding one percentage. Keep scores written as "84%" in the docs' tables so they shade.
