An invented credit-ratings world: issuers, the bonds they issue, and the rating actions on both, as an analyst's extract from two internal systems would come. The codes (`LTIDR`, `AF`, `RWN`) are left cryptic, and nothing in the files says what they stand for.

The 48 questions, asked of every credit dataset, are of two kinds (the ownership-paths dataset adds [13 more](#ownership-paths), 61 in all):

- **Implicit meanings** (Q1 to Q40): what any credit analyst knows without saying. A rating holds from one action to the next. An outlook isn't a rating change. A withdrawal isn't a default. A Country Ceiling caps foreign-currency ratings. A guaranteed note carries the guarantor's risk. Two records with one LEI are one entity. A strong model gets many of these right from general knowledge.
- **Local meanings** (Q41 to Q48): rules this dataset sets for itself, stated only in the ontology. QA records are test data. Domicile comes from the RESEARCH system, and names and parents from RATINGS. `XVD` and `CVK` are local currency codes. `CO` is a credit opinion, not a rating. `EX` is an expected rating, not yet assigned. No model can know these without being told, which is where an ontology should earn its place.

One ontology and one question bank are asked of three datasets. Each dataset computes its own answer keys from its own data.

## The datasets

### The base data

19 entity records (two of them sovereigns), 8 instruments and 47 rating actions, every one designed by hand so that each question has its point. Small enough to read in full, it's where the ladder was first tested.

### At 300 issuers

The base records plus 300 invented issuers that repeat the same traps many times over: duplicate RESEARCH records, QA test records, group chains, finance subsidiaries, local currencies, expected ratings, withdrawals, Watches, and rows out of date order. That makes 370 entity records, 115 instruments and 787 rating actions. The same 48 questions now need counting and joining across many records, which is where reading the data should start to fail and writing queries should pay off. `scale.py` builds it from a fixed seed.

### Ownership paths

Does the store need to be a graph? With one or two levels of parent, the data can't show a graph's strength. This dataset is the 300-issuer data plus six invented groups four to six levels deep, built so that answering means walking parent and guarantee links:

- in the largest group, a parent link names a **RESEARCH record** of the parent, so the chain goes on from that entity's RATINGS record;
- a RESEARCH record gives a **stale parent** in another group, which the RATINGS record overrules;
- a member is **in Valdoria by its RESEARCH record**, which holds for country, while RATINGS puts it in the Netherlands;
- a note is **guaranteed by another group's top entity**;
- a **QA test record** sits under one group's top, with a rating of its own.

It asks the 48 questions plus 13 that follow links (Q49 to Q61). `paths.py` builds it, and the designed entities' IDs go in `anchors.json`.

## The terms, explained

What the credit terms mean, in plain English, with the invented records as examples. This is for people: the model is never given it. What the model can be given is the [ontology](/domains/credit/ontology/).

### Instruments

An instrument is a specific piece of debt that a company has sold to investors, such as a
bond or note. It is the thing being rated, as distinct from the company that owes the money.

"Kestrel Energy 6.25% notes due 2031" (`I02`) breaks down as:

- **Issuer:** Kestrel Energy (`E01`), which borrowed the money and owes the payments.
- **Coupon:** 6.25% is the annual interest paid to investors.
- **Maturity:** 30 September 2031, when the money must be repaid.
- **Currency:** GBP, the currency it pays in.
- **Seniority:** subordinated (`SUB`), so if Kestrel fails, these investors are repaid after
  the senior ones.

The data has four instruments:

| ID | Instrument | Issuer | Seniority | Currency | Guarantor |
|---|---|---|---|---|---|
| `I01` | Kestrel Energy 4.50% due 2030 | `E01` | Senior unsecured | GBP | none |
| `I02` | Kestrel Energy 6.25% due 2031 | `E01` | Subordinated | GBP | none |
| `I03` | Northwind Finance 3.75% due 2030 | `E04` | Senior unsecured | EUR | `E02` |
| `I04` | Valdoria Telecom 5.00% due 2029 | `E05` | Senior unsecured | USD | none |

One company can have many instruments, each with its own rating. That rating starts from
the issuer's and moves up or down depending on the terms:

- **Seniority:** Kestrel is rated BBB, but its subordinated note `I02` is BB+, below
  investment grade. So "is Kestrel investment grade?" and "is this note investment grade?"
  get different answers ([Q3](/domains/credit/questions/#Q3)).
- **Guarantees:** Northwind Finance's note `I03` is backed by `E02`, so investors are really
  taking that guarantor's risk, not the issuer's ([Q5](/domains/credit/questions/#Q5)).
- **Currency:** `I04` pays in USD, so it is exposed to the risk that Valdoria stops money
  leaving the country ([Q6](/domains/credit/questions/#Q6), and see [Country Ceilings](#country-ceilings) below).

A knowledge graph therefore has to keep issuers and instruments as separate, linked things:
"the rating of X" is ambiguous until you say which one.

### Instruments, notes and bonds

A note is one kind of instrument. "Instrument" is the general term for any tradable financial
contract, and a note is a specific type of debt instrument.

| Term | What it is |
|---|---|
| **Instrument** | The umbrella term: bonds, notes, loans, shares, derivatives and so on |
| **Debt instrument** | An instrument where someone owes money and must repay it |
| **Bond** | Debt sold to investors, usually long-term |
| **Note** | Much the same as a bond, usually with a shorter term |

The line between a note and a bond is mostly convention. A note is often described as running
for about 1–10 years and a bond for longer, but it varies by market and issuer. The legal
terms matter far more for credit risk: seniority, guarantees and currency.

All four instruments in the data happen to be notes, but `lad:Instrument` is defined as "a
debt instrument, such as a bond or note", so a bond would fit without any change.

### Country Ceilings

A Country Ceiling is a cap on the foreign-currency ratings of entities based in a country.
It is written on the same scale as a rating, but it is not a judgement of anyone's
creditworthiness. In the data, the BB on the Republic of Valdoria (`A12`, type `CC`) is its
Country Ceiling.

**What it captures:** the risk that a government stops money being converted or sent abroad,
for example through capital controls in a currency crisis. Then even a healthy company
couldn't pay its foreign debts, because it couldn't get the dollars out. This is called
transfer and convertibility risk.

**Why currency matters:** the risk only applies to paying in foreign currency.

- **Local currency:** a Valdorian company paying a debt in Valdorian money doesn't need to
  convert anything or send it abroad, so capital controls don't stop it. The ceiling doesn't
  apply.
- **Foreign currency:** a Valdorian company paying dollars has to get through that
  restriction, however strong its business is. The ceiling applies.

Valdoria Telecom (`E05`) shows this directly:

| Action | What is rated | Rating | Ceiling applies? |
|---|---|---|---|
| `A13` | Issuer, local currency | **BBB-** | No, so this reflects the company's own strength |
| `A14` | Issuer, foreign currency | **BB** | Yes, capped at the ceiling |
| `A15` | `I04`, its USD note | **BB** | Yes, because it pays in dollars |

So the same company is investment grade in local currency and below investment grade in
foreign currency. Nothing about the business differs between the two; the gap comes entirely
from the country. [Q6](/domains/credit/questions/#Q6) asks why the two ratings differ, and [Q10](/domains/credit/questions/#Q10) has no single answer until you
say which rating you mean.

Two distinctions are easy to mix up:

- **The ceiling isn't the sovereign's own rating.** Valdoria the government would have its
  own issuer rating, which is a separate thing and could be a different level. The data
  doesn't include one, as `VD` only carries the ceiling. In real data, ceilings often sit
  somewhat above the sovereign's foreign-currency rating; check an agency's published
  criteria before relying on that.
- **It's a general cap, not an absolute one.** The ontology says foreign-currency ratings are
  "generally no higher than the ceiling". Real exceptions exist, such as a company with
  substantial earnings or support from abroad.

The rule links three things: an entity's country, the currency basis of a rating, and a
separate country-level fact. No row states that link, so a model reading only the CSV has to
bring it from its own training.
