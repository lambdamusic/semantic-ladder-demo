"""Turn the six CSV files into RDF (data/facts.ttl), using the ontology's terms.

A straight conversion, as in the credit domain: one resource per row, one property per
column, and every code (ART, LAB, K2, STG...) becomes the IRI of the matching concept in
ontology.ttl. Each resource gets a short rdfs:label built only from its own row, leaving
codes untranslated. Nothing is inferred or merged: the three records of Mara Ellison stay
three resources, a preprint and its published version stay two works, a lab is not rolled
up into its university. The meaning arrives only when the ontology is added alongside.

Rows of authorships.csv and citations.csv have no ID of their own, so their resources are
named from their columns (AS-W01-A01-1 is W01's authorship by A01, first affiliation;
C-W12-W03 is W12 citing W03).

    python domains/research/csv_to_rdf.py
"""

import csv
from pathlib import Path

from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace

HERE = Path(__file__).parent
DATA = HERE / "data"
RES = Namespace("https://example.org/research/")

# column -> (property, how to turn the cell into an RDF term)
INSTITUTION_COLS = {
    "name": ("name", "literal"),
    "ror": ("ror", "literal"),
    "country": ("country", "literal"),
    "type": ("institutionType", "code:itype"),
    "parent_id": ("parent", "ref"),
}
AUTHOR_COLS = {
    "name": ("name", "literal"),
    "orcid": ("orcid", "literal"),
}
SOURCE_COLS = {
    "name": ("name", "literal"),
    "issn": ("issn", "literal"),
    "type": ("sourceType", "code:stype"),
    "tier": ("tier", "code:tier"),
}
WORK_COLS = {
    "title": ("title", "literal"),
    "year": ("year", "year"),
    "type": ("workType", "code:wtype"),
    "source_id": ("source", "ref"),
    "doi": ("doi", "literal"),
    "version_of": ("versionOf", "ref"),
    "is_retracted": ("retracted", "boolean"),
    "record_source": ("recordSource", "code:origin"),
}
AUTHORSHIP_COLS = {
    "work_id": ("work", "ref"),
    "author_id": ("author", "ref"),
    "author_position": ("authorPosition", "integer"),
    "institution_id": ("institution", "ref"),
    "affil_seq": ("affiliationSeq", "integer"),
}
CITATION_COLS = {
    "citing_work_id": ("citingWork", "ref"),
    "cited_work_id": ("citedWork", "ref"),
}

# ontology_to_md.py reads these three names (the credit domain's tables) to name each
# property's CSV column. The six research tables are grouped onto them so it works
# unchanged; the groups are chosen so no column name occurs twice in one group with
# different properties (three tables have a `type` column).
ENTITY_COLS = {**INSTITUTION_COLS, **AUTHOR_COLS, **CITATION_COLS}
INSTRUMENT_COLS = {**SOURCE_COLS, **AUTHORSHIP_COLS}
ACTION_COLS = WORK_COLS


def term(kind, value):
    if kind == "literal":
        return Literal(value)
    if kind == "year":
        return Literal(value, datatype=XSD.gYear)
    if kind == "integer":
        return Literal(int(value))
    if kind == "boolean":
        return Literal(value == "true")
    if kind == "ref":
        return RES[value]
    prefix = kind.split(":", 1)[1]
    return RES[f"{prefix}-{value}"]


TABLES = [
    # file, how a row is named, class, columns, label
    ("institutions.csv", lambda r: r["institution_id"], RES.Institution, INSTITUTION_COLS, lambda r: r["name"]),
    ("authors.csv", lambda r: r["author_id"], RES.Author, AUTHOR_COLS, lambda r: r["name"]),
    ("sources.csv", lambda r: r["source_id"], RES.Source, SOURCE_COLS, lambda r: r["name"]),
    ("works.csv", lambda r: r["work_id"], RES.Work, WORK_COLS, lambda r: r["title"]),
    ("authorships.csv", lambda r: f"AS-{r['work_id']}-{r['author_id']}-{r['affil_seq']}", RES.Authorship,
     AUTHORSHIP_COLS, lambda r: f"{r['work_id']} {r['author_id']} {r['institution_id']}"),
    ("citations.csv", lambda r: f"C-{r['citing_work_id']}-{r['cited_work_id']}", RES.Citation, CITATION_COLS,
     lambda r: f"{r['citing_work_id']} cites {r['cited_work_id']}"),
]


def build():
    g = Graph()
    g.bind("res", RES)
    for filename, name, cls, cols, label in TABLES:
        with open(DATA / filename, newline="") as f:
            for row in csv.DictReader(f):
                s = RES[name(row)]
                g.add((s, RDF.type, cls))
                g.add((s, RDFS.label, Literal(label(row))))
                for col, (prop, kind) in cols.items():
                    if row[col]:
                        g.add((s, RES[prop], term(kind, row[col])))
    return g


if __name__ == "__main__":
    g = build()
    out = DATA / "facts.ttl"
    g.serialize(out, format="turtle")
    print(f"{len(g)} triples -> {out.relative_to(HERE.parent)}")
