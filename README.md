# Semantics ladder

How much does an LLM gain from being told what data *means*? The same questions, over the
same facts, given to a model in different ways: the data alone, the data as RDF, the data
with an ontology that defines every term and code, the ontology as logical axioms, and the
data after its rules have run. The model either reads the rows or writes SQL and SPARQL over
them, and every answer is graded by code. After Andrea Splendiani's
["Ontologies for AI in practice / part I"](https://www.linkedin.com/pulse/ontologies-ai-practice-part-i-andrea-splendiani-fpihe/)
(October 2026), which ran a family-tree question up a similar ladder.

`RESULTS.md` records what each run showed, in order. `PLAN.md` sets out the questions the
experiment should answer and what's left to do.

**All the data is invented.** The credit domain's companies, LEIs, ratings, Valdoria and
Corvenia are made up, and its ontology isn't any rating agency's definitions. The research
domain's works, people and institutions are made up too, shaped like OpenAlex but not taken
from it.

## How it works

- **Each domain is a folder** in `domains/`, with its data, its ontology, its questions and
  how to build each condition's prompt.
- **Every question hides a meaning the rows don't state:** an implicit meaning any analyst
  would know, or a local rule that only this dataset sets for itself.
- **Answers are graded by code.** Each answer ends with a JSON block holding a typed answer
  per question (a rating, yes, no or depends, record IDs, a count), compared with a key
  computed from the data. Only questions with no typed answer, such as "why?", go to an LLM
  grader, with a checklist, and each is graded twice so the grader's own agreement is
  measured.
- **Questions are the unit of analysis.** `report.py` gives each condition's accuracy with a
  95% bootstrap interval over questions, and paired differences between conditions.
- **Any model, through one call.** `providers.py` takes `provider:model`. Claude runs through
  the `claude` command line, from an empty directory with no tools, settings or MCP servers,
  so it sees only the prompt. The keys are never sent to it. Gemini is planned.

## Layout

| | |
|---|---|
| `src/run.py` | the reading ladder: asks, grades and writes the report. Conditions: `csv`, `rdf`, `rdf+ontology`, `csv+ontology`, `csv+markdown` (the same definitions as Markdown), `csv+padding` (finance text of the same length, about none of this: the length control), `csv+neutral` (the ontology with one slanted sentence made neutral), `executed` (the data after its rules have run, with no definitions), and `csv+axioms` (the ontology's names and codes with the definitions removed, plus OWL axioms and SHACL rules), with or without `+markdown` |
| `src/query.py` | the querying ladder: the model never sees the rows, but writes SQL (DuckDB) or SPARQL (rdflib), and the runner sends back each query's results. Conditions: `sql`, `sql+markdown`, `sparql`, `sparql+ontology`, `sql+executed`, `sparql+axioms` |
| `src/grade.py` | grading by code, and by an LLM with a checklist |
| `src/report.py` | accuracy with intervals, paired differences, grader agreement |
| `src/reasons.py` | checks whether answers graded correct rest on sound reasoning |
| `src/providers.py` | `ask(text, system, model)` for each provider |
| `src/ontology_to_md.py` | writes a domain's `ontology.md` from its `ontology.ttl`, so the two can't drift |
| `src/web/` | the web pages (see below) |
| `domains/credit/` | credit ratings: `data/` (three CSV files and `facts.ttl`), `ontology.ttl`, `axioms.ttl` (checked by `check_axioms.py`), `questions.json` (48 questions with typed keys, written by `build_questions.py`, which stops if a key disagrees with the data), `domain.py`, `execute.py`, `csv_to_rdf.py`, and `concepts.md`, the credit terms explained for people. `scale.py` and `paths.py` build the larger copies |
| `domains/credit_100/`, `credit_300/` | the credit domain at 100 and 300 issuers |
| `domains/credit_paths/` | 300 issuers plus six deep ownership groups, with 61 questions, 13 of which follow links |
| `domains/research/` | research analytics: works, authors, institutions and citations, with 48 questions; `NOTES.md` describes how it was built |
| `results/<domain>/<timestamp>-<model>/` | per run: `meta.json` (with the commit), `questions.json`, the prompts, the answers, `grades.json`, `report.md` |

## Running it

Needs Python 3.13 with the packages in `requirements.txt`, and, for Claude, the `claude`
command line. Run everything from the repo root.

```bash
python src/run.py                          # credit, Sonnet, all conditions, 5 repeats
python src/run.py --runs 1 --only csv      # a quick check
python src/run.py --domain research        # another domain
python src/run.py --resume results/credit/<run>    # finish a stopped run
python src/run.py --regrade results/credit/<run>   # redo the code grading, with the run's own questions
python src/report.py results/credit/<run>          # rebuild a report
python src/query.py --domain credit_300            # the model writes SQL or SPARQL instead of reading the data
python src/reasons.py results/credit/<run>         # check the reasoning behind correct answers

python domains/credit/csv_to_rdf.py        # after editing a CSV
python domains/credit/build_questions.py   # after editing a CSV or a question: checks every key against the data
python domains/credit/execute.py           # then: the tables for the executed condition
python domains/credit/scale.py 300         # a scaled copy: domains/credit_300
python domains/credit/paths.py             # 300 issuers plus deep groups and path questions: domains/credit_paths
python src/ontology_to_md.py credit        # after editing ontology.ttl
```

## The web pages

```bash
tools/run-web        # http://127.0.0.1:8030
```

A Django app in `src/web/` that shows the experiment from its own files, read when each
page opens: this README, the plan and the results log; each domain's data, questions and
ontology; and every run, with accuracy and intervals, a grid of marks by question, every
answer to a question, the prompts, and for query runs each session's queries and results.
No database. The pages' text is in `src/web/content/`.

```bash
tools/site-dump      # the same pages as a static site in site/, for GitHub Pages (needs wget)
```

It runs its own server on port 8031, mirrors every page with wget, and syncs the result into
`site/`. It doesn't commit: check `site/` and commit it. On a push to `main`, `.github/workflows/pages.yml`
publishes `site/` to GitHub Pages. `docs/` is for the project's own Markdown documentation.
