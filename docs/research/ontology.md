The same approach as the credit domain: classes, a property for each CSV column, and every code as a SKOS concept with a plain-English definition. The local rules are stated there and nowhere else. Each file links to its source on GitHub:

- **[`ontology.ttl`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/domains/research/ontology/ontology.ttl)**: the definitions, as SKOS in Turtle.
- **[`ontology.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/domains/research/ontology/ontology.md)**: the same definitions as Markdown, generated from the Turtle by [`ontology_to_md.py`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/src/ontology_to_md.py). This is what `csv+markdown` gets, and it's shown below.
- **[`padding.md`](https://github.com/lambdamusic/semantic-ladder-demo/blob/main/domains/research/ontology/padding.md)**: the decoy glossary for `csv+padding`. It's on the same subject, scholarly publishing, and as long as `ontology.md`, but defines none of the terms the questions depend on.

There's no `axioms.ttl` for this domain yet, so it has no `csv+axioms` or `sparql+axioms` condition.
