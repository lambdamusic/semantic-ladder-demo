Six files, shown as the model gets them in the conditions that read CSV. `generate_data.py` writes them from a fixed seed.

There are 52 designed works and 33 background works. The background works are noise: their authors are at four background institutions, and they cite only each other, except for the few that set up the citation-window questions.

The hierarchy: Tessel Laboratory (I04, LAB) sits under the Albury Centre for Marine Robotics (I03, LAB), under the University of Albury (I02, UNI), under the Albury University System (I01, SYS), which also holds Albury Metropolitan University (I05). Halloran Institute (I06, AFF) has I02 as its parent but is not a unit of it. Kesting Institute of Hydrodynamics (I08, LAB) sits under Kesting University (I07).

The traps these records set, and the questions that test each, are on the [Questions page](/domains/research/questions/).

The `executed` condition gets the tables `execute.py` writes:
- test records dropped;
- preprints merged into their published versions;
- each work flagged as research output or not;
- authors merged into people;
- one credited institution per person and work;
- the institution roll-ups;
- tiers ranked.
