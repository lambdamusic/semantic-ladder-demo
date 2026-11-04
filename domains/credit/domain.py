"""The credit domain: invented ratings data, given to the LLM as CSV, RDF and an ontology."""
import csv
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
ONTOLOGY = HERE / "ontology.ttl"
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


def context(condition):
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
    elif extra == "markdown":  # the same definitions, generated from ontology.ttl by ontology_to_md.py
        parts.append(f"### ontology.md (the vocabulary the data uses)\n\n{read(HERE / 'ontology.md')}")
    elif extra == "padding":  # the length control: finance text of the same length, about none of this
        parts.append(f"### background.md\n\n{read(HERE / 'padding.md')}")
    elif extra:
        raise ValueError(condition)
    return "\n\n".join(parts)


def canonical():
    """Record ID -> the entity it stands for: records with the same LEI are one entity."""
    with open(DATA / "entities.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["entity_id"]: r["lei"] or r["entity_id"] for r in rows}
