"""A scaled copy of the research domain: the base data plus invented works that repeat its traps.

    python domains/research/scale.py 850      # -> domains/research_850/ (850 works in all)

N is the total number of works. The base records stay exactly as they are, so every question
keeps its point, and a question about one record (W07, W23, W70, W71, I04, I06, S01...) keeps
its answer. The added works carry the same traps many times over, on the designed people,
institutions and sources, so the aggregate keys change and need counting and joining across
many records:

- Mara Ellison under a fourth record, "M. Ellison", the name of two other people (A04 and a
  new one at Rostval); Lena Vossberg, Jonas Brandt (Albury Metropolitan), Tomasz Wierzba and
  Sofie de Raat under second records; a third Jonas Brandt and a second Priya Ramanathan;
- more works for the Albury system's universities and labs (two new labs, I19 and I20), for
  Kesting and its institute, for Rostval (a new lab, I23), and for the other designed institutions;
- authors listing two affiliations, where the last-listed decides: Tessel and Halloran, and
  two new affiliated institutes (I21 under Albury Metropolitan, I22 under Kesting);
- preprints with their published versions, and preprints without one;
- STG test records, many of them citing a Kesting work; retracted works, some citing;
- SUP supplement articles, editorials, errata and paratext; works in delisted (K0) sources;
- citations to the sonar paper at every level of self-citation, to W30 and W31 inside and
  outside their windows, around W01 at one and two hops, and to Kesting from many
  institutions, Rostval with four Rostval authors on each citing work;
- background works by background people, in background journals, citing each other.

Fractional counts (Q12, Q14) must stay whole numbers: if the added 2024 works leave a fraction
for Kesting or for GB, one consortium work with as many authors as the fraction's
denominator makes it whole. Seeded, so a size always gives the same data.

ALL OF IT IS INVENTED, like the base data: DOIs use the prefix 10.55555, and ORCIDs are not
checksummed. The keys are computed from the data by build_questions.py (none are written by
hand at scale), csv_to_rdf.py writes the RDF, and execute.py the executed condition's tables.
"""
import csv
import hashlib
import importlib
import os
import random
import shutil
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).parent
FILES = ["institutions.csv", "authors.csv", "sources.csv", "works.csv", "authorships.csv", "citations.csv"]

# institution_id, name, country, type, parent_id
NEW_INSTITUTIONS = [
    ("I19", "Albury Laboratory for Acoustic Imaging", "GB", "LAB", "I02"),
    ("I20", "Albury Metropolitan Centre for Port Studies", "GB", "LAB", "I05"),
    ("I21", "Wexcombe Institute for Estuary Research", "GB", "AFF", "I05"),
    ("I22", "Sandhaven Institute for Wave Research", "DE", "AFF", "I07"),
    ("I23", "Rostval Laboratory for Offshore Structures", "NL", "LAB", "I09"),
    # background
    ("I24", "Pellmore University", "US", "UNI", ""),
    ("I25", "Università di Calvessa", "IT", "UNI", ""),
    ("I26", "Tarnowa University of Technology", "PL", "UNI", ""),
    ("I27", "Kirrabay University", "AU", "UNI", ""),
    ("I28", "Nordvik University", "NO", "UNI", ""),
    ("I29", "Hanseo Ocean Institute", "KR", "GOV", ""),
    ("I30", "Universidade de Arvela", "PT", "UNI", ""),
    ("I31", "Corrimal Marine Systems Inc", "US", "CO", ""),
]
BACKGROUND_INSTS = ["I15", "I16", "I17", "I18"] + [i for i, *_ in NEW_INSTITUTIONS[5:]]

# source_id, name, type, tier: no new K3 source, so S01 stays the only one in the highest tier
NEW_SOURCES = [
    ("S09", "Journal of Coastal Hydraulics", "JOU", "K2"),
    ("S10", "Marine Technology Bulletin", "JOU", "K1"),
    ("S11", "Annals of Ocean Observation", "JOU", "K2"),
    ("S12", "Shelf Sea Letters", "JOU", "K1"),
    ("S13", "International Journal of Ocean Frontiers", "JOU", "K0"),
    ("S14", "CoastRxiv", "REP", ""),
]
DESIGNED_SOURCES = ["S01"] * 3 + ["S02"] * 3 + ["S03"] * 3 + ["S06", "S09", "S10", "S11"]
BACKGROUND_SOURCES = ["S07", "S08", "S09", "S10", "S11", "S12"]
REPOSITORIES = ["S05", "S05", "S14"]

FIRST = ["Alba", "Bastian", "Carys", "Dorian", "Elsa", "Florin", "Greta", "Henrik", "Ilse", "Jarno", "Katrin",
         "Linus", "Marit", "Nils", "Olwen", "Pim", "Quinn", "Rosa", "Silas", "Tamsin", "Ulla", "Viggo", "Wren",
         "Yara", "Zeno", "Anouk", "Bryony", "Cosimo", "Delphine", "Emrys", "Fenna", "Gideon", "Hester", "Ivo",
         "Jolien", "Kester", "Liesel", "Maelle", "Niko", "Odile"]
LAST = ["Aldous", "Brockmann", "Castellan", "Dewhurst", "Eberhardt", "Falconer", "Gisborne", "Haverkamp",
        "Ibbotson", "Jansma", "Kerridge", "Lachance", "Merriman", "Nordahl", "Ostergaard", "Penhallow", "Quarrie",
        "Rademaker", "Sallis", "Tregunna", "Uttley", "Vandersloot", "Whitcombe", "Yelland", "Zandvoort",
        "Ashdown", "Bellamore", "Corbridge", "Dannecker", "Elphick"]
MARINE = ["glider navigation", "sonar imaging", "acoustic positioning", "ocean optics", "buoy telemetry",
          "underwater docking", "seabed classification", "survey vessel autonomy", "sensor calibration",
          "fleet coordination", "turbidity sensing", "battery endurance"]
HYDRO = ["tidal mixing", "wave boundary layers", "bed shear stress", "turbulent wakes", "stratified flows",
         "vortex shedding", "sediment resuspension", "estuarine plumes", "breaking waves", "channel hydraulics"]
COAST = ["wave runup", "estuarine salinity", "tidal asymmetry", "sediment flux", "storm surge", "dune erosion",
         "river plumes", "harbour seiches", "coastal upwelling", "beach profiles", "internal waves", "marsh accretion"]
FORMS = ["Observations of {}", "A model of {}", "Seasonal variability in {}", "Remote sensing of {}",
         "Uncertainty in {} estimates", "Long-term trends in {}", "Field measurements of {}", "A framework for {}",
         "Low-cost methods for {}", "Machine learning for {}", "Revisiting {}", "Scaling laws for {}"]
PLACES = ["the North Sea", "the Albury estuary", "a macrotidal bay", "shallow channels", "the Brevin shelf",
          "harbour basins", "a laboratory flume", "sandy coasts", "fjords", "tidal inlets", "the open shelf",
          "mixed-energy coasts", "the Wexcombe marshes", "a semi-enclosed sea"]
YEARS = list(range(2019, 2026))
NOT_2024 = [y for y in YEARS if y != 2024]


def read(folder, name):
    with open(folder / "data" / name, newline="") as f:
        return list(csv.DictReader(f))


class Generator:
    """Adds records to the base data. Works get IDs from W201 up, in shuffled order."""

    def __init__(self, n_add, seed):
        self.rng = rng = random.Random(seed)
        self.s = n_add / 765  # the counts below are written for 850 works in all
        base = {name: read(HERE, name) for name in FILES}
        self.base = base
        self.base_works = {w["work_id"]: w for w in base["works.csv"]}
        self.orcid = {a["author_id"]: a["orcid"] for a in base["authors.csv"]}
        self.used_orcids = {o for o in self.orcid.values() if o}
        self.used_dois = {w["doi"] for w in base["works.csv"]}
        self.used_titles = {w["title"] for w in base["works.csv"]}
        self.used_names = {a["name"] for a in base["authors.csv"]}
        self.rows = {name: [] for name in FILES}
        self.meta = {}  # work_id -> {year, target (may random citations point at it), type}
        self.ids = [f"W{i}" for i in range(201, 201 + n_add + 100)]
        rng.shuffle(self.ids)
        self.next_author = 100
        self.cites = []

        letters = "abcdefghjkmnpqrstvwxyz0123456789"
        for iid, name, country, itype, parent in NEW_INSTITUTIONS:
            self.rows["institutions.csv"].append(dict(
                institution_id=iid, name=name, ror="0" + "".join(rng.choice(letters) for _ in range(6)) + f"{rng.randint(10, 99)}",
                country=country, type=itype, parent_id=parent))
        for sid, name, stype, tier in NEW_SOURCES:
            self.rows["sources.csv"].append(dict(
                source_id=sid, name=name, type=stype, tier=tier,
                issn=f"{rng.randint(1000, 9999)}-{rng.randint(100, 999)}{rng.choice('0123456789X')}" if stype == "JOU" else ""))
        self.people()

    def k(self, x):
        return max(1, round(x * self.s))

    # People -------------------------------------------------------------------------------------

    def new_orcid(self):
        while True:
            d = "".join(self.rng.choice("0123456789") for _ in range(9))
            o = f"0000-000{d[0]}-{d[1:5]}-{d[5:9]}"
            if o not in self.used_orcids:
                self.used_orcids.add(o)
                return o

    def fresh_name(self):
        while True:
            n = f"{self.rng.choice(FIRST)} {self.rng.choice(LAST)}"
            if n not in self.used_names:
                self.used_names.add(n)
                return n

    def author(self, name=None, orcid=None, no_orcid=False):
        self.next_author += 1
        aid = f"A{self.next_author}"
        self.rows["authors.csv"].append(dict(author_id=aid, name=name or self.fresh_name(),
                                             orcid="" if no_orcid else (orcid or self.new_orcid())))
        return aid

    def people(self):
        o = self.orcid
        # Second records of designed people (same ORCID), and same-name different people
        self.MARA_M = self.author("M. Ellison", o["A01"])           # Mara again, under the name A04 also has
        self.ELLISON_ROS = self.author("M. Ellison")                # a third "M. Ellison", at Rostval
        self.LENA_L = self.author("L. Vossberg", o["A09"])
        self.JONAS_J = self.author("J. Brandt", o["A05"])           # the Albury Metropolitan Jonas Brandt
        self.JONAS_OSK = self.author("Jonas Brandt")                 # a third Jonas Brandt, at Oskel
        self.TOMASZ_T = self.author("T. Wierzba", o["A08"])
        self.SOFIE_S = self.author("S. de Raat", o["A11"])
        self.PRIYA_JP = self.author("Priya Ramanathan")              # a different Priya Ramanathan, at Hoshimine
        self.FELDKAMP = self.author()                               # appears only on test (STG) records

        def group(existing, homes):
            return list(existing) + [(self.author(no_orcid=self.rng.random() < 0.05), h) for h in homes]

        self.ALB = group([], ["I02"] * 5 + ["I03"] * 4 + ["I04"] * 3 + ["I19"] * 4)
        self.AMU = group([("A16", "I05")], ["I05"] * 4 + ["I20"] * 2)
        self.WEX = group([], ["I21"] * 2)
        self.HAL = group([("A22", "I06")], ["I06"] * 2)
        self.KES = group([("A10", "I08")], ["I07"] * 6 + ["I08"] * 4)
        self.SAN = group([], ["I22"] * 2)
        self.ROS = group([("A11", "I09"), ("A18", "I09"), ("A19", "I09"), ("A20", "I09"),
                          (self.SOFIE_S, "I09"), (self.ELLISON_ROS, "I09")], ["I09"] * 5 + ["I23"] * 2)
        self.LOR = group([("A14", "I12")], ["I12"] * 5)
        self.BRE = group([("A13", "I11")], ["I11"] * 3)
        self.OSK = group([("A17", "I14")], ["I14"] * 4)
        self.DUN = group([("A15", "I13")], ["I13"] * 3)
        self.MAR = group([("A12", "I10")], ["I10"] * 2)
        bg_old = [(f"A{30 + n}", ["I15", "I16", "I17", "I18"][n % 4]) for n in range(16)]
        bg_new = []
        for n in range(46):
            home = BACKGROUND_INSTS[n % len(BACKGROUND_INSTS)]
            bg_new.append((self.author(no_orcid=self.rng.random() < 0.08), home))
        for n in range(6):  # same name, different people, at different background institutions
            name = self.fresh_name()
            for home in self.rng.sample(BACKGROUND_INSTS, 2):
                bg_new.append((self.author(name), home))
        self.BG = bg_old + bg_new + [(self.PRIYA_JP, "I16")]
        self.EXT = self.LOR + self.BRE + self.OSK + self.DUN + self.MAR + self.BG  # co-authors from outside
        self.FILL = self.LOR + self.BRE + self.OSK + self.MAR + self.BG          # no GB, Kesting or Rostval
        self.GB = self.ALB + self.AMU + self.DUN + self.HAL

    # Works --------------------------------------------------------------------------------------

    def title(self, topics):
        while True:
            t = self.rng.choice(FORMS).format(self.rng.choice(topics))
            if self.rng.random() < 0.6:
                t += f" in {self.rng.choice(PLACES)}"
            t = t[0].upper() + t[1:]
            if t not in self.used_titles:
                self.used_titles.add(t)
                return t

    def doi(self, source, year):
        while True:
            d = f"10.55555/{source.lower()}.{year}.{self.rng.randint(1000, 9999)}"
            if d not in self.used_dois:
                self.used_dois.add(d)
                return d

    def work(self, title, year, wtype, source, byline, version_of="", retracted=False, origin="FEED",
             cites=(), target=True):
        """byline: [(author, [institutions in the order listed])]"""
        wid = self.ids.pop()
        self.rows["works.csv"].append(dict(work_id=wid, title=title, year=year, type=wtype, source_id=source,
                                           doi=self.doi(source, year), version_of=version_of,
                                           is_retracted="true" if retracted else "false", record_source=origin))
        for pos, (a, insts) in enumerate(byline, 1):
            for seq, inst in enumerate(insts, 1):
                self.rows["authorships.csv"].append(dict(work_id=wid, author_id=a, author_position=pos,
                                                         institution_id=inst, affil_seq=seq))
        self.cites += [(wid, c) for c in cites]
        self.meta[wid] = dict(year=year, type=wtype, target=target and wtype != "PTX" and origin != "STG",
                              title=title, byline=byline, retracted=retracted, source=source)
        return wid

    def team(self, core, n_core, ext=None, n_ext=0):
        picked = self.rng.sample(core, n_core) + (self.rng.sample(ext, n_ext) if n_ext else [])
        return [(a, [i]) for a, i in picked]

    def generic(self, core, n, topics, years=YEARS, ext=None, ext_p=0.3, sizes=(1, 1, 2, 2, 3), target=True,
                lead=None, sources=DESIGNED_SOURCES):
        """n research works by a group, some with an outside co-author; lead: a fixed first author."""
        made = []
        ext = self.EXT if ext is None else ext
        if lead:
            core = [p for p in core if p[0] != lead[0]]
        for _ in range(n):
            size = min(self.rng.choice(sizes), len(core) + (1 if lead else 0))
            by = ([lead] if lead else []) + self.team(core, size - 1 if lead else size,
                                                      ext, 1 if self.rng.random() < ext_p else 0)
            wtype = self.rng.choices(["ART", "REV"], [9, 1])[0]
            t = self.title(topics) + (": a review" if wtype == "REV" else "")
            made.append(self.work(t, self.rng.choice(years), wtype, self.rng.choice(sources), by, target=target))
        return made

    def preprint(self, wid, swap=None):
        """A preprint of a published work: same title and byline (swap: author record -> another record of that person)."""
        m = self.meta[wid]
        by = [((swap or {}).get(a, a), insts) for a, insts in m["byline"]]
        year = max(2019, m["year"] - self.rng.choice([0, 1, 1]))
        return self.work(m["title"], year, "PPR", self.rng.choice(REPOSITORIES), by, version_of=wid, target=m["target"])

    # The traps ----------------------------------------------------------------------------------

    def designed(self):
        rng, k = self.rng, self.k
        alb = self.ALB
        mara_records = ["A01", "A01", "A01", "A02", "A02", "A02", "A03", "A03", self.MARA_M, self.MARA_M, self.MARA_M]

        # Mara Ellison: research works under four records, at the University of Albury
        mara = []
        for n in range(k(11)):
            rec = mara_records[n % len(mara_records)]
            by = [(rec, ["I02"])] + self.team(alb, rng.choice([0, 1, 1]), self.EXT, 1 if rng.random() < 0.3 else 0)
            mara.append(self.work(self.title(MARINE), rng.choice(YEARS), "ART", rng.choice(DESIGNED_SOURCES), by))
        self.preprint(mara[0], {"A01": "A02"})
        self.preprint(mara[3], {"A02": self.MARA_M, self.MARA_M: "A03"})
        # and her works that are not research output
        for n in range(k(2)):
            self.work(f"Editorial: {rng.choice(MARINE)}", rng.choice(YEARS), "EDT", "S01", [(["A01", self.MARA_M][n % 2], ["I02"])])
        for w in mara[1:1 + k(2)]:
            m = self.meta[w]
            self.work(f"Erratum: {m['title']}", min(2025, m["year"] + 1), "ERR", m["source"], m["byline"])
        self.work(self.title(MARINE), 2022, "ART", "S04", [("A02", ["I02"])])
        self.work(self.title(MARINE), 2024, "ART", "S13", [("A03", ["I02"]), (alb[0][0], [alb[0][1]])])
        self.work(self.title(MARINE), 2023, "ART", "S02", [("A01", ["I02"]), (alb[4][0], [alb[4][1]])], retracted=True)

        # Priya Ramanathan: one record, more works than any one of Mara's records, fewer than Mara
        priya = self.generic(alb, k(9), MARINE, lead=("A07", ["I03"]), sizes=(1, 2, 2))
        self.preprint(priya[0])

        # The Albury system: its universities and labs
        albury = self.generic(alb, k(50), MARINE)
        for w in albury[:2]:
            self.preprint(w)
        self.generic(self.AMU, k(25), COAST + MARINE)
        jonas = self.generic(self.AMU, k(5), COAST, lead=("A05", ["I05"]), sizes=(1, 2))
        self.generic(self.AMU, k(2), COAST, lead=(self.JONAS_J, ["I05"]), sizes=(1, 2))
        self.preprint(jonas[0], {"A05": self.JONAS_J})
        # affiliated institutes, and authors listing two affiliations: the one listed last is credited
        self.generic(self.WEX, k(5), COAST)
        for n in range(k(4)):
            a, _ = rng.choice([p for p in self.AMU if p[1] == "I05"])
            insts = ["I21", "I05"] if n % 2 == 0 else ["I05", "I21"]
            self.work(self.title(COAST), rng.choice(YEARS), "ART", rng.choice(DESIGNED_SOURCES), [(a, insts)])
        for n in range(k(10)):  # Tomasz Wierzba: Tessel and Halloran, in both orders
            insts = ["I04", "I06"] if n % 2 == 0 else ["I06", "I04"]
            by = [(["A08", self.TOMASZ_T][n % 3 == 2], insts)]
            if rng.random() < 0.4:
                by += self.team(self.HAL if insts[-1] == "I06" else alb, 1)
            self.work(self.title(COAST), rng.choice(YEARS), "ART", rng.choice(DESIGNED_SOURCES), by)
        self.generic(self.HAL, k(4), COAST, lead=("A22", ["I06"]), sizes=(1, 1, 2))
        self.generic(self.HAL, k(3), COAST)

        # Kesting University and its institute; its works get citations only from the blocks below
        kes = self.generic(self.KES, k(30), HYDRO, years=[2024] * k(6) + NOT_2024 * 4, sizes=(1, 1, 2, 2), target=False)
        lena = self.generic(self.KES, k(5), HYDRO, years=[2024, 2024] + NOT_2024, lead=("A09", ["I07"]),
                            sizes=(1, 2), target=False)
        lena += self.generic(self.KES, k(3), HYDRO, years=NOT_2024, lead=(self.LENA_L, ["I08", "I07"]),
                             sizes=(1, 2), target=False)
        marcus = self.generic(self.KES, k(5), HYDRO, years=NOT_2024, lead=("A04", ["I07"]), sizes=(1, 2), target=False)
        sup = []
        for n in range(k(5)):
            sup.append(self.work(self.title(HYDRO), rng.choice(NOT_2024), "SUP", ["S06", "S06", "S06", "S02", "S02"][n % 5],
                                 self.team(self.KES, rng.choice([1, 2])), target=False))
        for a, insts in [("A09", ["I07"]), (self.LENA_L, ["I07"]), ("A10", ["I08"]), (self.KES[3][0], ["I07"])][:k(4)]:
            self.work(self.title(HYDRO), rng.choice(NOT_2024), "ART", rng.choice(["S01", "S02", "S03"]), [(a, insts)],
                      retracted=True, target=False)
        for w in [x for x in kes if self.meta[x]["year"] != 2019][:k(4)]:
            self.preprint(w)
        for insts in [["I22", "I07"], ["I22", "I07"], ["I07", "I22"], ["I07", "I22"], ["I07", "I12"], ["I12", "I07"]]:
            a = rng.choice([p for p in self.KES if p[1] == "I07"])[0]
            self.work(self.title(HYDRO), rng.choice(NOT_2024), "ART", rng.choice(DESIGNED_SOURCES), [(a, insts)], target=False)
        for a in ["A04", "A10"]:
            self.work(self.title(HYDRO), rng.choice(YEARS), "ART", rng.choice(["S04", "S13"]), [(a, ["I07"])], target=False)
        self.generic(self.SAN, k(5), HYDRO)
        kesting = ["W20", "W08", "W16", "W21", "W24"] + [w for w in kes + lena + marcus + sup
                                                         if not self.meta[w]["retracted"]]

        # Rostval: in 2024, one author of four on each work; otherwise not in 2024
        for _ in range(k(12)):
            by = self.team(self.ROS, 1, self.FILL, 3)
            self.work(self.title(HYDRO + COAST), 2024, "ART", rng.choice(DESIGNED_SOURCES), by)
        ros = self.generic(self.ROS, k(25), HYDRO + COAST, years=NOT_2024, ext=self.FILL, sizes=(1, 2, 3, 4))
        for w in ros[:2]:
            self.preprint(w, {"A11": self.SOFIE_S})
        self.work(self.title(HYDRO), 2022, "ART", "S02", self.team(self.ROS, 2), retracted=True)

        # The other designed institutions
        self.generic(self.LOR, k(25), HYDRO + COAST)
        self.generic(self.LOR, k(4), COAST, lead=("A06", ["I12"]), sizes=(1, 2))
        self.generic(self.BRE, k(15), COAST + MARINE)
        osk = self.generic(self.OSK, k(20), COAST + HYDRO)
        self.generic(self.OSK, k(3), COAST, lead=(self.JONAS_OSK, ["I14"]), sizes=(1, 2))
        dun = self.generic(self.DUN, k(15), COAST)
        mar = self.generic(self.MAR, k(8), MARINE)
        others = self.generic(self.LOR + self.BRE, k(3), COAST)
        for w in osk[:4] + dun[:1] + mar[:1] + others:
            self.preprint(w)
        for _ in range(k(10)):  # preprints with no published version in the data
            g = rng.choice([self.ALB, self.AMU, self.LOR, self.OSK, self.BRE, self.DUN, self.BG])
            self.work(self.title(COAST + MARINE), rng.choice(YEARS), "PPR", rng.choice(REPOSITORIES), self.team(g, rng.choice([1, 2])))
        for n in range(k(2)):
            self.work(self.title(COAST), rng.choice(YEARS), "ART", "S02", self.team(self.LOR, 1), retracted=True)

        # Supplement articles, editorials, errata, paratext, delisted sources
        for _ in range(k(5)):
            self.work(self.title(COAST + HYDRO), rng.choice(YEARS), "SUP", "S06", self.team(self.BRE + self.LOR + self.DUN, rng.choice([1, 2])))
        for _ in range(k(3)):
            self.work(f"Foreword: {rng.choice(HYDRO)}", rng.choice(YEARS), "EDT", "S06", [])
        for _ in range(k(7)):
            g = rng.choice([self.ALB, self.KES, self.ROS, self.LOR, self.BRE, self.DUN])
            self.work(f"Editorial: {rng.choice(MARINE + HYDRO + COAST)}", rng.choice(YEARS), "EDT",
                      rng.choice(["S01", "S02", "S03"]), self.team(g, 1), target=g is not self.KES)
        for w in rng.sample(albury + osk + dun, k(5)):
            m = self.meta[w]
            self.work(f"Erratum: {m['title']}", min(2025, m["year"] + 1), "ERR", m["source"], m["byline"])
        for _ in range(k(10)):
            self.work(rng.choice(["Issue information", "Front matter", "Table of contents", "Masthead"]),
                      rng.choice(YEARS), "PTX", rng.choice(["S01", "S02", "S03", "S06"]), [])
        for n in range(k(18)):
            g = rng.choice([self.ALB, self.AMU, self.DUN, self.LOR, self.BG, self.OSK])
            self.work(self.title(COAST + MARINE), rng.choice(YEARS), rng.choice(["ART", "ART", "REV"]),
                      ["S04", "S13"][n % 2], self.team(g, rng.choice([1, 2])))

        self.citation_blocks(kesting)

    def citation_blocks(self, kesting):
        rng, k = self.rng, self.k
        alb = self.ALB
        test_people = [("A21", ["I07"]), (self.FELDKAMP, ["I07"])]

        # Kesting's works, cited from many institutions. Only these blocks cite Kesting (besides
        # base works), so W20 leads its citations, and W22 would lead only with the test records.
        others = [w for w in kesting if w != "W20"]
        load = Counter()

        def targets(with_w20):
            free = [w for w in others if load[w] < 2 and w != "W22"]
            out = (["W20"] if with_w20 else []) + rng.sample(free, rng.choice([1, 1, 2]) - (1 if with_w20 else 0) or 1)
            for w in out:
                load[w] += 1
            return out

        def year_after(ts, avoid_2024=False):
            years = [y for y in YEARS if y >= max(self.year(t) for t in ts) and not (avoid_2024 and y == 2024)]
            return rng.choice(years or [2025])

        plan = ([("LOR", 1)] * k(9) + [("ROS", 4)] * k(3) + [("BRE", 1)] * k(3) + [("ALB", 1)] * k(3)
                + [("AMU", 1)] * k(2) + [("OSK", 1)] * k(3) + [("DUN", 1)] * k(2) + [("SAN", 1)] * k(2))
        for n, (g, size) in enumerate(plan):
            ts = targets(n < 10)
            self.work(self.title(HYDRO), year_after(ts, avoid_2024=g == "ROS"), "ART", rng.choice(DESIGNED_SOURCES),
                      self.team(getattr(self, g), size), cites=ts)
        self.work(self.title(HYDRO), 2025, "ART", "S03", self.team(self.LOR, 1), retracted=True, cites=["W20", "W21"])
        for n in range(k(15)):  # test records citing W22, and sometimes another Kesting work
            ts = ["W22"] + ([rng.choice(others)] if n % 4 == 0 else [])
            self.work(self.title(HYDRO), 2025, rng.choice(["ART", "ART", "REV", "SUP"]), rng.choice(["S01", "S02", "S03", "S06"]),
                      [rng.choice(test_people)], origin="STG", cites=ts)
        for n in range(k(3)):  # test copies listing Lena Vossberg
            self.work(self.title(HYDRO), 2025, "ART", "S02", [("A09", ["I07"]), test_people[n % 2]], origin="STG")

        # The sonar paper (W03, with its preprint W02): self-citations at every level, and none
        sonar = [  # (byline, cites)
            ([("A01", ["I02"])], ["W03"]),
            ([(self.MARA_M, ["I02"]), (self.OSK[2][0], ["I14"])], ["W03", "W02"]),
            ([("A02", ["I02"])], ["W02"]),
            ([("A07", ["I03"])], ["W03"]),
            ([("A07", ["I03"]), (self.LOR[1][0], ["I12"])], ["W03"]),
            ([(alb[9][0], [alb[9][1]])], ["W03"]),                       # Tessel: the University of Albury
            ([(alb[12][0], [alb[12][1]])], ["W03", "W02"]),              # the new acoustic-imaging lab
            ([(alb[0][0], [alb[0][1]]), (self.OSK[1][0], ["I14"])], ["W03"]),
            ([(self.AMU[1][0], ["I05"])], ["W03"]),                      # Albury Metropolitan: the system only
            ([(self.AMU[5][0], ["I20"])], ["W03"]),
            ([(self.AMU[2][0], ["I05"]), (self.AMU[3][0], ["I05"])], ["W02"]),
            ([(self.AMU[4][0], ["I05", "I13"])], ["W03"]),               # last listed Dunmore: GB, not the system
            ([(self.WEX[0][0], ["I21"])], ["W03"]),                      # an affiliated institute: GB only
            ([("A22", ["I06"])], ["W03"]),                               # Halloran: GB only
            ([(self.DUN[1][0], ["I13"])], ["W03"]),
            ([(self.DUN[2][0], ["I13"]), (self.BRE[1][0], ["I11"])], ["W03", "W02"]),
            ([("A04", ["I07"])], ["W03"]),                               # the other M. Ellison
            ([(self.ELLISON_ROS, ["I09"])], ["W03"]),                    # and a third
            ([(self.LOR[2][0], ["I12"])], ["W03"]),
            ([(self.BG[20][0], [self.BG[20][1]])], ["W02"]),
        ]
        for by, cites in sonar[:max(4, round(len(sonar) * self.s))]:
            target = not any(i in ("I07", "I08") for _, insts in by for i in insts)
            self.work(self.title(MARINE), rng.choice([2023, 2024, 2025]), "ART", rng.choice(DESIGNED_SOURCES), by,
                      cites=cites, target=target)
        self.work(self.title(MARINE), 2025, "ART", "S02", [("A21", ["I07"])], origin="STG", cites=["W03"])
        self.work(self.title(MARINE), 2025, "ART", "S01", [(self.FELDKAMP, ["I07"])], origin="STG", cites=["W02", "W03"])
        self.work(self.title(MARINE), 2024, "ART", "S03", [(alb[1][0], [alb[1][1]])], retracted=True, cites=["W03"])

        # W30 (2019): many citations, nearly all after its window; W31 (2023, preprint W42): all within it
        for n in range(k(10)):
            g = rng.choice([self.BG, self.BG, self.LOR, self.DUN])
            self.work(self.title(COAST), rng.choice([2022, 2023, 2024, 2025]), "ART", rng.choice(BACKGROUND_SOURCES),
                      self.team(g, rng.choice([1, 2])), cites=["W30"])
        self.work(self.title(COAST), 2021, "ART", "S07", self.team(self.BG, 1), cites=["W30"])
        self.work(self.title(COAST), 2024, "ART", "S08", self.team(self.BG, 1), retracted=True, cites=["W30", "W31"])
        self.work(self.title(COAST), 2025, "ART", "S08", [test_people[0]], origin="STG", cites=["W30", "W31"])
        for cites in (["W31"], ["W31"], ["W31"], ["W31"], ["W42"], ["W42"], ["W31", "W42"])[:max(2, round(7 * self.s))]:
            g = rng.choice([self.BG, self.OSK, self.BRE])
            self.work(self.title(COAST + HYDRO), rng.choice([2023, 2024, 2025]), "ART", rng.choice(BACKGROUND_SOURCES),
                      self.team(g, rng.choice([1, 2])), cites=cites)

        # Around W01 (2021): new works citing it, and works citing those; none of them is cited at random
        first = []
        for n in range(k(4)):
            g = rng.choice([self.OSK, self.BRE, self.BG, self.DUN])
            first.append(self.work(self.title(MARINE), [2022, 2023, 2023, 2024][n % 4], "ART", rng.choice(DESIGNED_SOURCES),
                                   self.team(g, rng.choice([1, 2])), cites=["W01"], target=False))
        hop = first + ["W40", "W41"]
        for n in range(k(8)):
            ts = rng.sample(hop, rng.choice([1, 1, 2]))
            if n == 0:
                ts = ts + ["W01"]  # a work at both one and two hops
            g = rng.choice([self.BG, self.LOR, self.MAR, self.DUN])
            self.work(self.title(MARINE), year_after(ts), "ART", rng.choice(DESIGNED_SOURCES), self.team(g, rng.choice([1, 2])),
                      cites=ts, target="W01" not in ts)
        self.work(self.title(MARINE), 2025, "ART", "S01", [test_people[1]], origin="STG", cites=["W01", first[0]])
        self.work(self.title(MARINE), 2024, "ART", "S02", self.team(self.BG, 1), retracted=True, cites=["W40"])

    def year(self, wid):
        return int(self.base_works[wid]["year"]) if wid in self.base_works else self.meta[wid]["year"]

    def background(self, n):
        for _ in range(n):
            wtype = self.rng.choices(["ART", "REV", "EDT"], [8, 1, 1])[0]
            title = self.title(COAST)
            if wtype == "REV":
                title += ": a review"
            if wtype == "EDT":
                title = f"Editorial: {title[0].lower()}{title[1:]}"
            self.work(title, self.rng.choice(YEARS), wtype, self.rng.choice(BACKGROUND_SOURCES),
                      self.team(self.BG, self.rng.choice([1, 1, 2, 2, 3])))

    def balance(self, b):
        """Make Kesting's and GB's fractional counts in 2024 whole, with one consortium work each if needed."""
        made = 0
        for share, pool, target in [(b.fractional("I07", 2024), [("A09", "I07")] + self.KES, False),
                                    (b.fractional(country="GB", yr=2024), self.ALB + self.AMU + self.DUN, True)]:
            if share.denominator == 1:
                continue
            need = 1 - (share - (share.numerator // share.denominator))
            inside, size = need.numerator, need.denominator
            by = self.team(pool, inside) + self.team(self.FILL, size - inside)
            self.work(f"A community intercomparison of {self.rng.choice(HYDRO + COAST)}", 2024, "ART", "S03", by,
                      target=target)
            made += 1
        return made

    def random_citations(self):
        """Every added work cites a few earlier added works that no question counts the citations of."""
        rng = self.rng
        pool = sorted((m["year"], w) for w, m in self.meta.items() if m["target"])
        versions = {(r["work_id"], r["version_of"]) for r in self.rows["works.csv"] if r["version_of"]}
        have = set(self.cites)
        for w, m in self.meta.items():
            if m["type"] == "PTX":
                continue
            earlier = [t for y, t in pool if y <= m["year"] and t != w and (w, t) not in versions and (t, w) not in versions]
            for t in rng.sample(earlier, min(len(earlier), rng.choice([0, 0, 1, 1, 2, 3]))):
                if (w, t) not in have:
                    have.add((w, t))
                    self.cites.append((w, t))

    def write(self, target):
        order = lambda wid: int(wid[1:])  # noqa: E731
        self.rows["works.csv"].sort(key=lambda w: order(w["work_id"]))
        self.rows["authorships.csv"].sort(key=lambda r: (order(r["work_id"]), r["author_position"], r["affil_seq"]))
        self.rows["citations.csv"] = [dict(citing_work_id=a, cited_work_id=b)
                                      for a, b in sorted(set(self.cites), key=lambda c: (order(c[0]), order(c[1])))]
        for name in FILES:
            with open(target / "data" / name, "w", newline="") as out:
                out.write((HERE / "data" / name).read_text())
                if self.rows[name]:
                    w = csv.DictWriter(out, fieldnames=list(self.base[name][0]), lineterminator="\n")
                    w.writerows(self.rows[name])


def rules(target):
    """build_questions.py, loaded over the scaled folder's data."""
    os.environ["RESEARCH_FOLDER"] = str(target)
    sys.modules.pop("build_questions", None)
    if str(HERE) not in sys.path:
        sys.path.insert(0, str(HERE))
    return importlib.import_module("build_questions")


def check(b):
    """The points the questions make still hold, and every comparison has one answer."""
    i02 = b.works_of("I02")
    by_person = Counter(p for w in i02 for p, i in b.credited(w).items() if "I02" in b.chain(i))
    by_record = Counter(a for w in i02 for a in {r["author_id"] for r in b.AUTHORSHIPS if r["work_id"] in b.records(w)
                                                 and "I02" in b.chain(b.credited(w)[b.PERSON[r["author_id"]]])})
    assert b.top_author("I02") == "A01", "Q6: Mara Ellison leads the University of Albury"
    assert b.PERSON[by_record.most_common(1)[0][0]] != b.MARA, "Q6: by record, someone else would lead"
    full = {i: len(b.works_of(i, 2024)) for i in ("I07", "I09")}
    frac = {i: b.fractional(i, 2024) for i in ("I07", "I09")}
    assert full["I09"] > full["I07"] and frac["I07"] > frac["I09"], ("Q13: the ranking flips", full, frac)
    assert len(b.citers("W30")) > len(b.citers("W31")) and len(b.in_window("W31", 2)) > len(b.in_window("W30", 2)), "Q22"
    citing = sorted(((len(b.citing_works_by(i, b.KESTING)), i) for i in b.INSTS if i not in b.chain("I07") and i != "I08"),
                    reverse=True)
    assert citing[0][1] == "I12" and citing[0][0] > citing[1][0], ("Q27: one leader", citing[:3])
    per_author = sum(len([p for p, i in b.credited(c).items() if "I09" in b.chain(i)])
                     for c in b.citing_works_by("I09", b.KESTING))
    assert per_author > citing[0][0], "Q27: counted per author, Rostval would win"
    cites = sorted(((b.citations(w), w) for w in b.KESTING), reverse=True)
    assert cites[0][0] > cites[1][0], ("Q33: one most-cited work", cites[:3])
    with_tests = Counter(d for c, d in b.CITES if d in b.KESTING and b.WORKS[c]["is_retracted"] == "false")
    assert with_tests.most_common(1)[0][0] != cites[0][1], "Q33: with test records another work would lead"
    assert [s for s, r in b.SOURCES.items() if r["tier"] == "K3"] == ["S01"], "Q40"
    names = ("Mara Ellison", "M. Ellison", "Ellison, Mara J.")
    assert len({b.PERSON[a] for a, r in b.AUTHORS.items() if r["name"] == "Mara Ellison"}) == 1, "Q7: one Mara Ellison"
    return dict(by_person=by_person.most_common(3), by_record=by_record.most_common(3), full=full, frac=frac,
                citing=citing[:3], cites=cites[:3], q1=len({b.PERSON[a] for a, r in b.AUTHORS.items() if r["name"] in names}))


def build(total):
    target = HERE.parent / f"research_{total}"
    shutil.rmtree(target, ignore_errors=True)
    (target / "data").mkdir(parents=True)
    for name in ["ontology.ttl", "ontology.md", "padding.md", "domain.py"]:
        shutil.copy(HERE / name, target / name)
    n_add = total - len(read(HERE, "works.csv"))
    g = Generator(n_add, seed=int(hashlib.sha256(f"research-{total}".encode()).hexdigest()[:8], 16))
    g.designed()
    designed = len(g.meta)
    g.background(n_add - 2 - designed)
    g.write(target)
    made = g.balance(rules(target))
    g.background(2 - made)
    g.random_citations()
    g.write(target)
    assert len(g.meta) == n_add

    sys.path.insert(0, str(HERE))
    import csv_to_rdf
    csv_to_rdf.DATA = target / "data"
    csv_to_rdf.build().serialize(target / "data" / "facts.ttl", format="turtle")
    env = dict(os.environ, RESEARCH_FOLDER=str(target))
    for script in ["build_questions.py", "execute.py"]:
        subprocess.run([sys.executable, str(HERE / script)], env=env, check=True)
    points = check(rules(target))
    print(f"{target.name}: {n_add} works added ({designed} on the traps, {made} to keep fractional counts whole), "
          + ", ".join(f"{len(g.rows[n])} {n.removesuffix('.csv')}" for n in FILES if n != "works.csv"))
    for name, value in points.items():
        print(f"  {name}: {value}")


if __name__ == "__main__":
    for size in sys.argv[1:] or ["850"]:
        build(int(size))
