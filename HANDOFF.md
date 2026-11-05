# Handoff: 5 November 2026

The previous session ran in `~/dev2/credit-graph-lab_2026` and built this repo from scratch over 4 November. This is where it stopped.

## State

- **Every run is finished and committed** (last commit `419a9ce`). Nothing is running in the background.
- **`site/` is generated and uncommitted:** 974 pages, 20 MB, made by `tools/site-dump` after the last run. Michele will check it, commit it, push the repo, and set Settings > Pages > Source to "GitHub Actions". `.github/workflows/pages.yml` then publishes `site/` on each push to `main`. Rerun `tools/site-dump` after any new run or page edit. `docs/` is kept for Markdown documentation.
- **The web app** has the first round's structure. In the sidebar, "The experiment" holds the introduction, results log, plan, all runs and the README. Each domain then gets its own group: Credit ratings, Credit at 300 issuers, Credit: ownership paths, Research analytics. Each group has Introduction, Data, Questions and traps, Ontology and Results pages. The text comes from `src/web/content/`. The theme is teal and amber, so it looks different from the credit lab's navy.

## The domains

| Folder | What | Rules |
|---|---|---|
| `domains/credit` | the base credit domain: 19 entity records, 48 questions | v2, since commit 18a2f42: domicile from RESEARCH, names and parents from RATINGS |
| `domains/credit_100`, `credit_300` | `scale.py` copies, 48 questions | still v1 (domicile from RATINGS); `credit_300` holds the reading and querying runs at 300 issuers |
| `domains/credit_paths` | `paths.py`: 300 issuers plus six deep groups, 61 questions (Q49 to Q61 follow links); `anchors.json` names the designed entities | v2 |
| `domains/research` | invented, shaped like OpenAlex; 48 questions; built by a subagent and reviewed (`NOTES.md`) | its own five local rules; has `executed`, no axioms |

## Main findings so far (detail in `RESULTS.md`)

- **Written-down meaning helps, and the gain sits in each dataset's own rules.**
  - Credit v2: Sonnet goes from 85% to 99–100%, Haiku from 78% to 99–100%.
  - Research: Sonnet goes from 56% to 97–98%, Haiku from 44% to 96–97%.
- **Form matters little.**
  - Markdown matches Turtle, and RDF alone adds nothing.
  - The length control adds nothing.
  - Axioms without prose do as well as prose. They're followed to the letter, mistakes included.
- **One slanted sentence in the prose can flip an answer** (Q10). The axioms carry no slant.
- **Executed rules get close to the definitions:** credit +9 to +15, research +35 to +48. The research misses come from the tables' design: merging preprints hides them, there's no ultimate-parent column, and "why" questions lose their reasons.
- **At 300 issuers, querying beats reading only slightly**, and SQL ties SPARQL once the definitions are given. Long lists are nearly right everywhere: strict accuracy 51–86%, F1 92–100%.
- **On paths:**
  - Without definitions a graph doesn't help.
  - With them, SPARQL is the steadiest querying condition.
  - A precomputed `ancestors` table gives SQL every path right.
  - Reading the 100 KB of CSV with the definitions beats querying.
- **Reasoning check** (`reasons.py`, credit v2 Sonnet): 9% of correct `csv` answers rest on unsound reasoning, against 3% with the definitions. Treat this as indicative only.

## Next (from `PLAN.md`)

1. **Query mode at more sizes, with five repeats.** Three repeats is too few: one bad session moves a path score by about 30 points.
2. **Data too large to read**, for example 3,000 issuers, where querying should finally pay off. `scale.py N` and `paths.py` build the data. `paths.py` has `SIZE = 300` hard-coded.
3. **Research query mode** (`query.py --domain research --only sql sql+markdown sparql sparql+ontology sql+executed`), and research axioms.
4. **Better executed tables:** keep merged records visible, and add an ultimate-parent column (research).
5. **The blog post,** from the tables (the `write-blog` skill). Opus and Gemini later.

## Pitfalls already found (and fixed)

- **rdflib can run a bad SPARQL join for hours.** `query.py` stops each query after 60 seconds (`TIMEOUT`) and counts it as failed.
- **Sonnet sometimes writes queries as `<invoke name="sql">` markup.** `queries_in()` reads that, and the runner asks once when a reply has neither queries nor a JSON answer. Sessions that failed this way are kept in `failed/` in the run folder.
- **`--regrade` once graded v1 runs against v2 keys.** It now uses the run's own `questions.json`. Check that the accuracy tables are unchanged after any regrade.
- **A run folder is named by minute.** Two runs of the same domain and model started in the same minute would share a folder, so space them out (the old background scripts slept 61 seconds between runs).
- **Query mode on credit_300 needs `--only sql sql+markdown sparql sparql+ontology`:** its `domain.py` is an older copy, without `EXECUTED_TABLES` or `AXIOMS_NOTE`. Rebuilding with `scale.py` would update it, but would also move it to the v2 rules and change its keys.
- **`sparql+axioms` builds `data/inferred.ttl` once**, which takes about 2.5 minutes at 300 issuers. Delete the file after changing `axioms.ttl` or the data.

## Outside this repo

`~/dev2/credit-graph-lab_2026/CLAUDE.md` still describes `semantics-ladder/` as a folder in that repo, which was the first round. This repo is the continuation, and that project doesn't need to change.
