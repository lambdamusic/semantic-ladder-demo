"""Turn the three CSV files into RDF (data/facts.ttl), using the ontology's terms.

A straight conversion, on purpose: one resource per row, one property per column, and
every code (LTIDR, DG, NEG...) becomes the IRI of the matching concept in ontology.ttl.
Each resource also gets a short rdfs:label, built only from its own row and leaving codes
untranslated, so the file is easier to read without adding any meaning. Nothing is inferred or merged: the two Northwind records stay two resources. So the RDF
holds the same information as the CSV, in a different shape; the meaning arrives only
when the ontology is added alongside it.

    python domains/credit/csv_to_rdf.py
"""

import csv
from pathlib import Path

from rdflib import RDF, RDFS, XSD, Graph, Literal, Namespace

HERE = Path(__file__).parent
DATA = HERE / "data"
LAD = Namespace("https://example.org/ladder/")

# column -> (property, how to turn the cell into an RDF term)
ENTITY_COLS = {
    "name": ("name", "literal"),
    "lei": ("lei", "literal"),
    "country": ("country", "literal"),
    "entity_type": ("entityType", "code:etype"),
    "parent_id": ("parent", "ref"),
    "source_system": ("sourceSystem", "literal"),
}
INSTRUMENT_COLS = {
    "description": ("description", "literal"),
    "issuer_id": ("issuer", "ref"),
    "guarantor_id": ("guarantor", "ref"),
    "seniority": ("seniority", "code:seniority"),
    "currency": ("currency", "literal"),
    "maturity": ("maturity", "date"),
}
ACTION_COLS = {
    "date": ("date", "date"),
    "rated_id": ("ratedThing", "ref"),
    "rating_type": ("ratingType", "code:type"),
    "ccy_basis": ("ccyBasis", "code:basis"),
    "action": ("action", "code:action"),
    "rating": ("rating", "literal"),
    "outlook": ("outlook", "code:outlook"),
    "watch": ("watch", "code:watch"),
    "comment": ("comment", "literal"),
}


def term(kind, value):
    if kind == "literal":
        return Literal(value)
    if kind == "date":
        return Literal(value, datatype=XSD.date)
    if kind == "ref":
        return LAD[value]
    prefix = kind.split(":", 1)[1]
    return LAD[f"{prefix}-{value}"]


def entity_label(row):
    return row["name"]


def instrument_label(row):
    return row["description"].replace(" notes due ", " ")


def action_label(row):
    return f"{row['rated_id']} {row['action']} {row['rating']} {row['date']}"


def load(g, filename, id_col, cls, cols, label):
    with open(DATA / filename, newline="") as f:
        for row in csv.DictReader(f):
            s = LAD[row[id_col]]
            g.add((s, RDF.type, cls))
            g.add((s, RDFS.label, Literal(label(row))))
            for col, (prop, kind) in cols.items():
                if row[col]:
                    g.add((s, LAD[prop], term(kind, row[col])))


def build():
    g = Graph()
    g.bind("lad", LAD)
    load(g, "entities.csv", "entity_id", LAD.Entity, ENTITY_COLS, entity_label)
    load(g, "instruments.csv", "instrument_id", LAD.Instrument, INSTRUMENT_COLS, instrument_label)
    load(g, "rating_actions.csv", "action_id", LAD.RatingAction, ACTION_COLS, action_label)
    return g


if __name__ == "__main__":
    g = build()
    out = DATA / "facts.ttl"
    g.serialize(out, format="turtle")
    print(f"{len(g)} triples -> {out.relative_to(HERE.parent)}")
