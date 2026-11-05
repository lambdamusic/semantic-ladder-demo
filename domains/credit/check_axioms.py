"""Run axioms.ttl's SHACL rules over the data and print what they derive, to check them against the keys.

    python domains/credit/check_axioms.py domains/credit
"""
import sys
from rdflib import Graph, Namespace, RDF
from pyshacl import validate
folder = sys.argv[1]
LAD = Namespace("https://example.org/ladder/")
data = Graph().parse(f"{folder}/data/facts.ttl").parse(f"{folder}/ontology/ontology.ttl").parse(f"{folder}/ontology/axioms.ttl")
shapes = Graph().parse(f"{folder}/ontology/axioms.ttl")
conforms, results, text = validate(data, shacl_graph=shapes, advanced=True, inplace=True, allow_infos=True)
print("conforms:", conforms); print(text[:1500])
q = lambda s: list(data.query("PREFIX lad: <https://example.org/ladder/> " + s))
print("sameEntityAs:", sorted((str(a).rsplit('/',1)[1], str(b).rsplit('/',1)[1]) for a, b in q("SELECT ?a ?b { ?a lad:sameEntityAs ?b }")))
print("domicile E17:", q("SELECT ?c { lad:E17 lad:domicile ?c }"))
print("Marlow periods:", sorted((str(a).rsplit('/',1)[1], str(t)) for a, t in q("SELECT ?a ?t { ?a lad:ratedThing lad:E14 ; lad:validTo ?t }")))
issuers = {str(e).rsplit('/',1)[1] for (e,) in q("SELECT DISTINCT ?e { ?a a lad:RatingInForce ; lad:ratingType lad:type-LTIDR ; lad:ratedThing ?e }")}
print("issuers with a rating in force:", len(issuers), sorted(issuers))
print("I05 risk, I07 local:", q("SELECT ?w { lad:I05 lad:creditRiskOf ?w }"), q("SELECT ?l { lad:I07 lad:localCurrency ?l }"))
print("domicile E10:", q("SELECT ?c { lad:E10 lad:domicile ?c }"))
print("ultimate parent of E11:", q("SELECT ?u { lad:E11 lad:ultimateParent ?u }"), "| ancestors:", q("SELECT ?a { lad:E11 lad:ancestor ?a }"))
legal = {str(l) for (l,) in q("SELECT ?l { ?e a lad:Entity ; lad:lei ?l FILTER NOT EXISTS { ?e lad:sourceSystem 'QA' } }")}
print("distinct legal entities with an LEI (sovereigns have none):", len(legal))
print("in force on I08 (EX):", q("ASK { ?a lad:ratedThing lad:I08 ; a lad:RatingInForce }"))
# the ceiling constraint must catch a breach: lift Valdoria Telecom's FC rating above BB and validate again
bad = Graph().parse(f"{folder}/data/facts.ttl").parse(f"{folder}/ontology/ontology.ttl").parse(f"{folder}/ontology/axioms.ttl")
from rdflib import Literal
bad.set((LAD.A14, LAD.rating, Literal("BBB")))
c2, _, t2 = validate(bad, shacl_graph=shapes, advanced=True, inplace=True, allow_infos=True)
print("with a breach, conforms:", c2, "|", [l for l in t2.splitlines() if "Message" in l][:2])
