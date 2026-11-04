# Right for the right reason?

Answers graded correct by code, with their reasoning checked by an LLM against what each question tests.

| Condition | Correct answers checked | Sound | Unsound | Unclear |
|---|---|---|---|---|
| `csv` | 200 | 156 | 18 | 26 |
| `csv+markdown` | 235 | 210 | 6 | 19 |

## Unsound and unclear

- **Q3/csv+markdown/2** (unclear): Cites the instrument's BB+ rating directly, with no mention of the subordination notching; likely correct but the reasoning is thin.
- **Q3/csv+markdown/4** (unclear): Gives BB+ and speculative grade but never mentions subordination or notching below the issuer.
- **Q3/csv+markdown/5** (unsound): Gives the instrument rating BB+ but does not invoke the issuer-versus-instrument notching; it only says BB+ is speculative, with no subordination reasoning.
- **Q3/csv/1** (unclear): Gives BB+ from an instrument action but never states the issuer-vs-instrument notching; the A23/A07 ordering is odd.
- **Q3/csv/2** (unclear): Traces action history to BB+ but doesn't mention subordination notching.
- **Q3/csv/3** (unsound): Reads the rating from the instrument's own downgrade without addressing issuer-versus-instrument notching; unclear that BB+ is applied as the notch rule.
- **Q3/csv/4** (unsound): Cites A23 BBB assignment and BB+ downgrade for the instrument, but no notching from the issuer is shown; the note's rating is taken from instrument actions, which is plausible but the BBB-to-BB+ path is unverified and inconsistent with a one-step subordinated notch reasoning.
- **Q3/csv/5** (unclear): Cites downgrade to BB+ but doesn't address issuer versus subordinated notching.
- **Q8/csv/1** (unclear): States RD for E08 but doesn't address WD exclusion or whether the status held on 1 Oct 2026.
- **Q11/csv/1** (unsound): Treats A36 as the latest by ID/order though the file is out of date order; and 'only placed on watch' reasoning is shaky, though the date-based result is correct by luck.
- **Q11/csv/3** (unsound): Cites A36 on 2024-09-30 as a downgrade, which would give a rating below BBB+ at 2025-06-01; the reasoning on dates and ratings is inconsistent with A-→BBB+ and hints at guesswork.
- **Q11/csv/5** (unclear): Doesn't say it handled out-of-order file rows; it cites dates, which is consistent with sorting by date.
- **Q12/csv/3** (unclear): Only cites A34 without showing the date comparison against the later downgrade.
- **Q15/csv/2** (unsound): Reaches A- via assignment before the 2026 downgrade, which is right, but the duplicate-entity claim based on LEI is an unstated convention that is unrelated to the date rule.
- **Q16/csv+markdown/2** (unsound): Cites A33 as the latest affirmation at BBB+ but A33 is dated after A36 only per Q18 as 2026; reasoning is thin yet consistent. Minor: it treats the Watch as irrelevant without addressing A35.
- **Q16/csv/2** (unsound): States BBB+ for Marlow, contradicting the earlier answers where its rating was A- in 2024 and downgraded once; rating levels are inconsistent.
- **Q18/csv+markdown/1** (unclear): Says E06 placed on RWN by A17 but never shows the Watch persisting to 1 Oct 2026; also E14 clearing is reasoned but E06 not checked for later resolution.
- **Q18/csv+markdown/4** (unsound): Claims affirmation A33 cleared the Watch A35, but A35 is dated 2025-11-20 while the question concerns the 2026 affirmation; ordering and the cited action are muddled, so the Watch-ended reasoning is inconsistent with the other answers (A33 was cited as the affirmation in Q13/Q16 and A35 is later than A36).
- **Q19/csv+markdown/3** (unclear): Names E01 and E09 and sources, but does not show the outlooks were still Negative; the E06 reasoning is only that the outlook is blank.
- **Q19/csv/2** (unclear): Only cites the source actions without explaining that outlooks come from affirmations or the status on the date.
- **Q19/csv/3** (unclear): Only lists entities and actions without explaining the outlook state at the date.
- **Q19/csv/4** (unclear): Just cites actions without explaining how the outlooks were derived from affirmations.
- **Q21/csv+markdown/5** (unclear): Gives only the value with no reasoning shown.
- **Q22/csv+markdown/5** (unclear): Gives only the value E08, with no reasoning on RD versus WD.
- **Q22/csv/1** (unclear): States RD as the reason for E08 but doesn't address WD, so it's unclear whether the RD/WD distinction was applied.
- **Q22/csv/4** (unclear): Says RD is default but does not address WD or confirm other entities were excluded.
- **Q23/csv+markdown/1** (unclear): Cites A04 only; does not state it is the short-term rating on a separate scale.
- **Q23/csv/2** (unclear): Gives the value and action ID only, without showing it's the short-term rating type.
- **Q23/csv/4** (unclear): Gives only the value and a citation, with no reasoning about rating type.
- **Q23/csv/5** (unclear): Gives only the value and an action ID, with no sign it picked the short-term rating type or the latest one.
- **Q25/csv+markdown/4** (unclear): Lists instrument ratings, but I03 is rated A 'via the E02 guarantee', which hints at issuer-derived rating rather than its own.
- **Q26/csv+markdown/1** (unclear): Cites A40 only; does not show it is the local-currency rating rather than foreign.
- **Q26/csv/4** (unclear): Gives only the value and a citation, with no reasoning about currency basis.
- **Q26/csv/5** (unclear): Gives only a value and a citation, with no sign it chose the local-currency rating.
- **Q27/csv+markdown/1** (unclear): Cites A42 only; no reasoning that it is the instrument rating below the issuer.
- **Q27/csv/4** (unclear): Gives only the value and a citation, with no reasoning about instrument versus issuer.
- **Q27/csv/5** (unclear): Gives only a value and a citation, so it is unclear whether it used the note's rating rather than the issuer's.
- **Q28/csv/5** (unclear): Gives only a value and a citation, with no sign it separated the rating from the ceiling.
- **Q30/csv/3** (unclear): Names entities and ratings but does not show E05/E15 are in countries with ceilings; the claim 'only VD and CV' is asserted.
- **Q31/csv+markdown/3** (unclear): States only the conclusion with no comparison; the ceiling check isn't shown.
- **Q31/csv+markdown/4** (unclear): States the conclusion without showing the comparison against ceilings.
- **Q31/csv+markdown/5** (unclear): Gives only 'No', with no reasoning.
- **Q31/csv/2** (unclear): Concludes no exceedance but does not show the local-currency or sovereign cases; thin reasoning.
- **Q31/csv/3** (unclear): Asserts no FC rating exceeds its ceiling without showing the comparison.
- **Q33/csv+markdown/4** (unsound): Answer says E10 is guarantor and parent, but the test is parent vs ultimate parent; the reasoning never distinguishes roles, only cites guarantee and rating.
- **Q35/csv+markdown/1** (unsound): Counts 3 entities, but lists E09, E10 and E11 with E17 as a duplicate; the count is right but it relies on dedup of E17, which is acceptable. Reasoning matches membership by parent links, so it holds.
- **Q39/csv+markdown/4** (unclear): Cites affirmation A09 but does not state it sits on the other record or resolve identity.
- **Q39/csv+markdown/5** (unclear): Cites actions A08, A09 but doesn't say the latest action is on the other record or how identity was resolved.
- **Q39/csv/2** (unclear): Bare value with no reasoning; cannot tell whether the other record's latest action was used.
- **Q39/csv/4** (unclear): Gives only citations and the rating, with no sign that the action on the other duplicate record was used.
- **Q40/csv+markdown/5** (unsound): Says E10 is domiciled in LU, not DE, yet the rule makes Halden LU and the stated list excludes it; also the reasoning mentions DE oddly, not matching GB; Pellam/withdrawal handling is only partly explained.
- **Q43/csv+markdown/2** (unclear): Gives E10 = E17 but never says the research record's country overrides the ratings record's.
- **Q44/csv/1** (unsound): Guesses XVD is Valdoria's local currency and admits the data does not define the code.
- **Q44/csv/2** (unsound): Admits XVD as Valdoria's currency is inferred, not defined in data; a guessed convention.
- **Q44/csv/3** (unsound): Infers local currency from a rating match, hedged with 'probably', rather than from XVD being the Valdorian dollar; it says the data doesn't define XVD.
- **Q44/csv/4** (unsound): Infers that XVD is Valdoria's currency from the code, a convention the data admits it doesn't define.
- **Q44/csv/5** (unsound): Infers XVD as Valdoria's currency from how it looks and hedges with 'probably'; the code mapping isn't confirmed from data.
- **Q45/csv/3** (unsound): Reaches 'no' via hedged local-currency inference ('appears') without establishing XVD as local currency.
- **Q47/csv/1** (unsound): Cites expiry, not the expected-rating (EX) not being a rating; different reasoning than tested rule.
- **Q47/csv/3** (unsound): Reasons from an expiry rather than that the expected (EX) rating is not an assigned rating.
- **Q47/csv/4** (unsound): Reaches 'none' by treating EX as expired, an assumption; the test is that an expected rating is not a rating until assigned.
- **Q47/csv/5** (unsound): Misreads EX as 'expired'; it is an expected rating, which isn't a rating until assigned.
- **Q48/csv+markdown/1** (unclear): States I01-I07 rated and I08 not, but doesn't show that the EX exclusion or the 1 Oct 2026 dating drove the count.
- **Q48/csv+markdown/2** (unclear): Excludes I08 but does not say it is because the rating is only expected, and does not address the date.
- **Q48/csv+markdown/5** (unclear): Gives 7 (I01-I07) and implies I08's expected rating is excluded, but never states the rule or shows why the others held ratings on that date.
- **Q48/csv/1** (unclear): States I01-I07 and I08 expired without saying the expected rating is excluded; reasoning thin.
- **Q48/csv/3** (unclear): Gives only a list I01–I07 without saying why I08's expected rating is excluded or how the date was applied.
- **Q48/csv/4** (unsound): Says I08 is 'no longer rated' as if it lapsed, not because the expected rating never counts; reasoning is about the wrong rule.
- **Q48/csv/5** (unsound): Excludes I08 for the wrong reason (expired rather than an expected rating that doesn't count).
