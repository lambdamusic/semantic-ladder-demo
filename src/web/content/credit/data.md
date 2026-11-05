Three small files, shown exactly as the model gets them in the conditions that read CSV. The conditions that read RDF get the same rows as `facts.ttl`: a straight conversion, one resource per row and one property per column, with nothing merged or inferred.

Some details are deliberate:

- **Northwind Holdings** has two records (`E02`, `E03`) with different names and one LEI. Its latest action sits on the other system's record.
- **Halden Bank** has a RESEARCH record (`E17`) that puts it in Luxembourg, while its RATINGS record says Germany. By the local rule, RESEARCH holds for country.
- **Brindle Capital** (`E16`) is a QA test record, with rating actions that look real.
- **Valdoria's** Country Ceiling sits in the same table as the ratings.
- **Marlow Utilities'** actions are out of date order.
- **Instruments** pay in local codes (`XVD`, `CVK`), and one has only an expected rating (`EX`).

The `executed` condition gets different tables, written by `execute.py`: one row per entity with its records listed, ratings with the dates they held, each instrument with whose risk it carries, the ceilings, and every entity's ancestors.
