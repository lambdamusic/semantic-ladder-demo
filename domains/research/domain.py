"""The research domain: invented research-analytics data shaped like OpenAlex, given to the LLM as CSV, RDF and an ontology."""
import csv
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
ONTO = HERE / "ontology"  # ontology.ttl, ontology.md, axioms.ttl, padding.md
ONTOLOGY = ONTO / "ontology.ttl"
QUESTIONS = HERE / "questions.json"
CSV_FILES = ["institutions.csv", "authors.csv", "sources.csv", "works.csv", "authorships.csv", "citations.csv"]
CONDITIONS = ["csv", "rdf", "rdf+ontology", "csv+ontology", "csv+markdown", "csv+padding", "executed",
              "csv+axioms", "csv+axioms+markdown"]

# The executed condition: the tables execute.py writes, the rules applied and no definitions.
EXECUTED_TABLES = ["works.csv", "people.csv", "credits.csv", "institutions.csv", "institution_units.csv",
                   "sources.csv", "citations.csv"]
EXECUTED_NOTE = (
    "These tables are the data after its rules have been applied. Test records are gone. A preprint is merged "
    "into its published version (record_ids lists the records each work merges). research_output says whether a "
    "work counts as research output. Author records are merged into people (author_ids lists them). credits gives "
    "the one institution credited for each person on each work. institution_units lists every institution each "
    "institution's works count towards, itself included, with how many levels up. citations links merged works, "
    "and only from citing works that count. tier_rank ranks journal tiers, 1 the highest; a delisted source's works "
    "are not research output.")

# The sparql+axioms condition: the store after axioms.ttl's SHACL rules have run.
AXIOMS_NOTE = ("The store holds the data after the rules of its axioms have run, with no definitions alongside. "
               "Besides the data's own properties, it holds what the rules derived: res:samePersonAs links the "
               "author records of one person; res:countsAs gives the work a record counts as (a preprint's published "
               "version, or itself), and the class res:ResearchWork holds the works that count as research output; "
               "res:hasPerson gives each work's distinct people, one author record each; res:creditedInstitution "
               "and res:creditedCountry give the institutions and countries credited on a work, every level up; "
               "res:unitOf, res:countsTowards and res:ultimateParent give the hierarchy; res:cites links the works "
               "of the citations that count; res:tierRank ranks the journal tiers, 1 the highest.")

SYSTEM = (
    "You answer questions about a research-analytics dataset of works, authors, institutions, "
    "sources and citations. Use only the data you are given and what it tells you about its own "
    "meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise."
)

# How the answer names a work, author, institution or source: its record ID, as in the data.
ENTITY_HINT = ("Name works, authors, institutions and sources by their record ID: the work_id, author_id, "
               "institution_id or source_id in the CSV files, or the part of the IRI after res: in the RDF "
               "(W01, A07, I02, S03; not their titles or names).")


def read(path):
    return path.read_text().strip()


def bare_ontology():
    """ontology.ttl with every definition and comment taken out: names, codes and structure only."""
    from rdflib import RDFS, Graph, Namespace
    skos = Namespace("http://www.w3.org/2004/02/skos/core#")
    g = Graph().parse(ONTOLOGY)
    for p in (skos.definition, skos.scopeNote, RDFS.comment):
        g.remove((None, p, None))
    return g.serialize(format="turtle").strip()


def context(condition):
    if condition not in CONDITIONS:  # the credit domain's csv+neutral condition doesn't exist here
        raise ValueError(f"the research domain has no condition {condition!r}; it has {', '.join(CONDITIONS)}")
    if condition == "executed":
        return EXECUTED_NOTE + "\n\n" + "\n\n".join(
            f"### {name}\n```csv\n{read(DATA / 'executed' / name)}\n```" for name in EXECUTED_TABLES)
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
    elif extra.startswith("axioms"):  # the meaning as logic: no prose, the ontology's names and codes plus OWL and SHACL
        parts.append("### ontology.ttl, without its definitions (the vocabulary the data uses)\n"
                     "The codes in the CSV files are the skos:notation values of the concepts below.\n"
                     f"```turtle\n{bare_ontology()}\n```")
        parts.append(f"### axioms.ttl (OWL axioms and SHACL rules over the vocabulary)\n```turtle\n{read(ONTO / 'axioms.ttl')}\n```")
        if extra == "axioms+markdown":
            parts.append(f"### ontology.md (the vocabulary the data uses)\n\n{read(ONTO / 'ontology.md')}")
    elif extra == "markdown":  # the same definitions, generated from ontology.ttl by ontology_to_md.py
        parts.append(f"### ontology.md (the vocabulary the data uses)\n\n{read(ONTO / 'ontology.md')}")
    elif extra == "padding":  # the length control: text on scholarly publishing of the same length, about none of this
        parts.append(f"### background.md\n\n{read(ONTO / 'padding.md')}")
    return "\n\n".join(parts)


def canonical():
    """Record ID -> the entity it stands for: author records with the same ORCID are one person.

    Works, institutions and sources stand for themselves (grade.py falls back to the ID).
    A preprint is deliberately not merged with its published version here: questions that
    list works ask for records, and merging would accept the wrong record of a pair.
    """
    with open(DATA / "authors.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["author_id"]: r["orcid"] or r["author_id"] for r in rows}
