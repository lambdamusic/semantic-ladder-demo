The meaning comes in three forms, so that the experiment can tell the form apart from the content:

- **`ontology.ttl`**: three classes, the properties each CSV column names, and every code as a SKOS concept, with its `skos:notation` as it appears in the data. The meaning is in plain-English `skos:definition`s.
- **`ontology.md`**: the same definitions as Markdown, generated from the Turtle by `ontology_to_md.py` so that the two never drift. This is what the `csv+markdown` and query conditions get.
- **`axioms.ttl`**: the meaning as logic, with no prose. OWL keys, functional properties, disjoint classes and code lists as classes, plus SHACL-AF rules that derive what the definitions say: identity by LEI, domicile, parent chains entity by entity, rating periods, ratings in force, credit risk, and a constraint that catches a rating above its ceiling. The `csv+axioms` condition gets these plus the ontology with its definitions removed. `sparql+axioms` queries the data after the rules have run.

`check_axioms.py` runs the rules over the data and checks their output against the keys, so the logic is tested as well as read.
