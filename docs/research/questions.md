Each question looks like a lookup, and each has an obvious wrong answer. Only the question text is sent to the model, which must give its answer as a typed JSON field, except Q47 and Q48, which ask why and are graded against a checklist. The trap and the key are never sent. Keys are computed from the data, and each is checked against one written by hand, so the two can't silently disagree.

## The implicit meanings

| Implicit meaning | What it says | Questions |
|---|---|---|
| **Who is who** | One person can have several author records, matched by ORCID; one name can belong to different people | Q1 to Q7 |
| **Institution hierarchy** | A lab's works are also its centre's, its university's and its system's, each work counted once | Q8 to Q11 |
| **Counting method** | Full counting gives each institution on a work the whole work; fractional counting splits it by author. The two can rank institutions differently | Q12 to Q14, Q47 |
| **Document types** | Editorials, errata and front matter aren't research output | Q15 to Q17 |
| **Versions** | A preprint and its published version are one work, and a citation of either is a citation of that work | Q18 to Q21 |
| **Citation windows** | A citation's year is the citing work's year, and an older work has had longer to be cited | Q22, Q23 |
| **Retractions** | A retracted work isn't research output, and its citations don't count | Q24 to Q26 |
| **Citations at several levels** | Citations roll up to institutions, each citing work counted once, and self-citation means something different for an author, an institution and a country | Q27 to Q30 |
| **Citation chains** | A work two hops away cites a work that cites the first, and each is counted once | Q31, Q32 |

## The local meanings

| Local rule | Questions |
|---|---|
| `STG` records are test data: they and their citations are ignored | Q33, Q34 (also Q11, Q16, Q25, Q31) |
| `SUP` is a supplement article, which is research output, not supplementary material | Q34 to Q36 |
| When an author lists several affiliations on a work, only the one listed last is credited | Q37, Q38, Q45 (also Q48) |
| The tiers count upwards: `K3` is the highest, `K1` the lowest | Q39 to Q41 |
| `K0` isn't a tier but a delisting: works in a delisted source aren't research output | Q42, Q43 (also Q7) |
| An affiliated institute (`AFF`) is not a unit of its parent: its parent link is an agreement, not membership | Q44, Q46 (also Q48) |

"Research work" is the dataset's own term, so some answers given without the ontology, such as counting editorials, could be called a reasonable reading rather than an error. A review found they're mostly the questions that depend on the local rules anyway (see the [conclusions](/conclusions/#5-does-the-domain-matter)).
