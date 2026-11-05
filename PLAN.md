# Semantics ladder: plan for the next round

*Written 4 November 2026. The aim is a result solid enough to publish as a blog post and as this repo. The first round's numbers below come from the original experiment, before this repo.*

## Progress (4 November, night)

`RESULTS.md` has the findings; this is what's left of the plan.

- **Done:**
  - Phases 0 and 1, at the base size and at 300 issuers.
  - Phase 2 at 300 issuers and on the path domain, with the rules run in the store as well (`sql+executed`, `sparql+axioms`).
  - Phase 4's research domain, with Sonnet and Haiku, plus its `executed` condition.
  - Credit domain v2: a system-of-record rule that can't be guessed, and the axioms fixed.
  - Partial credit for lists, and a reasoning check (`reasons.py`).
  - The web app, in the first round's structure, and `tools/site-dump`.
- **Left:**
  - Query mode at more sizes, with five repeats: three is too few, since one bad session moves a path score by about 30 points.
  - Data too large to read, where querying should finally pay off.
  - Research query mode, and research axioms.
  - Executed tables that keep the merged records and an ultimate-parent column (the research misses).
  - Opus and Gemini, set aside for now.
  - The blog post.

## Where things stood at the start

- **The ontology helps, but only a little:** `rdf+ontology` minus `csv` is +0.67 out of 10 on the base arm and between 0 and +1.0 across the variants, with Sonnet at three repeats. That's about 7 percentage points, not 1%. Either way it's too small to stand on.
- **The questions are too easy:** six of the ten were right in every condition and every run. All the signal sits in Q5 and Q6, so the gain rests on two questions.
- **RDF alone adds nothing:** `rdf` never beat `csv`, and at scale it was the worst condition at counting (61% exact at 300 issuers), plausibly because it's more than five times the size.
- **The comparison is confounded by length:** the `csv` prompt is 3 KB and `csv+ontology` is 18.5 KB. Some of the gain could come from a longer prompt or more domain words, not from these definitions.
- **The grader adds noise:** an LLM grader marks near-identical answers differently, so the "unstable" counts overstate how much the answers vary. The scale test, graded by code, didn't have this problem.
- **Counting is a separate problem:** the ontology protected identity but not arithmetic. A query should count; the LLM should write and explain it.

## What to claim at the end

Fix the questions before running anything, so the results answer them rather than suggest them:

1. **Does written-down meaning help?** Definitions against none, with the length confound removed.
2. **Does the form of the meaning matter?** Markdown prose, SKOS definitions in RDF, formal axioms, and rules that are executed.
3. **Is it better for the LLM to write queries than to read the data?** And does the store need to be a graph, or will any database do?
4. **Does it hold across models?** Claude Haiku, Sonnet and Opus; Gemini as a secondary step.
5. **Does it hold in another domain?** Research analytics on an OpenAlex slice.

My expectation, to state before the runs: the form of the definitions matters little, and executed rules matter a lot. When the LLM writes queries, the ontology matters *more* than when it reads, and the results stop degrading with size. A graph beats SQL only on questions about paths of unknown depth and on merging sources. The reading gap narrows as models get stronger. Writing this down first is what makes a surprise worth reporting.

## Phase 0: make the experiment able to tell the difference (do first)

Everything after this depends on it. Without it, more conditions only add more noise.

1. **A bigger, harder question bank.** About 40 questions: four or five per implicit meaning, from templates (rating on a date between two actions, alias spelt three ways, guaranteed debt of a finance subsidiary, withdrawal beside a default). Drop or rewrite the ones every condition gets right. *Done when:* no condition scores above about 85% on the base data.
2. **Answers graded by code where possible.** Ask for a JSON block per question (`{"id": "Q3", "answer": "BB+", "records": ["A07"]}`) and compare it with the key in Python. Keep the LLM grader only for the explanation questions (Q5, Q6), and give each of those a checklist of points rather than a model answer. *Done when:* at least three quarters of the questions are graded by code, and the LLM-graded ones are scored twice to measure grader agreement.
3. **A length control.** Add a `csv+padding` condition: the CSV plus a text the same length as the ontology, on finance but not about this data (for example a generic glossary of bond terms). If it scores like `csv+ontology`, the gain was length, not meaning.
4. **Statistics that fit the design.** Questions are the unit, not repeats: two conditions differ when they differ on the same questions. Report accuracy per condition with a bootstrap confidence interval over questions, and paired differences between conditions. Five repeats is enough; more questions buy more certainty than more repeats.
5. **Runner split by provider.** `run.py` calls the `claude` CLI directly. Put the call behind `ask(text, system, provider, model)` so Gemini can slot in, and record the provider, model, temperature and date in every result folder.

## Phase 1: the form of the meaning (Claude, no cost)

Use the same definitions throughout, so only the form changes:

| Condition | What the LLM gets | Question it answers |
|---|---|---|
| `csv` | the data only | the baseline |
| `csv+padding` | the data plus unrelated text of the same length | is it just length? |
| `csv+markdown` | the data plus the definitions as a Markdown glossary, one heading per term | is an ontology just good documentation? |
| `csv+skos` | the data plus today's `ontology.ttl` (definitions in RDF) | what RDF adds to the same prose |
| `csv+axioms` | the data plus OWL and SHACL with the prose definitions removed: keys, cardinalities, disjointness, the ceiling as a SHACL rule | can the model use logic it has to read? |
| `csv+axioms+markdown` | both | do they add up? |
| `executed` | the data after a reasoner and SPARQL have run: merged identities (`owl:sameAs`), the rating in force on each date, ceiling violations flagged | what curation and rules buy (Splendiani's steps 5 and 6) |

- **Generate Markdown from the Turtle** (`ontology_to_md.py`) so both say the same things. Hand-written Markdown would drift.
- **Write the axioms and rules for real:** SHACL shapes and SPARQL rules that run with `pyshacl` and rdflib. The `executed` condition is their output, so the logic is tested as well as read.
- **Keep `rdf` as one condition, not a rung.** It's a finding that format adds nothing, and its prompt is larger, which costs money in Phase 2.
- **Run at two sizes:** base, and the 100-issuer version from the scale test, where reading starts to fail and executed rules should pull ahead.

*Expected result:* `csv+markdown` ≈ `csv+skos`; `executed` clearly best on time, identity and counting; `csv+axioms` alone weaker than prose. That would be the post's main argument: **an ontology's value to an LLM is the meaning it writes down and the rules it runs, not its file format.**

## Phase 2: the LLM writes the queries

So far the LLM reads the data and works out the answer. Here it never sees the rows: it gets a schema, writes a query, the runner executes it and returns the result, and the LLM answers from that. It's the usual argument for knowledge graphs as LLM guardrails (the LLM writes and explains the query, the query counts), so it should be tested, not assumed.

**The loop:** the LLM replies with one query in a fenced block; the runner executes it and sends back the result, or the error; up to five rounds, then the final answer as JSON. The runner owns the loop rather than giving Claude tools, so it works the same for Gemini.

**The conditions** cross the store with the meaning it's given:

| | Schema only | Schema plus definitions | Rules executed in the store |
|---|---|---|---|
| **DuckDB (SQL)** | tables and columns | plus the ontology's definitions, as Markdown and as column comments | plus views: one entity per LEI, the rating in force on a date, the ceiling check |
| **RDF store (SPARQL)** | the classes and properties used | plus `ontology.ttl` | plus `owl:sameAs` and materialised rules, as in Phase 1's `executed` |

**What makes it a fair test of "does it need a graph?":**
- **The same meaning on both sides.** Every rule that becomes SHACL or SPARQL in the graph becomes a view in DuckDB. Without this, the comparison is about how much each side was given, not about graphs.
- **Questions a graph should win.** The toy data has one level of parent, so it can't show a graph's strength. Add questions about ownership chains of unknown depth ("who is at the top of this group?") and about facts merged from several sources. OpenAlex's institution hierarchy gives the same in Phase 4. If SQL ties there too, that's worth reporting: it's your Dimensions-on-BigQuery point, where the graph was the wrong answer.
- **Fluency is a confound.** Models have seen far more SQL than SPARQL. Record syntax errors and rounds used, separately from wrong answers, so "SPARQL was worse" can be split into "harder to write" and "harder to get right".

**What to measure:** accuracy, graded by code; whether the query was right when the answer was wrong, or the other way round; rounds used; failed queries; tokens. Run at all four scale-test sizes: reading fell from 100% to 83% exact between 0 and 300 issuers, and querying should stay flat.

**The likely key finding:** a query is executed exactly, so its errors are errors of meaning, such as counting records instead of entities. That's precisely what the ontology states, so in this mode it becomes a guide to writing queries rather than an aid to reasoning, and should matter more.

## Phase 3: other models

1. **Claude across sizes first** (Haiku, Sonnet, Opus) through the CLI, at no cost, to see whether the gap narrows with capability. Opus already got everything right except Q6 without the ontology.
2. **Gemini, as a secondary step,** through the API. The key goes in the `GEMINI_API_KEY` environment variable, never in a file. Use a Pro and a Flash model, fix the temperature, and record the model version string.
3. **One grader for everyone.** Code grading covers most questions. For the rest, use the same Claude grader across all models, and spot-check a sample with Gemini as the grader, to see whether a model grades its own family more kindly.
4. **Cost:** prompts are 3 to 26 KB (about 1,000 to 6,500 tokens), so a full run of seven conditions with 40 questions is roughly 60,000 input tokens. Five repeats on two models at two sizes comes to a few million tokens, mostly output if thinking is on. The query loop adds a round trip per query. Check current Gemini prices, set a spending cap, and run a single repeat first to measure real cost.

## Phase 4: a second domain, research analytics on OpenAlex

This is the test of whether the finding is about ontologies or about credit. It's also the domain you know best from Dimensions.

**Its implicit meanings** are the equivalents of the credit list:

| Implicit meaning | The trap |
|---|---|
| Who is who | One author under three name variants, matched by ORCID; two different authors with the same name |
| Institution hierarchy | A lab under a university under a system: counting at the wrong level |
| Counting method | Full against fractional counting of co-authored papers |
| Document types | Editorials, errata and paratext counted as research output |
| Versions | A preprint and its published version counted as two works |
| Time windows | Citations counted over different windows for old and new papers |
| Normalisation | Raw citation counts compared across fields, instead of a field-normalised measure |
| Retractions | A retracted paper still counted, or its citations |

**Steps:**
1. **Pick a slice** that contains these traps, from the OpenAlex API or snapshot: one country's institutions in two fields over five years, a few thousand works. Store it in `data/raw/`.
2. **Decide on contamination.** OpenAlex is public and the models may know these institutions. I'd anonymise the names and IDs: keep the structure, invent the labels, and say so. Real data would be closer to how the method is used in practice, but then a correct answer can come from memory.
3. **Write the ontology the same way:** definitions first, then Markdown, SKOS, axioms and executed rules, with the same conditions as Phases 1 and 2. Align it with OpenAlex's own entity types rather than inventing new ones.
4. **About 40 competency questions,** mostly counts and rankings, so they can be graded by code against SPARQL and Python, as in the scale test. Include questions that go up the institution hierarchy to an unknown depth, for the graph against SQL comparison.
5. **Citations: who cites whom, at several levels.** The second hopping case, and the richest one for the graph against SQL comparison. The citation network is between works, but the questions are usually about authors, institutions, countries or fields, so each answer means hopping from works up to one of those levels and aggregating there. Candidate questions:
   - **Citations rolled up a level:** which institutions cite this one most? Each citing work must be counted once per institution, not once per author.
   - **Self-citation, which depends on the level:** citing your own work, your institution's or your country's are three different counts. A good trap, since "self-citation" is ambiguous until the level is stated.
   - **More than one hop:** works that cite the works that cite a paper, or "how close are these two groups in the citation network?"
   - **Communities of citers:** groups of institutions that mostly cite each other. Finding them needs a graph algorithm (community detection in networkx or Kùzu), not a single query, so treat it as a stretch: the runner computes the communities, and the LLM is asked to explain or use them.
   
   A slice with enough citations inside it matters here: pick works in one field over a few years, so that most of their references point to other works in the slice.

*Done when:* the same comparison tables exist for both domains.

## Phase 5: publish

1. **This repo, made public.** It started as a clean copy of the first round, so there's nothing to strip. Add one script that rebuilds every table, a licence and a note on what the runs cost.
2. **A blog post** built on the comparison tables: the claim, Splendiani's experiment as the starting point, the four questions with their answers, and what didn't work. The `write-blog` skill can draft it from the tables.
3. **The first round** stays where it was built, with its own pages, and can link here.
4. **A web app and a static site.** A `src/web/` Django app in the same style as the first round's pages: the experiment, each domain's data, questions, traps and ontology (with its chart), and the results, read live from `results/` and `RESULTS.md`. Then mirror it into `site/` as a static site for GitHub Pages, following the `init-django-static-site` approach (Django as the authoring tool, `wget` to mirror).

## Decisions to make before starting

| Decision | My recommendation |
|---|---|
| Headline question | Reading against querying (Phases 1 and 2 together): the form of the meaning, then whether the LLM should read the data or query it. The others test how far that generalises |
| OpenAlex data | Anonymised structure, so memory can't answer |
| Gemini | Secondary: a one-repeat pilot after the Claude runs, then decide |
| How many questions | 40 per domain, five repeats |

## Order over the next few days

| When | Work | Ends with |
|---|---|---|
| Day 1 | Phase 0: question bank, code grading, length control, statistics, provider split | A base run with confidence intervals that aren't all at the ceiling |
| Day 2 | Phase 1: Markdown generator, axioms and SHACL, the executed condition; Claude runs | The form-of-meaning table, at two sizes |
| Day 3 | Phase 2: the query loop, DuckDB and RDF stores with matching views and rules, path questions; Claude runs at four sizes | Reading against querying, and SQL against SPARQL |
| Day 4 | Phase 3: Haiku and Opus; the Gemini pilot if there's time | The tables across models |
| Days 5 and 6 | Phase 4: the OpenAlex slice, its ontology and questions; runs | The tables for a second domain |
| After | Phase 5: the repo and the post | Something to publish |

If time runs short, Phases 0 to 2 make a complete post on their own, and the second domain can be a follow-up.
