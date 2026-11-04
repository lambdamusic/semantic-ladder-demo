Does the store need to be a graph? With only one or two levels of parent, it can't show a graph's strength. This domain is the 300-issuer data, on the version 2 rules, plus six invented groups four to six levels deep, built so that answering means walking parent and guarantee links:

- in the largest group, a parent link names a **RESEARCH record** of the parent, so the chain goes on from that entity's RATINGS record;
- a RESEARCH record gives a **stale parent** in another group, which the RATINGS record overrules;
- a member is **in Valdoria by its RESEARCH record**, which holds for country, while RATINGS puts it in the Netherlands;
- a note is **guaranteed by another group's top entity**;
- a **QA test record** sits under one group's top, with a rating of its own.

`paths.py` builds it, and the designed entities' IDs go in `anchors.json`, from which `build_questions.py` writes the 13 path questions (Q49 to Q61), with keys computed from the data. Q1 to Q48 are the usual questions, keyed on this data.

The two query conditions that matter most here are `sql+executed`, where DuckDB has an `ancestors` table, and `sparql+axioms`, where the graph holds `lad:ancestor` and `lad:ultimateParent` derived by the SHACL rules. In both, the closure is computed before the model starts. Without it, SQL needs a recursive query and SPARQL needs a property path.

**In this section:** the [data](/domains/credit_paths/data/), the [questions](/domains/credit_paths/questions/), the [ontology](/domains/credit_paths/ontology/), and the [results](/domains/credit_paths/results/).
