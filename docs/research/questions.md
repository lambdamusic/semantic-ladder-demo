Each question looks like a lookup, and each has an obvious wrong answer. Only the question text is sent to the model, which must give its answer as a typed JSON field, except [Q47](#Q47) and [Q48](#Q48), which ask why and are graded against a checklist. The trap and the key are never sent. Keys are computed from the data, and each is checked against one written by hand, so the two can't silently disagree.

## The implicit meanings

| Implicit meaning | What it says | How the data sets it | Questions |
|---|---|---|---|
| **Who is who** | One person can have several author records, matched by ORCID; one name can belong to different people | A01, A02 and A03 are Mara Ellison (one ORCID); A04, also "M. Ellison", is someone else at Kesting; A05 and A06 are two Jonas Brandts. By record, Priya Ramanathan (A07, 4 works) beats each Mara record; merged, Mara has 5 ([Q6](#Q6)). [Q7](#Q7) combines identity, versions, document types and the delisted source | [Q1](#Q1) to [Q7](#Q7) |
| **Institution hierarchy** | A lab's works are also its centre's, its university's and its system's, each work counted once | Ultimate parent three levels up ([Q8](#Q8)); a university's count includes its labs ([Q9](#Q9)); a system's count includes both universities, with W12 shared between them counted once ([Q10](#Q10)) | [Q8](#Q8) to [Q11](#Q11) (also [Q38](#Q38), [Q44](#Q44), [Q46](#Q46)) |
| **Counting method** | Full counting gives each institution on a work the whole work; fractional counting splits it by author. The two can rank institutions differently | Kesting 2024: full 3, fractional 2. Rostval 2024: full 4, fractional 1 (four works, one author of four from Rostval on each), so the ranking flips ([Q13](#Q13)). GB 2024: full 7, fractional 6. All fractional answers are whole numbers by design | [Q12](#Q12) to [Q14](#Q14), [Q47](#Q47) |
| **Document types** | Editorials, errata and front matter aren't research output | Editorials (W04, W76), an erratum (W05), paratext (W09, W10) | [Q15](#Q15) to [Q17](#Q17) |
| **Versions** | A preprint and its published version are one work, and a citation of either is a citation of that work | W02 is the preprint of W03 and W42 of W31 (`version_of`); W18 is a preprint with no published version; W15 cites both W02 and W03 | [Q18](#Q18) to [Q21](#Q21) |
| **Citation windows** | A citation's year is the citing work's year, and an older work has had longer to be cited | W30 (2019) has 5 citations in all but 1 within its year plus two; W31 (2023) has 4 in all, all within the window | [Q22](#Q22), [Q23](#Q23) |
| **Retractions** | A retracted work isn't research output, and its citations don't count | W23 (Lena Vossberg, Kesting) is retracted and cited once (W39) | [Q24](#Q24) to [Q26](#Q26) |
| **Citations at several levels** | Citations roll up to institutions, each citing work counted once, and self-citation means something different for an author, an institution and a country | Kesting is cited by three single-author Lorvain works and by one Rostval work with four Rostval authors (counted per author, Rostval would win: [Q27](#Q27), [Q28](#Q28)). The sonar paper (W02/W03) is cited by 7 works: author self-citations 2, University of Albury 2, the system 3, GB 4 ([Q29](#Q29), [Q30](#Q30)) | [Q27](#Q27) to [Q30](#Q30) |
| **Citation chains** | A work two hops away cites a work that cites the first, and each is counted once | Two hops from W01: W40 and W41, then W50, W51 and W52, with W51 citing both and a test record W90 left out | [Q31](#Q31), [Q32](#Q32) |

[Q7](#Q7), [Q9](#Q9), [Q11](#Q11), [Q16](#Q16) and [Q25](#Q25) also depend on the local rules: they combine several traps.

## The local meanings

Each rule is stated only in the ontology, and none can be guessed from a code's name or from general conventions.

| Local rule | How the data sets it | Where the ontology states it | Questions |
|---|---|---|---|
| `STG` records are test data: they and their citations are ignored | Works with `record_source` STG (W90 to W92, at Kesting, by A21) describe no real work: they're ignored, with their authorships and the citations they make. With them, W22 would be Kesting's most-cited work (4 citations against W20's 3) | `res:origin-STG`; `res:Work` (condition 1); `res:Citation` | [Q33](#Q33), [Q34](#Q34) (also [Q11](#Q11), [Q16](#Q16), [Q25](#Q25), [Q31](#Q31)) |
| `SUP` is a supplement article, which is research output, not supplementary material | A peer-reviewed article in a supplement issue, counted like an article (W17, W24) | `res:wtype-SUP`; `res:Work` (condition 2) | [Q34](#Q34) to [Q36](#Q36) |
| When an author lists several affiliations on a work, only the one listed last is credited | Only the one with the highest `affil_seq` counts. W70 lists Tessel and then Halloran, so it goes to Halloran; W71 lists Halloran and then Tessel, so it goes to Tessel | `res:affiliationSeq` (also `res:Authorship`, `res:country`) | [Q37](#Q37), [Q38](#Q38), [Q45](#Q45) (also [Q9](#Q9), [Q48](#Q48)) |
| The tiers count upwards: `K3` is the highest, `K1` the lowest | The reverse of the natural guess, where tier 1 would be the best | `res:tier`, `res:tier-K3` to `res:tier-K1` | [Q39](#Q39) to [Q41](#Q41) |
| `K0` isn't a tier but a delisting: works in a delisted source aren't research output | Works in a K0 source (W07, W75) are left out of every count | `res:tier-K0`; `res:Work` (condition 4) | [Q42](#Q42), [Q43](#Q43) (also [Q7](#Q7)) |
| An affiliated institute (`AFF`) is not a unit of its parent: its parent link is an agreement, not membership | Halloran's parent link records an agreement, so its works are never credited to the University of Albury or the system, and its ultimate parent is itself | `res:itype-AFF`; `res:Institution`; `res:parent` | [Q44](#Q44) to [Q46](#Q46) (also [Q9](#Q9), [Q48](#Q48)) |

"Research work" is the dataset's own term, so some answers given without the ontology, such as counting editorials, could be called a reasonable reading rather than an error. A review found they're mostly the questions that depend on the local rules anyway (see the [conclusions](/conclusions/#5-does-the-domain-matter)).
