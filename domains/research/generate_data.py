"""Write the research domain's invented data: six CSV files shaped like OpenAlex, but small.

    python domains/research/generate_data.py      # -> domains/research/data/*.csv

ALL OF IT IS INVENTED: the works, authors, institutions, journals, ORCIDs, RORs, ISSNs
and DOIs. None stands for a real one. The DOIs use the prefix 10.55555, and the ORCIDs
are not checksummed.

Two parts. The core (W01-W92) is written out by hand below, because each of the
experiment's traps (one person under several author records, a lab under a university
under a system, a preprint and its published version, a retracted work, test records,
affiliated institutes...) is built from particular works and citations. The background
(W101 onwards, plus the citers W60-W67) is generated with a fixed seed, by authors at
four other institutions in journals of their own, so it adds noise to the files without
touching any key: background works cite only other background works, except the
citations listed in DESIGNED_CITES.
"""
import csv
import random
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
SEED = 2026

# institution_id, name, country, type, parent_id
INSTITUTIONS = [
    ("I01", "Albury University System", "GB", "SYS", ""),
    ("I02", "University of Albury", "GB", "UNI", "I01"),
    ("I03", "Albury Centre for Marine Robotics", "GB", "LAB", "I02"),
    ("I04", "Tessel Laboratory for Ocean Sensing", "GB", "LAB", "I03"),
    ("I05", "Albury Metropolitan University", "GB", "UNI", "I01"),
    ("I06", "Halloran Institute for Coastal Studies", "GB", "AFF", "I02"),
    ("I07", "Kesting University", "DE", "UNI", ""),
    ("I08", "Kesting Institute of Hydrodynamics", "DE", "LAB", "I07"),
    ("I09", "Rostval Technical University", "NL", "UNI", ""),
    ("I10", "Marrow Instruments BV", "NL", "CO", ""),
    ("I11", "Brevin Ocean Agency", "FR", "GOV", ""),
    ("I12", "Université de Lorvain", "FR", "UNI", ""),
    ("I13", "Dunmore College", "GB", "UNI", ""),
    ("I14", "Oskel Polytechnic", "NL", "UNI", ""),
    # background
    ("I15", "Carrow State University", "US", "UNI", ""),
    ("I16", "Hoshimine Institute of Technology", "JP", "UNI", ""),
    ("I17", "Université de Mallois", "CA", "UNI", ""),
    ("I18", "Universidad de Ventolera", "ES", "UNI", ""),
]

# author_id, name, has ORCID (people with the same ORCID key share one)
AUTHORS = [
    ("A01", "Mara Ellison", "mara"),
    ("A02", "M. Ellison", "mara"),
    ("A03", "Ellison, Mara J.", "mara"),
    ("A04", "M. Ellison", "marcus"),          # Marcus Ellison, Kesting: a different person
    ("A05", "Jonas Brandt", "jonas-gb"),
    ("A06", "Jonas Brandt", "jonas-fr"),      # a different Jonas Brandt, at Lorvain
    ("A07", "Priya Ramanathan", "priya"),
    ("A08", "Tomasz Wierzba", "tomasz"),
    ("A09", "Lena Vossberg", "lena"),
    ("A10", "Dirk Hallmann", "dirk"),
    ("A11", "Sofie de Raat", "sofie"),
    ("A12", "Pieter Maas", "pieter"),
    ("A13", "Claire Fontanet", "claire"),
    ("A14", "Hugo Marchetti", "hugo"),
    ("A15", "Aisha Okonjo", "aisha"),
    ("A16", "Rhys Calloway", ""),             # no ORCID
    ("A17", "Ingrid Solberg", "ingrid"),
    ("A18", "Bram Kuipers", "bram"),
    ("A19", "Femke Hoogeveen", "femke"),
    ("A20", "Joost Verhaar", "joost"),
    ("A21", "Petra Lindqvist", "petra"),      # appears only on test (STG) records
    ("A22", "Niamh Corrigan", "niamh"),
]

# source_id, name, type, tier
SOURCES = [
    ("S01", "Journal of Marine Autonomy", "JOU", "K3"),
    ("S02", "Ocean Sensing Letters", "JOU", "K2"),
    ("S03", "Coastal Engineering Review", "JOU", "K1"),
    ("S04", "Global Marine Science Reports", "JOU", "K0"),
    ("S05", "OceanArXiv", "REP", ""),
    ("S06", "Proceedings of the Hydrodynamics Forum", "JOU", "K2"),
    # background
    ("S07", "Journal of Estuarine Dynamics", "JOU", "K2"),
    ("S08", "Hydrology Notes", "JOU", "K1"),
]

# work_id, title, year, type, source, version_of, retracted, record_source,
# authorships as [(author, [institutions in the order listed])]
CORE = [
    # Mara Ellison (A01, A02, A03: one ORCID) and Priya Ramanathan
    ("W01", "Adaptive path planning for underwater gliders", 2021, "ART", "S01", "", False, "FEED",
     [("A01", ["I02"]), ("A07", ["I03"])]),
    ("W02", "Drift-aware mapping with low-cost sonar", 2022, "PPR", "S05", "W03", False, "FEED",
     [("A02", ["I02"]), ("A07", ["I03"])]),
    ("W03", "Drift-aware mapping with low-cost sonar", 2023, "ART", "S02", "", False, "FEED",
     [("A03", ["I02"]), ("A07", ["I03"])]),
    ("W04", "Editorial: a new decade of marine autonomy", 2023, "EDT", "S01", "", False, "FEED",
     [("A01", ["I02"])]),
    ("W05", "Erratum: Drift-aware mapping with low-cost sonar", 2024, "ERR", "S02", "", False, "FEED",
     [("A01", ["I02"]), ("A07", ["I03"])]),
    ("W06", "Shoreline change detection from glider transects", 2024, "ART", "S03", "", False, "FEED",
     [("A01", ["I02"]), ("A15", ["I13"])]),
    ("W07", "Low-cost sonar arrays for coastal monitoring", 2020, "ART", "S04", "", False, "FEED",
     [("A02", ["I02"])]),
    ("W08", "Turbulent wake modelling behind tidal turbines", 2025, "ART", "S01", "", False, "FEED",
     [("A04", ["I07"])]),
    ("W09", "Issue information", 2023, "PTX", "S01", "", False, "FEED", []),
    ("W10", "Front matter", 2024, "PTX", "S02", "", False, "FEED", []),
    ("W12", "Sonar mosaics from glider fleets", 2024, "ART", "S02", "", False, "CRIS",
     [("A01", ["I02"]), ("A16", ["I05"])]),
    ("W13", "Fleet coordination for survey gliders", 2024, "ART", "S01", "", False, "FEED",
     [("A07", ["I03"])]),
    ("W14", "Harbour mapping with autonomous surface vessels", 2025, "ART", "S03", "", False, "FEED",
     [("A05", ["I05"])]),
    ("W15", "Low-cost sonar: a review", 2025, "REV", "S02", "", False, "FEED",
     [("A15", ["I13"])]),
    ("W16", "Sonar-based wake detection", 2025, "ART", "S02", "", False, "FEED",
     [("A04", ["I07"])]),
    ("W17", "Acoustic positioning near the shore", 2024, "SUP", "S06", "", False, "FEED",
     [("A13", ["I11"])]),
    ("W18", "Comparing sonar odometry methods", 2022, "PPR", "S05", "", False, "FEED",
     [("A11", ["I09"])]),
    ("W19", "Glider-borne turbidity sensing", 2025, "ART", "S02", "", False, "CRIS",
     [("A02", ["I02"])]),

    # Kesting University and its institute; who it is co-authored with in 2024
    ("W20", "Bed shear stress under breaking waves", 2024, "ART", "S01", "", False, "FEED",
     [("A09", ["I07"]), ("A13", ["I11"])]),
    ("W21", "A field campaign on tidal mixing", 2024, "ART", "S02", "", False, "FEED",
     [("A10", ["I08"]), ("A09", ["I07"]), ("A11", ["I09"]), ("A12", ["I10"])]),
    ("W22", "Turbulence closures for coastal models: a review", 2024, "REV", "S03", "", False, "FEED",
     [("A09", ["I07"])]),
    ("W23", "Anomalous dissipation in estuarine plumes", 2023, "ART", "S02", "", True, "FEED",
     [("A09", ["I07"])]),
    ("W24", "Vortex shedding in shallow channels", 2025, "SUP", "S06", "", False, "FEED",
     [("A10", ["I08"])]),
    ("W27", "Sensor fusion for moored buoys", 2024, "ART", "S03", "", False, "FEED",
     [("A18", ["I09"]), ("A13", ["I11"]), ("A14", ["I12"]), ("A17", ["I14"])]),
    ("W28", "Calibration drift in conductivity sensors", 2024, "ART", "S02", "", False, "FEED",
     [("A19", ["I09"]), ("A15", ["I13"]), ("A16", ["I05"]), ("A06", ["I12"])]),
    ("W29", "Open hardware for ocean observation: a review", 2024, "REV", "S01", "", False, "FEED",
     [("A20", ["I09"]), ("A16", ["I05"]), ("A15", ["I13"]), ("A13", ["I11"])]),

    # Citation windows: an older and a newer work
    ("W30", "Tidal stream resource maps for the Dunmore coast", 2019, "ART", "S03", "", False, "FEED",
     [("A15", ["I13"])]),
    ("W31", "Machine-learned tidal forecasts", 2023, "ART", "S01", "", False, "FEED",
     [("A17", ["I14"])]),
    ("W42", "Machine-learned tidal forecasts", 2023, "PPR", "S05", "W31", False, "FEED",
     [("A17", ["I14"])]),

    # Who cites Kesting
    ("W32", "Wave-current interaction over sandbars", 2025, "ART", "S01", "", False, "FEED",
     [("A11", ["I09"]), ("A18", ["I09"]), ("A19", ["I09"]), ("A20", ["I09"])]),
    ("W33", "Mixing efficiency in stratified tidal flows", 2025, "ART", "S02", "", False, "FEED",
     [("A14", ["I12"])]),
    ("W34", "Evaluating turbulence closures against flume data", 2025, "ART", "S03", "", False, "FEED",
     [("A06", ["I12"])]),
    ("W35", "Sediment resuspension by storms: a review", 2025, "REV", "S02", "", False, "FEED",
     [("A14", ["I12"])]),
    ("W36", "Shear and mixing in a macrotidal estuary", 2025, "ART", "S03", "", False, "FEED",
     [("A13", ["I11"])]),

    # The two Jonas Brandts
    ("W37", "Port traffic and seabed disturbance", 2022, "ART", "S03", "", False, "FEED",
     [("A05", ["I05"])]),
    ("W38", "Seagrass mapping from aerial imagery", 2023, "ART", "S02", "", False, "FEED",
     [("A06", ["I12"])]),
    ("W39", "Replicating dissipation estimates in plumes", 2024, "ART", "S03", "", False, "FEED",
     [("A17", ["I14"])]),

    # Two citation hops from W01
    ("W40", "Energy budgets for long-range gliders", 2022, "ART", "S02", "", False, "FEED",
     [("A11", ["I09"])]),
    ("W41", "Path planning under uncertain currents", 2023, "ART", "S03", "", False, "FEED",
     [("A14", ["I12"])]),
    ("W50", "Battery ageing in autonomous platforms", 2024, "ART", "S03", "", False, "FEED",
     [("A17", ["I14"])]),
    ("W51", "Benchmarks for marine path planners", 2024, "ART", "S02", "", False, "FEED",
     [("A12", ["I10"])]),
    ("W52", "Route optimisation for ocean drones", 2025, "ART", "S01", "", False, "FEED",
     [("A13", ["I11"])]),

    # Tomasz Wierzba: several affiliations; the Halloran Institute
    ("W70", "Optical backscatter in turbid estuaries", 2023, "ART", "S02", "", False, "FEED",
     [("A08", ["I04", "I06"])]),
    ("W71", "Low-power optical sensors for gliders", 2024, "ART", "S01", "", False, "FEED",
     [("A08", ["I06", "I04"])]),
    ("W72", "Integrating optical sensors on survey gliders", 2024, "ART", "S03", "", False, "FEED",
     [("A08", ["I04"]), ("A07", ["I03"])]),
    ("W73", "Saltmarsh retreat on the Halloran shore", 2022, "ART", "S02", "", False, "CRIS",
     [("A08", ["I06"])]),
    ("W74", "Coastal squeeze and managed realignment: a review", 2023, "REV", "S01", "", False, "FEED",
     [("A22", ["I06"])]),
    ("W75", "Rip currents at tourist beaches", 2023, "ART", "S04", "", False, "FEED",
     [("A15", ["I13"])]),
    ("W76", "Foreword to the Forum proceedings", 2025, "EDT", "S06", "", False, "FEED", []),

    # Test records loaded from staging
    ("W90", "Sediment transport in tidal inlets", 2025, "ART", "S02", "", False, "STG",
     [("A21", ["I07"])]),
    ("W91", "Closure models for wave boundary layers", 2025, "ART", "S01", "", False, "STG",
     [("A21", ["I07"])]),
    ("W92", "Coastal turbulence: a review", 2025, "REV", "S03", "", False, "STG",
     [("A21", ["I07"])]),
]

CORE_CITES = [
    # Mara's sonar paper, both versions
    ("W12", "W03"), ("W13", "W03"), ("W14", "W03"), ("W15", "W03"), ("W15", "W02"),
    ("W16", "W03"), ("W17", "W03"), ("W18", "W02"),
    # Kesting's works
    ("W32", "W20"), ("W35", "W20"), ("W36", "W20"), ("W33", "W21"), ("W36", "W21"),
    ("W34", "W22"), ("W90", "W22"), ("W91", "W22"), ("W92", "W22"), ("W39", "W23"),
    # two hops from W01
    ("W40", "W01"), ("W41", "W01"), ("W50", "W40"), ("W51", "W40"), ("W51", "W41"),
    ("W52", "W41"), ("W90", "W41"),
]

# Background citers of the citation-window works, by background authors: work_id, year, cites
DESIGNED_CITES = [
    ("W60", 2020, ["W30"]), ("W61", 2022, ["W30"]), ("W62", 2023, ["W30", "W31"]),
    ("W63", 2024, ["W30"]), ("W64", 2025, ["W30"]), ("W65", 2024, ["W31"]),
    ("W66", 2025, ["W31"]), ("W67", 2023, ["W42"]),
]

FIRST = ["Ana", "Ben", "Chiara", "Daichi", "Elif", "Felipe", "Grace", "Haruto", "Ines", "Julien",
         "Kai", "Lucia", "Mateo", "Noor", "Oscar", "Paula"]
LAST = ["Aranda", "Beaulieu", "Carver", "Dorsey", "Esposito", "Fujimura", "Galvez", "Hartwell",
        "Ishida", "Jaramillo", "Kincaid", "Lefebvre", "Morrow", "Nakagawa", "Olmedo", "Pruitt"]
TOPICS = ["wave runup", "estuarine salinity", "tidal asymmetry", "sediment flux", "storm surge",
          "dune erosion", "river plumes", "harbour seiches", "coastal upwelling", "beach profiles",
          "internal waves", "marsh accretion"]
FORMS = ["Observations of {}", "A model of {}", "Seasonal variability in {}", "Remote sensing of {}",
         "Uncertainty in {} estimates", "Long-term trends in {}"]


def orcid(rng):
    """An ORCID-shaped identifier, invented: 0000-000d-dddd-dddd, no valid checksum."""
    d = "".join(rng.choice("0123456789") for _ in range(9))
    return f"0000-000{d[0]}-{d[1:5]}-{d[5:9]}"


def build():
    rng = random.Random(SEED)
    letters = "abcdefghjkmnpqrstvwxyz0123456789"

    institutions = [dict(institution_id=i, name=n, ror="0" + "".join(rng.choice(letters) for _ in range(6))
                         + f"{rng.randint(10, 99)}", country=c, type=t, parent_id=p)
                    for i, n, c, t, p in INSTITUTIONS]

    people = {}
    authors = []
    for a, name, key in AUTHORS:
        if key and key not in people:
            people[key] = orcid(rng)
        authors.append(dict(author_id=a, name=name, orcid=people.get(key, "")))
    background_authors = []
    for n in range(16):
        a = f"A{30 + n}"
        authors.append(dict(author_id=a, name=f"{FIRST[n]} {LAST[(n * 5) % 16]}", orcid=orcid(rng)))
        background_authors.append((a, ["I15", "I16", "I17", "I18"][n % 4]))

    sources = [dict(source_id=s, name=n, issn=f"{rng.randint(1000, 9999)}-{rng.randint(100, 999)}{rng.choice('0123456789X')}"
                    if t == "JOU" else "", type=t, tier=tier) for s, n, t, tier in SOURCES]

    works, authorships, cites = [], [], []

    def add(wid, title, year, wtype, source, version_of, retracted, origin, byline):
        works.append(dict(work_id=wid, title=title, year=year, type=wtype, source_id=source,
                          doi=f"10.55555/{source.lower()}.{year}.{rng.randint(1000, 9999)}",
                          version_of=version_of, is_retracted="true" if retracted else "false",
                          record_source=origin))
        for pos, (author, insts) in enumerate(byline, 1):
            for seq, inst in enumerate(insts, 1):
                authorships.append(dict(work_id=wid, author_id=author, author_position=pos,
                                        institution_id=inst, affil_seq=seq))

    for w in CORE:
        add(*w)
    cites += CORE_CITES

    def background_byline():
        team = rng.sample(background_authors, rng.choice([1, 1, 2, 2, 3]))
        return [(a, [inst]) for a, inst in team]

    pool = []  # background works: they cite only each other
    for wid, year, targets in DESIGNED_CITES:
        topic = rng.choice(TOPICS)
        add(wid, rng.choice(FORMS).format(topic).capitalize(), year, "ART", rng.choice(["S07", "S08"]),
            "", False, "FEED", background_byline())
        cites += [(wid, t) for t in targets]
        pool.append((wid, year))
    for n in range(25):
        wid, year = f"W{101 + n}", rng.randint(2019, 2025)
        wtype = rng.choices(["ART", "REV", "EDT"], [8, 1, 1])[0]
        title = rng.choice(FORMS).format(rng.choice(TOPICS)).capitalize()
        if wtype == "REV":
            title += ": a review"
        if wtype == "EDT":
            title = f"Editorial: {rng.choice(TOPICS)}"
        add(wid, title, year, wtype, rng.choice(["S07", "S08"]), "", False, "FEED", background_byline())
        earlier = [w for w, y in pool if y <= year]
        for target in rng.sample(earlier, min(len(earlier), rng.choice([0, 1, 2, 2, 3]))):
            cites.append((wid, target))
        pool.append((wid, year))

    works.sort(key=lambda w: int(w["work_id"][1:]))
    order = {w["work_id"]: i for i, w in enumerate(works)}
    authorships.sort(key=lambda r: (order[r["work_id"]], r["author_position"], r["affil_seq"]))
    cites = sorted(set(cites), key=lambda c: (order[c[0]], order[c[1]]))
    return {
        "institutions.csv": institutions,
        "authors.csv": authors,
        "sources.csv": sources,
        "works.csv": works,
        "authorships.csv": authorships,
        "citations.csv": [dict(citing_work_id=a, cited_work_id=b) for a, b in cites],
    }


def main():
    DATA.mkdir(exist_ok=True)
    for name, table in build().items():
        with open(DATA / name, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(table[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(table)
        print(f"{name}: {len(table)} rows")


if __name__ == "__main__":
    main()
