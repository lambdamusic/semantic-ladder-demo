"""The credit domain at 300 issuers plus deep corporate groups: questions that follow links.

    python domains/credit/paths.py          # -> domains/credit_paths/

The 300-issuer data of scale.py (same seed), plus six invented groups four to six levels
deep, built so that answering means walking parent and guarantee links:
- a parent link that names a RESEARCH record, so the chain goes on from that entity's RATINGS record;
- a RESEARCH record giving a stale parent that the RATINGS record overrules;
- members domiciled in Valdoria, some by a RESEARCH record that overrules RATINGS;
- notes guaranteed by the group's top entity, and some by an entity of another group;
- a QA test record attached inside a group.
The designed entities' IDs go in anchors.json, which build_questions.py reads to write the
path questions (Q49 on) with keys computed from the data.
"""
import csv
import json
import os
import random
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import scale  # noqa: E402

SIZE = 300
SHAPES = [  # children per member, level by level from the top
    [3, 2, 2, 1, 1, 1],
    [2, 2, 1, 2, 1],
    [3, 1, 2, 1],
    [2, 3, 1, 1, 1],
    [2, 1, 2, 1],
    [3, 2, 1, 1],
]
TOPS = ["GB", "DE", "US", "FR", "NL", "VD"]


def build():
    seed = int(__import__("hashlib").sha256(str(SIZE).encode()).hexdigest()[:8], 16)
    entities, instruments, actions = scale.generate(SIZE, seed)
    rng = random.Random(seed + 1)
    ids = {"E": 5000, "I": 5000, "A": 5000}

    def new(kind):
        ids[kind] += 1
        return f"{kind}{ids[kind]}"

    def act(rated, kind, basis, action, rating, outlook, when):
        actions.append([new("A"), when, rated, kind, basis, action, rating, outlook, "", ""])

    anchors = {"groups": []}
    used = {r[1].rsplit(" ", 1)[0] for r in entities}
    for g, (shape, top_country) in enumerate(zip(SHAPES, TOPS)):
        stem = scale.word(rng)
        top = new("E")
        entities.append([top, f"{stem} Group {scale.SUFFIX[top_country]}", scale.lei(rng), top_country, "CORP", "", "RATINGS"])
        levels, members = [[top]], {top: top_country}
        for width in shape:
            nxt = []
            for p in levels[-1]:
                for _ in range(width):
                    c = new("E")
                    country = rng.choice(["GB", "DE", "FR", "NL", "US", "IT", "ES", "VD", "CV"]) if rng.random() < 0.4 else members[p]
                    label = f"{stem} {rng.choice(scale.SECTORS)}"
                    while label in used:  # names are unique, so a question can name an entity
                        label = f"{stem} {scale.word(rng)} {rng.choice(scale.SECTORS)}"
                    used.add(label)
                    entities.append([c, f"{label} {scale.SUFFIX[country]}", scale.lei(rng), country,
                                     "BANK" if rng.random() < 0.15 else "CORP", p, "RATINGS"])
                    members[c] = country
                    nxt.append(c)
            levels.append(nxt)
        info = {"top": top, "deepest": levels[-1][0], "depth": len(levels) - 1,
                "cousins": [levels[-1][0], levels[-1][-1]] if len(levels[-1]) > 1 else None}
        # ratings on about half the members, a quarter of them below investment grade
        for e in members:
            if rng.random() < 0.55:
                r = rng.choice(scale.SCALE[2:14])
                start = scale.date(rng, 2022, 2025)
                act(e, "LTIDR", "FC", "AS", scale.notch(r, 0, scale.CEILING.get(members[e])), "STA", start)
                if rng.random() < 0.3:
                    act(e, "LTIDR", "FC", "DG", scale.notch(r, 1, scale.CEILING.get(members[e])), "NEG",
                        scale.date(rng, int(start[:4]) + 1, 2026))
        # a note issued low in the group, guaranteed by the top
        issuer = levels[2][0]
        i = new("I")
        instruments.append([i, f"{stem} Funding {rng.randint(3, 7)}.25% notes due {rng.randint(2028, 2035)}",
                            issuer, top, "SU", "EUR", f"{rng.randint(2028, 2035)}-12-31"])
        act(i, "INST", "", "AS", rng.choice(scale.SCALE[3:9]), "", scale.date(rng, 2023, 2025))
        info["guaranteed_note"] = i
        anchors["groups"].append(info)
        anchors["groups"][-1]["levels"] = levels

    G = anchors["groups"]
    # 1. In group 0, the link from level 3 to level 2 names a RESEARCH twin of the level-2 entity.
    mid = G[0]["levels"][2][0]
    row = next(r for r in entities if r[0] == mid)
    twin = new("E")
    entities.append([twin, row[1].upper(), row[2], row[3], row[4], "", "RESEARCH"])
    for r in entities:
        if r[5] == mid and r[0] in G[0]["levels"][3]:
            r[5] = twin
            break
    linked = next(r[0] for r in entities if r[5] == twin)
    anchors["via_twin"] = {"record": twin, "of": mid, "child": linked}
    # 2. In group 1, a RESEARCH record of a level-2 member that names group 2's top as its parent (stale).
    stale = G[1]["levels"][2][0]
    row = next(r for r in entities if r[0] == stale)
    entities.append([new("E"), row[1].upper(), row[2], row[3], row[4], G[2]["top"], "RESEARCH"])
    anchors["stale_parent"] = {"entity": stale, "claimed": G[2]["top"]}
    # 3. In group 3, a member the RATINGS record puts in NL that RESEARCH puts in VD.
    vd = G[3]["levels"][1][0]
    row = next(r for r in entities if r[0] == vd)
    row[3] = "NL"
    entities.append([new("E"), row[1].upper(), row[2], "VD", row[4], "", "RESEARCH"])
    for a in actions:  # domiciled in VD, so its foreign-currency rating stays within Valdoria's ceiling
        if a[2] == vd and a[3] == "LTIDR":
            a[6] = scale.notch(a[6], 0, scale.CEILING["VD"])
    anchors["vd_by_research"] = vd
    # 4. A note issued in group 4, guaranteed by group 5's top: support across groups.
    i = new("I")
    instruments.append([i, f"Cross-group 4.75% notes due 2031", G[4]["levels"][1][0], G[5]["top"], "SU", "USD", "2031-06-30"])
    act(i, "INST", "", "AS", "BBB", "", "2025-02-14")
    anchors["cross_note"] = i
    # 5. A QA record placed under group 0's top, with a rating of its own.
    qa = new("E")
    entities.append([qa, f"{scale.word(rng)} Test {scale.SUFFIX['GB']}", scale.lei(rng), "VD", "CORP", G[0]["top"], "QA"])
    act(qa, "LTIDR", "FC", "AS", "B-", "NEG", "2026-03-01")
    anchors["qa_member"] = qa
    return entities, instruments, actions, anchors


def main():
    target = HERE.parent / "credit_paths"
    shutil.rmtree(target, ignore_errors=True)
    (target / "data").mkdir(parents=True)
    for name in ["ontology.ttl", "ontology.md", "padding.md", "domain.py", "axioms.ttl"]:
        shutil.copy(HERE / name, target / name)
    entities, instruments, actions, anchors = build()
    random.Random(7).shuffle(actions)
    for name, extra in [("entities.csv", entities), ("instruments.csv", instruments), ("rating_actions.csv", actions)]:
        with open(target / "data" / name, "w", newline="") as out:
            out.write((HERE / "data" / name).read_text())
            csv.writer(out, lineterminator="\n").writerows(extra)
    (target / "anchors.json").write_text(json.dumps(anchors, indent=1) + "\n")
    import csv_to_rdf
    csv_to_rdf.DATA = target / "data"
    csv_to_rdf.build().serialize(target / "data" / "facts.ttl", format="turtle")
    env = dict(os.environ, CREDIT_FOLDER=str(target))
    for script in ["build_questions.py", "execute.py"]:
        subprocess.run([sys.executable, str(HERE / script)], env=env, check=True)
    print(f"{target.name}: {len(entities)} entity records, {len(instruments)} instruments, {len(actions)} actions")


if __name__ == "__main__":
    main()
