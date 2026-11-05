"""Write a domain's ontology as Markdown: the same labels, codes and definitions, without RDF.

    python src/ontology_to_md.py credit      # domains/credit/ontology.ttl -> domains/credit/ontology.md

Generated rather than written, so the Markdown and the Turtle can't drift apart: the
csv+markdown and csv+ontology conditions differ only in form.
"""
import importlib
import re
import sys
from pathlib import Path

from rdflib import OWL, RDF, RDFS, Graph, Namespace

SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
ROOT = Path(__file__).resolve().parent.parent  # the repo: domains/


def build(name):
    folder = ROOT / "domains" / name
    text = (folder / "ontology.ttl").read_text()
    g = Graph().parse(data=text, format="turtle")
    local = lambda u: str(u).rsplit("/", 1)[-1]
    order = lambda items: sorted(items, key=lambda u: text.find(f":{local(u)} a "))
    columns = {}
    try:  # which CSV column each property names, where the domain has a converter
        conv = importlib.import_module(f"domains.{name}.csv_to_rdf")
        for cols in (conv.ENTITY_COLS, conv.INSTRUMENT_COLS, conv.ACTION_COLS):
            for column, (prop, _) in cols.items():
                columns[prop] = column
    except ImportError:
        pass

    names = {}  # lad:x in a definition -> how the Markdown names it
    for u in set(g.subjects(RDFS.label, None)):
        code = g.value(u, SKOS.notation)
        names[local(u)] = f"{g.value(u, RDFS.label)} ({code})" if code else f"{g.value(u, RDFS.label)}"

    def say(value):
        return re.sub(r"\b[a-z]+:([A-Za-z][\w-]*)", lambda m: names.get(m.group(1), m.group(0)), str(value))

    onto = next(g.subjects(RDF.type, OWL.Ontology))
    lines = [f"# {g.value(onto, RDFS.label)}", "", str(g.value(onto, RDFS.comment)), "", "## Classes", ""]
    for c in order(g.subjects(RDF.type, OWL.Class)):
        lines += [f"### {g.value(c, RDFS.label)}", "", say(g.value(c, SKOS.definition)), ""]
    lines += ["## Properties", ""]
    for p in order([*g.subjects(RDF.type, OWL.ObjectProperty), *g.subjects(RDF.type, OWL.DatatypeProperty)]):
        column = columns.get(local(p))
        head = f"### {g.value(p, RDFS.label)}" + (f" (CSV column `{column}`)" if column else "")
        lines += [head, "", say(g.value(p, SKOS.definition)), ""]
    lines += ["## Codes", "", "The codes as they appear in the data, grouped by list.", ""]
    for s in order(g.subjects(RDF.type, SKOS.ConceptScheme)):
        lines += [f"### {g.value(s, RDFS.label)}", ""]
        for c in order(g.subjects(SKOS.inScheme, s)):
            lines.append(f"- **{g.value(c, SKOS.notation)}**, {g.value(c, SKOS.prefLabel)}: {say(g.value(c, SKOS.definition))}")
        lines.append("")
    out = folder / "ontology.md"
    out.write_text("\n".join(lines))
    print(f"{out.relative_to(ROOT)}: {len(out.read_text()):,} characters (ontology.ttl: {len(text):,})")


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT))
    build(sys.argv[1] if len(sys.argv) > 1 else "credit")
