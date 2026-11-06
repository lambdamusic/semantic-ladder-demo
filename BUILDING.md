# Building and running the experiment

How to set it up, run it, rebuild every dataset and table, and check that the numbers on the
[web pages](https://semantic-ladder.michelepasin.org) come from the files in this repo. Run every
command from the repo root.

## Setup

- **Python 3.13**, with the packages in `requirements.txt` (rdflib, pySHACL, DuckDB, Django, Markdown):

  ```bash
  python -m venv ~/Envs/semantics-ladder
  ~/Envs/semantics-ladder/bin/pip install -r requirements.txt
  ```

  The scripts in `tools/` use that environment if it exists. Otherwise set `PYTHON=` to another interpreter.
- **The `claude` command line**, logged in, to ask the models. Each call runs `claude -p` with no tools and no
  settings, so the model sees only the prompt (`src/providers.py`). Rebuilding and checking need no model.
- **GraphDB** (optional), only for the SPARQL conditions on GraphDB. The free edition is enough. The runs
  create and use a repository of their own, `semantics-ladder`, with no inference.

## Running the experiment

A run asks one model every question of one dataset under several conditions, five times each, grades the
answers and writes a report. It's saved in `results/<dataset>/<date>-<model>/`, with its prompts,
questions, answers, grades and report, and the commit it ran on.

**Reading** (the model sees the data in its prompt), with `src/run.py`:

```bash
python src/run.py                                        # credit, Sonnet, every condition, 5 repeats
python src/run.py --domain research --model claude:haiku # another dataset, another model
python src/run.py --only csv csv+markdown --runs 1       # some conditions, one repeat: a quick check
python src/run.py --domain credit --dry-run              # write the prompts only
```

**Querying** (the model writes SQL or SPARQL and never sees the rows), with `src/query.py`. Each session has
up to 8 rounds of queries, each result is cut at 60 rows, and a query that runs over 60 seconds is reported
to the model as failed:

```bash
python src/query.py --domain credit_300                  # the six querying conditions, Sonnet, 5 repeats
python src/query.py --domain research --only sql sql+markdown sparql+axioms
python src/query.py --domain credit_paths --only sparql sparql+ontology sparql+axioms --store graphdb
                                                         # SPARQL on GraphDB, at GRAPHDB_URL (default localhost:7200)
```

The datasets are `credit`, `credit_300`, `credit_paths`, `research` and `research_850`. The conditions are
listed on the [Method page](https://semantic-ladder.michelepasin.org/method/), and `--help` lists them too.

**After a run:**

```bash
python src/run.py --resume results/credit/<run>      # finish a stopped run: asks only what's missing
python src/query.py --resume results/credit/<run>    # the same for a querying run
python src/run.py --domain credit --regrade results/credit/<run>
                                                     # regrade by code, against the run's own questions
python src/report.py results/credit/<run>            # rewrite the report from the grades
python src/reasons.py results/credit/<run>           # check the reasoning behind correct answers
```

A resumed run takes its dataset, model, conditions and questions from its own folder. Runs take a while:
10 to 40 minutes for reading on a base dataset, about an hour for querying, two to four hours on the larger
datasets. Don't change a dataset's files while a run on it is going.

## Building the datasets

Every dataset is built by scripts, and every answer key is computed from the data. Never edit
`questions.json` by hand. In the base datasets, each computed key is also checked against one written by
hand, and the build stops if they differ.

**Credit ratings**, from the hand-written CSV files in `domains/credit/data/`:

```bash
python domains/credit/csv_to_rdf.py          # data/facts.ttl: the same rows as RDF
python src/ontology_to_md.py credit          # ontology/ontology.md, from ontology/ontology.ttl
python domains/credit/build_questions.py     # questions.json, with every key checked
python domains/credit/execute.py             # data/executed/: the tables for the executed conditions
python domains/credit/check_axioms.py domains/credit    # run the SHACL rules and print what they derive
python domains/credit/scale.py 300           # domains/credit_300/: 300 more issuers, from a fixed seed
python domains/credit/paths.py               # domains/credit_paths/: 300 issuers, deep groups, 13 path questions
```

**Research analytics**, from a seeded generator:

```bash
python domains/research/generate_data.py     # data/*.csv
python domains/research/csv_to_rdf.py        # data/facts.ttl
python src/ontology_to_md.py research        # ontology/ontology.md
python domains/research/build_questions.py   # questions.json, with every key checked
python domains/research/execute.py           # data/executed/
python domains/research/check_axioms.py domains/research    # check the SHACL rules against the keys
python domains/research/scale.py 850         # domains/research_850/: 850 works, from a fixed seed
```

The scaled copies (`credit_300`, `credit_paths`, `research_850`) get their ontology files copied from the
base domain, so don't regenerate their `ontology.md`: they have no converter of their own, and the CSV
column names would drop out.

Each domain's meaning is in `ontology/`: `ontology.ttl` (the definitions, which `ontology.md` is generated
from and must never be edited by hand), `axioms.ttl` (the same meaning as OWL axioms and SHACL rules) and
`padding.md` (the decoy glossary).

## Checking the numbers

```bash
tools/rebuild --check    # rebuild everything in a scratch copy of the last commit, and list what differs
tools/rebuild            # rebuild everything in place
```

`tools/rebuild` runs every build script above, then regrades every run in `results/` by code from its saved
answers and its own questions, and rewrites its report. It calls no model and takes about a minute. With
`--check`, it does this in a scratch copy and says either that the rebuild matches the last commit file for
file, or which files differ.

## The web pages

```bash
tools/run-web            # the pages, at http://127.0.0.1:8030
tools/site-dump          # the same pages as a static site in site/ (needs wget)
```

The pages are a Django app in `src/web/`, with no database: every page reads the repo's files when it opens,
so a new run shows up on reload. The text is in `docs/`, in Markdown. `tools/site-dump` runs its own server
on port 8031, mirrors every page into `site/`, and leaves you to check and commit it. A push to `main` that
changes `site/` publishes it to GitHub Pages (`.github/workflows/pages.yml`).
