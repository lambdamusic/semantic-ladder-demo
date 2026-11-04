Six files, shown as the model gets them in the `csv` conditions. `generate_data.py` writes them from a fixed seed.

There are 52 designed works and 33 background works. The background works are noise: their authors are at four background institutions, and they cite only each other, except for the few that set up the citation-window questions.

- **Who is who:** Mara Ellison has three author records with one ORCID (`A01` to `A03`). `A04`, also "M. Ellison", is someone else. `A05` and `A06` are two different Jonas Brandts.
- **Hierarchy:** Tessel Laboratory (`I04`) is under the Albury Centre for Marine Robotics (`I03`), under the University of Albury (`I02`), under the Albury University System (`I01`). Halloran Institute (`I06`) has `I02` as its parent but is an affiliated institute, not a unit.
- **Versions:** `W02` is the preprint of `W03`, and `W42` of `W31`.
- **Test records:** `W90` to `W92` come from `STG`. Counted, they would make `W22` Kesting's most-cited work.
- **Affiliations:** `W70` and `W71` list two affiliations in opposite orders, so the rule about the last one decides which institution gets each.

The `executed` condition gets the tables `execute.py` writes:
- test records dropped;
- preprints merged into their published versions;
- each work flagged as research output or not;
- authors merged into people;
- one credited institution per person and work;
- the institution roll-ups;
- tiers ranked.
