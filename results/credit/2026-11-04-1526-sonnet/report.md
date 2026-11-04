# credit: claude:sonnet, 2026-11-04 15:26

10 questions, 5 repeats per condition. Correct = 1, partial = ½. Graded by code where a question has a typed key, by claude:sonnet with a checklist otherwise.

## Accuracy

| Condition | Accuracy | 95% interval | Questions unstable across repeats |
|---|---|---|---|
| `csv` | **95%** | 85% to 100% | 0 of 10 |
| `rdf` | **93%** | 79% to 100% | 1 of 10 |
| `rdf+ontology` | **99%** | 97% to 100% | 1 of 10 |
| `csv+ontology` | **96%** | 88% to 100% | 1 of 10 |

## Against `csv`, question by question

| Condition | Difference | 95% interval |
|---|---|---|
| `rdf` | -2 points | -6 to +0 |
| `rdf+ontology` | +4 points | +0 to +12 |
| `csv+ontology` | +1 points | -12 to +15 |

## By question

| Question | Graded by | `csv` | `rdf` | `rdf+ontology` | `csv+ontology` |
|---|---|---|---|---|---|
| Q1 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q2 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q3 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q4 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q5 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q6 | llm | 🟡 🟡 🟡 🟡 🟡 | 🟡 ❌ ❌ 🟡 🟡 | ✅ 🟡 ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q7 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q8 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q9 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ |
| Q10 | code | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ✅ ✅ ✅ | ✅ ✅ ❌ ✅ ❌ |

**The checklist grader agreed with itself** on 19 of 20 answers graded twice.

## Code grading against the old LLM grader

On the questions with typed keys, the two agreed on 170 of 180 answers.

| Condition | Accuracy, code | Accuracy, LLM grader | Unstable, code | Unstable, LLM grader |
|---|---|---|---|---|
| `csv` | 100% | 98% | 0 of 9 | 1 of 9 |
| `rdf` | 100% | 99% | 0 of 9 | 1 of 9 |
| `rdf+ontology` | 100% | 97% | 0 of 9 | 3 of 9 |
| `csv+ontology` | 96% | 96% | 1 of 9 | 2 of 9 |

## Why each miss was marked

**Q6.** Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?

- `csv` run 1: Identifies the BB country ceiling matching the foreign-currency rating (hedged as an inference), but never states that the ceiling caps foreign-currency and not local-currency ratings.
- `csv` run 2: It names the BB country ceiling only as 'consistent with' the gap and says the data states no reason, so it never asserts it as the cause. It says the ceiling caps foreign-currency but does not say local-currency ratings are exempt.
- `csv` run 3: Links FC rating to the BB country ceiling as consistent, but doesn't assert it as the cause or state that the ceiling caps FC and not LC ratings.
- `csv` run 4: Links the FC rating of BB to the Country Ceiling of BB as a possible cause but hedges, and never says the ceiling caps FC and not LC ratings.
- `csv` run 5: Links the BB foreign-currency rating to the BB country ceiling as a consistent cap, but hedges it as inference and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 1: Links the BB sovereign 'CC' rating to the FC rating and infers a country ceiling, but hedges it as an unconfirmed inference and never states that the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 2: Does not name the Country Ceiling (BB) as the cause or say it caps foreign-currency ratings; it states the data gives no reason.
- `rdf` run 3: Does not name the Country Ceiling (BB) as the cause or say it caps foreign-currency but not local-currency ratings; it says the data doesn't state the reason and only speculates about a sovereign-related cap.
- `rdf` run 4: Mentions the sovereign BB 'CC' record but declines to confirm it as the cause and never says the ceiling caps foreign-currency but not local-currency ratings.
- `rdf` run 5: Hedges that the BB sovereign 'CC' rating may be a country ceiling but doesn't confirm it as the cause, and never says the ceiling caps foreign-currency but not local-currency ratings.
- `rdf+ontology` run 2: Identifies the BB Country Ceiling and that FC ratings are capped by it, but hedges that no record states it as the cause, so it doesn't clearly name the ceiling as the cause.

**Q10.** Is Valdoria Telecom investment grade?

- `csv+ontology` run 3: investment_grade: expected depends, got no
- `csv+ontology` run 5: investment_grade: expected depends, got no

