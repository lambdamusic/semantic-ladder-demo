"""The credit domain: invented ratings data, given to the LLM as CSV, RDF and an ontology."""
import csv
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
ONTO = HERE / "ontology"  # ontology.ttl, ontology.md, axioms.ttl, padding.md
ONTOLOGY = ONTO / "ontology.ttl"
QUESTIONS = HERE / "questions.json"
CSV_FILES = ["entities.csv", "instruments.csv", "rating_actions.csv"]

SYSTEM = (
    "You answer questions about a credit-ratings dataset. Use only the data you are given "
    "and what it tells you about its own meaning. If a question is ambiguous, or the data "
    "cannot settle it, say so. Be concise."
)

# How the answer names an entity: its record ID, as in the data.
ENTITY_HINT = ("Name entities by their record ID: the entity_id in the CSV files, or the part of "
               "the IRI after lad: in the RDF (E01, not Kestrel Energy plc).")


def read(path):
    return path.read_text().strip()


EXECUTED_TABLES = ["entities.csv", "instruments.csv", "ratings.csv", "ceilings.csv", "ancestors.csv"]
EXECUTED_NOTE = ("These tables are the data after its rules have been applied: duplicate records merged into "
                 "one entity (record_ids lists the records each entity merges), and each rating with the "
                 "period it held. An empty valid_to means the rating was still in force on 1 October 2026. "
                 "ancestors lists every entity above each entity in its chain of parents, with how many levels up.")

AXIOMS_NOTE = ("The store holds the data after the rules of its axioms have run, with no definitions alongside. "
               "Besides the data's own properties, it holds what the rules derived: lad:sameEntityAs links the "
               "records of one entity; lad:domicile is the country that holds for an entity; lad:parentEntity, "
               "lad:ancestor and lad:ultimateParent give ownership entity by entity (an entity with no parent is "
               "its own ultimate parent); lad:validTo is when a rating stopped holding, and the class "
               "lad:RatingInForce holds the actions whose rating was in force on 1 October 2026; lad:creditRiskOf "
               "and lad:localCurrency describe instruments.")


SLANTED = "The foreign-currency (FC) one is the headline rating; there may also be a local-currency (LC) one."
NEUTRAL = "An entity may have a foreign-currency (FC) one, a local-currency (LC) one, or both."


def neutral_ontology():
    text = read(ONTOLOGY)
    assert text.count(SLANTED) == 1
    return text.replace(SLANTED, NEUTRAL)


def bare_ontology():
    """ontology.ttl with every definition and comment taken out: names, codes and structure only."""
    from rdflib import RDFS, Graph, Namespace
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")
    g = Graph().parse(ONTOLOGY)
    for p in (skos.definition, skos.scopeNote, RDFS.comment):
        g.remove((None, p, None))
    return g.serialize(format="turtle").strip()


def context(condition):
    if condition == "executed":  # written by execute.py: the rules applied, no definitions
        tables = EXECUTED_TABLES
        return EXECUTED_NOTE + "\n\n" + "\n\n".join(
            f"### {name}\n```csv\n{read(DATA / 'executed' / name)}\n```" for name in tables)
    parts = []
    if condition.startswith("csv"):
        for name in CSV_FILES:
            parts.append(f"### {name}\n```csv\n{read(DATA / name)}\n```")
    if condition.startswith("rdf"):
        parts.append(f"### facts.ttl (RDF, Turtle)\n```turtle\n{read(DATA / 'facts.ttl')}\n```")
    extra = condition.partition("+")[2]
    if extra == "ontology":
        note = ("The codes in the CSV files are the skos:notation values of the concepts below."
                if condition.startswith("csv") else "")
        parts.append(f"### ontology.ttl (the vocabulary the data uses){chr(10) + note if note else ''}\n"
                     f"```turtle\n{read(ONTOLOGY)}\n```")
    elif extra == "neutral":  # the ontology with its one slanted sentence made neutral: a test of wording
        parts.append(f"### ontology.ttl (the vocabulary the data uses)\n"
                     "The codes in the CSV files are the skos:notation values of the concepts below.\n"
                     f"```turtle\n{neutral_ontology()}\n```")
    elif extra.startswith("axioms"):  # the meaning as logic: no prose, the ontology's names and codes plus OWL and SHACL
        parts.append("### ontology.ttl, without its definitions (the vocabulary the data uses)\n"
                     "The codes in the CSV files are the skos:notation values of the concepts below.\n"
                     f"```turtle\n{bare_ontology()}\n```")
        parts.append(f"### axioms.ttl (OWL axioms and SHACL rules over the vocabulary)\n```turtle\n{read(ONTO / 'axioms.ttl')}\n```")
        if extra == "axioms+markdown":
            parts.append(f"### ontology.md (the vocabulary the data uses)\n\n{read(ONTO / 'ontology.md')}")
        elif extra != "axioms":
            raise ValueError(condition)
    elif extra == "markdown":  # the same definitions, generated from ontology.ttl by ontology_to_md.py
        parts.append(f"### ontology.md (the vocabulary the data uses)\n\n{read(ONTO / 'ontology.md')}")
    elif extra == "padding":  # the length control: finance text of the same length, about none of this
        parts.append(f"### background.md\n\n{read(ONTO / 'padding.md')}")
    elif extra:
        raise ValueError(condition)
    return "\n\n".join(parts)


def canonical():
    """Record ID -> the entity it stands for: records with the same LEI are one entity."""
    with open(DATA / "entities.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["entity_id"]: r["lei"] or r["entity_id"] for r in rows}
