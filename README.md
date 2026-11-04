# Semantics ladder

How much does an LLM gain from being told what data *means*? The same questions, over the
same facts, given to a model in different ways: the data alone, the data as RDF, and the
data with an ontology that defines every term and code. After Andrea Splendiani's
["Ontologies for AI in practice / part I"](https://www.linkedin.com/pulse/ontologies-ai-practice-part-i-andrea-splendiani-fpihe/)
(October 2026), which ran a family-tree question up a similar ladder.

This is the second round. The first, with ten questions graded by an LLM, found a small
gain from the ontology and none from RDF alone, with too little signal to be sure.
`PLAN.md` sets out what this round changes and the questions it should answer.

**All the data is invented.** The credit domain's companies, LEIs, ratings and the Republic
of Valdoria are made up, and the ontology isn't any rating agency's definitions.

## What changed from the first round

- **Answers are graded by code.** Each answer ends with a JSON block holding a typed answer
  per question (a rating, yes, no or depends, record IDs, a count), compared with the key in
  `grade.py`. Records that share an LEI count as one entity. Only questions with no typed
  answer, such as "why?", go to an LLM grader, with a checklist, and each is graded twice
  so the grader's own agreement is measured.
- **Questions are the unit of analysis.** `report.py` gives each condition's accuracy with a
  95% bootstrap interval over questions, and paired differences between conditions.
- **Any model, through one call.** `providers.py` takes `provider:model`. Claude runs
  through the `claude` command line (your Claude Code login, no API key); Gemini is planned.
- **Domains are folders.** `domains/credit/` holds the data, ontology, questions and how to
  build each condition's context, so a second domain can sit beside it.

## Layout

| | |
|---|---|
| `run.py` | asks, grades and writes the report. Conditions: `csv`, `rdf`, `rdf+ontology`, `csv+ontology`, `csv+markdown` (the same definitions as Markdown) and `csv+padding` (finance text of the same length, about none of this: the length control) |
| `ontology_to_md.py` | writes `ontology.md` from `ontology.ttl`, so the two can't drift |
| `grade.py` | grading by code, and by an LLM with a checklist |
| `report.py` | accuracy with intervals, paired differences, grader agreement |
| `providers.py` | `ask(text, system, model)` for each provider |
| `domains/credit/` | `data/` (three CSV files and `facts.ttl`), `ontology.ttl`, `questions.json` (40 questions with typed keys, written by `build_questions.py`, which stops if a key disagrees with the data), `domain.py`, `csv_to_rdf.py`, and `concepts.md`, the credit terms explained for people |
| `results/<domain>/<timestamp>-<model>/` | per run: `meta.json`, the prompts, the answers, `grades.json`, `report.md` |

## Running it

Needs Python 3 with `rdflib` (`pip install -r requirements.txt`) and, for Claude, the
`claude` command line.

```bash
python run.py                          # credit, Sonnet, all four conditions, 5 repeats
python run.py --runs 1 --only csv      # a quick check
python run.py --llm-grade-all          # also grade every answer with the first round's LLM grader
python run.py --resume results/credit/<run>   # finish a stopped run
python report.py results/credit/<run>         # rebuild a report
python domains/credit/csv_to_rdf.py           # after editing a CSV
python domains/credit/build_questions.py      # after editing a CSV or a question: checks every key against the data
```

The model runs from an empty directory with no tools, settings or MCP servers, so it sees
only the prompt. The keys in `questions.json` are never sent to it.
