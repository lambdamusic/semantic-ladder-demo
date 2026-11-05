# Research analytics: a teaching ontology

Works, authors, institutions, sources, authorships, citations and the codes the data uses, each with a definition that states what it means and how to count it. Invented for an experiment; not a model of any real bibliographic database.

## Classes

### Work

A record of something published: an article, review, preprint, editorial, erratum or piece of paratext (work type). Not every work is research output. A research work is a work that (1) is not a test record (see Staging (STG)), (2) is of a research type: an article (ART), a review (REV), a supplement article (SUP) or a preprint (PPR), (3) is not retracted (retracted), and (4) did not appear in a delisted source (Delisted (K0)). Editorials, errata and paratext are never research output. A preprint and its published version (version of) are two records of one research work and count once, under the published version (its year and its source). Every count of works means research works, and citations are counted to research works, unless a question says otherwise.

### Author

An author record: one person as one source spelled them. A person is identified by their ORCID (ORCID), not by their name or record ID. The same person can appear as several author records with differently spelled names: records with the same ORCID are the same person, and every work recorded against any of them is that person's. Two records with the same name and different ORCIDs are different people. A record with no ORCID is a person of its own.

### Institution

An organisation that authors are affiliated with: a university system, university, lab, company, government body or affiliated institute (institution type). Institutions form a hierarchy through parent: a lab can sit under a centre, under a university, under a university system. A work credited to a unit is also credited to every institution above it, to any depth, so counting an institution's works means counting the works of the institution and all its units, each work once. The exception is an affiliated institute (Affiliated institute (AFF)): its parent link does not make it a unit.

### Source

Where a work appeared: a journal or a repository (source type).

### Authorship

One author's place on one work, and one of the institutions they gave for it: one record per author, work and affiliation. An author who gave two affiliations on a work has two authorship records for it, with the same author position and different affiliation sequence. Which one counts is set by affiliation sequence.

### Citation

One work citing another: citing work lists cited work among its references. A citation happens in the citing work's year. A work's citation count is the number of distinct works, of any type, that cite it, leaving out test records (Staging (STG)) and retracted works. A work citing both a preprint and its published version is one citation of that research work. Citation counts for an author, institution or country add up the counts of their research works. When citations are rolled up to the citing side (which institution or country cites another most), each citing work counts once for each institution credited on it, however many of its authors are from that institution. A self-citation depends on the level: an author self-citation is one where the citing and cited works share at least one author (the same person, whatever the record); an institution self-citation is one where they share a credited institution at the level asked about; a country self-citation is one where they share a country of credited institutions. Each level includes the one below it, so the three are different counts. A citation window counts only the citations made in the cited work's publication year and a given number of years after it, so that older and newer works are compared over the same span.

## Properties

### name (CSV column `name`)

The name of an institution, author or source as the record spells it. Names are not identifiers: the same person can be spelled differently, and different people can share a name.

### ROR ID (CSV column `ror`)

The institution's Research Organization Registry identifier (invented here).

### country (CSV column `country`)

ISO code of the country where the institution is. A work's countries are the countries of the institutions credited on it (see affiliation sequence), not of every affiliation listed.

### institution type (CSV column `type`)

What kind of institution it is: a concept of the scheme Institution types.

### parent (CSV column `parent_id`)

The institution this one is a unit of. Follow it upwards, to any depth, to find the institutions a work is also credited to; the ultimate parent is the institution at the top of the chain, the one with no parent. For an affiliated institute (Affiliated institute (AFF)) the link records an agreement, not membership: do not follow it.

### ORCID (CSV column `orcid`)

The person's ORCID identifier (invented here): the identifier that says which person an author record stands for. Same ORCID, same person.

### ISSN (CSV column `issn`)

The journal's ISSN (invented here). Repositories have none.

### source type (CSV column `type`)

Whether the source is a journal or a repository: a concept of the scheme Source types.

### tier (CSV column `tier`)

The source's tier on this dataset's own journal list: a concept of the scheme Journal tiers. The tiers count upwards: K3 is the highest tier and K1 the lowest; K0 is not a tier but a delisting. Repositories have no tier.

### title (CSV column `title`)

The work's title. A preprint and its published version often share a title; two works with the same title are not the same work unless version of links them.

### publication year (CSV column `year`)

The year the work was published. A citation's year is the citing work's publication year.

### work type (CSV column `type`)

What kind of work it is: a concept of the scheme Work types. It decides whether the work is research output (see Work).

### source (CSV column `source_id`)

The journal or repository the work appeared in.

### DOI (CSV column `doi`)

The work's DOI (invented here). A preprint and its published version have different DOIs, though they are one research work.

### version of (CSV column `version_of`)

Set on a preprint whose published version is also in the data: it names that published version. The two records are one research work, counted once, under the published version; the authors, institutions and citations of either record belong to that one work.

### retracted (CSV column `is_retracted`)

True if the work has been retracted. A retracted work is not research output: leave it out of every count of works, and its citations out of every count of citations.

### record source (CSV column `record_source`)

The system the work record was loaded from: a concept of the scheme Record sources.

### work (CSV column `work_id`)

The work the authorship is on.

### author (CSV column `author_id`)

The author record: see Author for which person it stands for.

### author position (CSV column `author_position`)

The author's place in the byline, from 1. The number of a work's authors is the number of distinct people in its byline.

### institution (CSV column `institution_id`)

An institution the author gave on this work.

### affiliation sequence (CSV column `affil_seq`)

The order in which the author listed their affiliations on this work, from 1. House rule: when an author lists several affiliations on one work, the work is credited only to the affiliation listed last, the one with the highest sequence number, for that author; the others are ignored in every count. With one affiliation, that one is credited. Under full counting, a work counts once for each institution credited on it (and for the institutions above it). Under fractional counting, a work is split equally among its authors (distinct people), and each author's share goes to the one institution credited for them, and so to its country; an institution's fractional count adds up the shares of its own authors and its units' authors.

### citing work (CSV column `citing_work_id`)

The work that makes the citation.

### cited work (CSV column `cited_work_id`)

The work that is cited.

## Codes

The codes as they appear in the data, grouped by list.

### Work types

- **ART**, Research article: A peer-reviewed research article. Research output.
- **REV**, Review article: A peer-reviewed article that surveys a field. Research output.
- **SUP**, Supplement article: In this dataset, SUP does not mean supplementary material. It is a full, peer-reviewed research article published in a supplement issue of a journal, such as a proceedings supplement. It is research output and counts exactly like an article (ART).
- **PPR**, Preprint: A version posted to a repository before or without peer review. Research output, but if its published version is in the data (version of), the two are one research work, counted once.
- **EDT**, Editorial: An editor's introduction or opinion piece. Not research output.
- **ERR**, Erratum: A correction notice for an earlier work. Not research output, and not a new version of the work it corrects.
- **PTX**, Paratext: Front matter, issue information, tables of contents and the like: published with a journal issue, but not a contribution. Not research output.

### Institution types

- **SYS**, University system: A group of universities under one governing body. Its works are the works of all its universities and their units.
- **UNI**, University: A university or college.
- **LAB**, Laboratory, centre or institute: A research unit inside its parent institution. Its works are also its parent's works, and its parent's parent's, to the top.
- **AFF**, Affiliated institute: A legally independent institute linked to a university by an agreement. Its parent link records that agreement and nothing more: an affiliated institute is not a unit of its parent, is not part of the parent's system, and its works are never credited to the parent or to anything above it. Its ultimate parent is itself.
- **CO**, Company: A company.
- **GOV**, Government body: A government agency or laboratory.

### Source types

- **JOU**, Journal: A peer-reviewed journal, including its proceedings or supplement issues.
- **REP**, Repository: A preprint server or other repository.

### Journal tiers

- **K3**, Tier K3, the highest: The highest tier: the journals the list ranks first. A higher number is a higher tier, so K3 ranks above K2, and K2 above K1.
- **K2**, Tier K2, the middle: The middle tier: below K3, above K1.
- **K1**, Tier K1, the lowest: The lowest tier that is still listed: below K2.
- **K0**, Delisted source: Not a tier: a source removed from the list for failing its review of editorial practice. Works that appeared in a K0 source are not research output, whatever their type, and are left out of every count of works and citations.

### Record sources

- **FEED**, Bibliographic feed: Loaded from the external bibliographic feed.
- **CRIS**, Institutional research information system: Entered by an institution in its own research information system. As good as a feed record.
- **STG**, Staging load: Test records, loaded into staging to check the import and never removed. They describe no real work: ignore an STG work, its authorships and every citation it makes, in every count.
