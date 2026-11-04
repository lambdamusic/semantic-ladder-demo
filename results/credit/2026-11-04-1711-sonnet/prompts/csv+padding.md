<!-- system: You answer questions about a credit-ratings dataset. Use only the data you are given and what it tells you about its own meaning. If a question is ambiguous, or the data cannot settle it, say so. Be concise. -->

## The data

### entities.csv
```csv
entity_id,name,lei,country,entity_type,parent_id,source_system
E01,Kestrel Energy plc,7245002OOPBG04092E43,GB,CORP,,RATINGS
E02,Northwind Holdings plc,213800PHEIYNJMHTDV74,GB,CORP,,RATINGS
E03,NORTHWIND HLDGS,213800PHEIYNJMHTDV74,GB,CORP,,RESEARCH
E04,Northwind Finance BV,213800LA5RYJLGXV2T85,NL,FINSUB,E02,RATINGS
E05,Valdoria Telecom SA,391200LESH03LMOY2U61,VD,CORP,,RATINGS
E06,Orrin Bank AG,549300AMVE3VRVG7HK43,DE,BANK,,RATINGS
E07,Pellam Retail Ltd,969500B6IUACELPI2291,GB,CORP,,RATINGS
E08,Saxby Shipping SA,969500KOTZ1JFIZSG796,GR,CORP,,RATINGS
VD,Republic of Valdoria,,VD,SOV,,RATINGS
E09,Halden Group plc,815600ASM9EHDG931T89,GB,CORP,,RATINGS
E10,Halden Bank AG,391200QYPVFF2O9K2039,DE,BANK,E09,RATINGS
E11,Halden Leasing SA,549300XBZH4ULO9MQV55,FR,FINSUB,E10,RATINGS
E12,Halden Foods Ltd,213800IJDL4OJ4DG5T19,GB,CORP,,RATINGS
E13,Orrin Bancorp Inc,815600O8X8K2F154N214,US,BANK,,RATINGS
E14,Marlow Utilities plc,3912005AH2C1I9YF8106,GB,CORP,,RATINGS
CV,Republic of Corvenia,,CV,SOV,,RATINGS
E15,Corvenia Power SA,213800PBQVHVBBH6GV02,CV,CORP,,RATINGS
E16,Brindle Capital Ltd,5493003Z3PXXR7KNFM81,GB,CORP,,QA
E17,HALDEN BANK,391200QYPVFF2O9K2039,LU,BANK,,RESEARCH
```

### instruments.csv
```csv
instrument_id,description,issuer_id,guarantor_id,seniority,currency,maturity
I01,Kestrel Energy 4.50% notes due 2030,E01,,SU,GBP,2030-03-15
I02,Kestrel Energy 6.25% notes due 2031,E01,,SUB,GBP,2031-09-30
I03,Northwind Finance 3.75% notes due 2030,E04,E02,SU,EUR,2030-05-01
I04,Valdoria Telecom 5.00% notes due 2029,E05,,SU,USD,2029-11-20
I05,Halden Leasing 2.90% notes due 2028,E11,E10,SU,EUR,2028-06-30
I06,Corvenia Power 7.10% notes due 2032,E15,,SUB,USD,2032-02-15
I07,Valdoria Telecom 4.25% notes due 2027,E05,,SU,XVD,2027-08-31
I08,Corvenia Power 6.00% notes due 2034,E15,,SU,USD,2034-09-01
```

### rating_actions.csv
```csv
action_id,date,rated_id,rating_type,ccy_basis,action,rating,outlook,watch,comment
A01,2024-03-12,E01,LTIDR,FC,AS,A-,STA,,
A02,2025-06-20,E01,LTIDR,FC,DG,BBB,STA,,weaker cash flow after asset sale
A03,2026-02-10,E01,LTIDR,FC,AF,BBB,NEG,,
A04,2026-02-10,E01,STIDR,FC,AF,F2,,,
A05,2024-03-12,I01,INST,,AS,A-,,,
A06,2025-06-20,I01,INST,,DG,BBB,,,
A07,2025-06-20,I02,INST,,DG,BB+,,,
A08,2023-11-01,E02,LTIDR,FC,AS,A,STA,,
A09,2025-09-15,E03,LTIDR,FC,AF,A,POS,,
A10,2023-11-01,I03,INST,,AS,A,,,
A11,2025-09-15,I03,INST,,AF,A,,,
A12,2025-04-01,VD,CC,,AS,BB,,,
A13,2025-04-01,E05,LTIDR,LC,AS,BBB-,STA,,
A14,2025-04-01,E05,LTIDR,FC,AS,BB,STA,,
A15,2025-04-01,I04,INST,,AS,BB,,,
A16,2024-05-01,E06,LTIDR,FC,AS,A-,STA,,
A17,2026-09-03,E06,LTIDR,FC,RW,A-,,RWN,
A18,2024-01-10,E07,LTIDR,FC,AS,BB,STA,,
A19,2026-05-12,E07,LTIDR,FC,WD,WD,,,commercial reasons
A20,2024-06-01,E08,LTIDR,FC,AS,B,STA,,
A21,2026-01-20,E08,LTIDR,FC,DG,CCC,,,
A22,2026-07-08,E08,LTIDR,FC,DG,RD,,,distressed debt exchange completed
A23,2024-03-12,I02,INST,,AS,BBB,,,
A24,2023-05-01,E09,LTIDR,FC,AS,A,STA,,
A25,2026-03-01,E09,LTIDR,FC,AF,A,NEG,,
A26,2023-05-01,E10,LTIDR,FC,AS,A-,STA,,support from parent
A27,2026-04-15,E10,LTIDR,FC,DG,BBB+,STA,,
A28,2023-06-01,I05,INST,,AS,A-,,,
A29,2026-04-15,I05,INST,,DG,BBB+,,,
A30,2024-02-01,E12,LTIDR,FC,AS,BB-,STA,,
A31,2025-08-01,E12,LTIDR,FC,UG,BB,STA,,
A32,2024-07-01,E13,LTIDR,FC,AS,BBB,STA,,
A33,2026-05-01,E14,LTIDR,FC,AF,BBB+,STA,,
A34,2023-01-15,E14,LTIDR,FC,AS,A-,STA,,
A35,2025-11-20,E14,LTIDR,FC,RW,BBB+,,RWN,
A36,2024-09-30,E14,LTIDR,FC,DG,BBB+,STA,,
A37,2024-01-01,CV,CC,,AS,A,,,
A38,2024-01-01,CV,LTIDR,FC,AS,BBB+,STA,,
A39,2024-01-01,CV,LTIDR,LC,AS,A-,STA,,
A40,2024-03-01,E15,LTIDR,LC,AS,A+,STA,,
A41,2024-03-01,E15,LTIDR,FC,AS,A,STA,,
A42,2024-03-01,I06,INST,,AS,A-,,,
A43,2024-04-01,E16,LTIDR,FC,AS,BBB-,STA,,
A44,2026-06-01,E16,LTIDR,FC,DG,BB+,STA,,
A45,2025-04-01,I07,INST,,AS,BBB-,,,
A46,2025-02-01,E11,CO,,AS,BBB,,,
A47,2026-09-01,I08,INST,,EX,A,,,
```

### background.md

# Bond market mechanics: a short glossary

How bonds are priced, quoted, settled and traded. General background on fixed-income markets.

## Prices and yields

### Clean price

The price of a bond without the interest that has built up since the last coupon. Bonds are usually quoted this way, as a percentage of face value, so that the quote does not jump on each coupon date.

### Dirty price

The clean price plus accrued interest: what the buyer actually pays. It rises steadily between coupon dates and drops back when a coupon is paid.

### Accrued interest

The share of the next coupon that the seller has earned by holding the bond since the last coupon date. The buyer pays it to the seller at settlement and receives the full coupon later.

### Yield to maturity

The single discount rate that makes the present value of a bond's remaining payments equal to its dirty price, assuming every payment is made on time and each coupon is reinvested at that same rate.

### Current yield

The annual coupon divided by the clean price. Simple to compute, but it ignores the gain or loss as the price moves to par by maturity.

### Par, premium and discount

A bond trades at par when its price equals its face value, at a premium above it and at a discount below it. A bond whose coupon is above market yields trades at a premium.

## Coupons and schedules

### Coupon

The interest a bond pays, stated as an annual percentage of face value and usually paid annually, semi-annually or quarterly.

### Fixed and floating coupons

A fixed coupon stays the same for the life of the bond. A floating coupon resets each period to a reference rate plus a fixed margin, so its payments follow market rates.

### Zero-coupon bond

A bond that pays no coupons and is sold at a discount to face value. The investor's return is the difference between the purchase price and the amount repaid at maturity.

### Day-count convention

The rule for counting days when computing accrued interest. Common conventions are actual/actual, actual/360 and 30/360, and the choice changes the amount accrued over a period.

### Business-day convention

The rule for moving a payment date that falls on a weekend or holiday: to the following business day, to the preceding one, or to the following one unless that crosses into the next month.

### Record date

The date on which the holder must be registered to receive the next coupon. A bond bought after the record date but before the payment date trades without that coupon.

## Risk and sensitivity

### Duration

The weighted average time until a bond's cash flows are received, weighted by their present values. Longer duration means the price moves more when yields change.

### Modified duration

Duration adjusted for the yield, giving the approximate percentage change in price for a one-percentage-point change in yield.

### Convexity

How much duration itself changes as yields move. Two bonds with the same duration can react differently to large yield changes if their convexity differs.

### Basis point

One hundredth of a percentage point. Yields, spreads and rate changes are usually quoted in basis points.

### DV01

The change in a bond's price for a one-basis-point change in yield, in currency terms. Traders use it to compare and hedge positions of different sizes.

### Spread

The difference between a bond's yield and the yield of a benchmark, such as a government bond of similar maturity or a swap rate. It is quoted in basis points.

### Yield curve

The yields of comparable bonds plotted against their maturities. It usually slopes upward, because investors ask for more to lend for longer; when short yields are above long ones it is called inverted.

## Structures

### Bullet bond

A bond that repays all of its face value in one payment at maturity.

### Amortising bond

A bond that repays part of its face value with each payment, so the amount outstanding falls over time.

### Callable bond

A bond the issuer may repay before maturity, on set dates and at set prices. Investors usually receive a higher coupon in return for this option.

### Puttable bond

A bond the investor may sell back to the issuer before maturity, at set prices on set dates.

### Convertible bond

A bond the holder may exchange for a set number of the issuer's shares. Its price reflects both the bond and the value of that option.

### Sinking fund

A provision that requires the issuer to retire part of an issue each year, by buying bonds in the market or by calling them at par.

### Make-whole call

A call at a price equal to the present value of the remaining payments, discounted at a benchmark yield plus a small spread, so that the investor is compensated for early repayment.

## Issuance

### Primary market

Where new bonds are sold to investors for the first time, usually through a group of banks that arrange and distribute the issue.

### Bookbuilding

The process of collecting investor orders before pricing a new issue. The size of the order book guides the final coupon and the amount sold.

### Reopening

Selling more of an existing bond, with the same coupon and maturity, so that the new bonds trade as one line with the old ones.

### Denomination

The smallest face amount in which a bond can be bought and traded. Large minimum denominations keep an issue to professional investors.

### Prospectus

The document that describes a new issue: the terms of the bonds, the issuer's business and the risks. Investors rely on it when deciding whether to buy.

### Trustee

A party appointed to act for bondholders and to check that the issuer keeps to the terms of the bonds.

### Paying agent

The bank that receives payments from the issuer and passes them to bondholders.

## Trading and settlement

### Secondary market

Where bonds are bought and sold after issue. Most bond trading happens between dealers and investors rather than on an exchange.

### Bid and offer

The prices at which a dealer will buy (bid) and sell (offer) a bond. The difference between them, the bid-offer spread, is a measure of how easy the bond is to trade.

### Settlement date

The date on which the bond and the cash change hands, usually one or two business days after the trade date.

### Clearing system

A central system that holds bonds in electronic form and moves them between accounts on settlement, so that no paper changes hands.

### Repo

A sale of a bond with an agreement to buy it back later at a set price. In effect it is a short-term loan secured on the bond, and the difference between the two prices is the interest.

### Haircut

The amount by which the value of a bond used as collateral is reduced, to protect the lender if the price falls.

### Benchmark bond

A large, frequently traded issue, usually from a government, whose yield is used as a reference for pricing other bonds of similar maturity.

### Index

A basket of bonds chosen by set rules, used to measure the performance of a market and as a target for funds that track it.

## Money and rates

### Reference rate

A published short-term interest rate, such as an overnight rate, that floating coupons, loans and derivatives are set against.

### Swap rate

The fixed rate exchanged for a floating rate in an interest-rate swap of a given maturity. Swap rates form a curve that is widely used to price bonds.

### Real yield

The yield after taking out expected inflation, as shown by bonds whose payments are linked to an inflation index.

### Break-even inflation

The difference between the yield on a conventional bond and on an inflation-linked bond of the same maturity: the inflation rate at which the two would return the same.

### Total return

What an investor earns over a period: coupons received, plus or minus the change in the bond's price, plus any interest earned on reinvesting the coupons.

## Quotes and conventions

### Thirty-seconds

Some government bond prices are quoted in thirty-seconds of a point rather than decimals, so a quote of 99-16 means 99 and a half percent of face value.

### Odd first coupon

A first coupon period that is longer or shorter than the regular ones, because the bond was issued between two regular coupon dates. The first payment is adjusted to match.

### Ex-coupon period

A short period before a coupon date during which a bond trades without the right to the next coupon. In some markets the accrued interest is negative during this period.

### When-issued trading

Trading in a new bond after it has been announced but before it has been issued, with settlement on the issue date.

### Stripping

Separating a bond's coupons and its final repayment into individual zero-coupon securities, each traded on its own.

### Fungible

Interchangeable: bonds of the same line are fungible, so any one can be delivered in place of another.

### Settlement fail

When one side does not deliver the bond or the cash on the settlement date. The trade stays open, and the late party may owe a penalty.

## Funds and portfolios

### Portfolio turnover

The share of a portfolio bought and sold over a year. High turnover raises trading costs, which come out of the fund's return.

### Tracking error

How far a fund's return differs from its benchmark's, measured as the spread of the differences over time.

### Weighted average maturity

The average time to maturity of a portfolio's bonds, each weighted by its share of the portfolio's value.

### Laddering

Buying bonds that mature at regular intervals, so that money comes back steadily and can be reinvested at the rates then available.

### Barbell

A portfolio concentrated in short and long maturities, with little in between.

### Immunisation

Matching the duration of a portfolio to the timing of a future payment, so that changes in yields affect the portfolio and the payment by about the same amount.

### Mark to market

Valuing holdings at current market prices rather than at their purchase price, so that the portfolio's reported value moves with the market.

## Questions

Answer each question below from the data above. Start each answer on a new line with its
number in bold, like **Q1.**, give the direct answer first, then at most two sentences of
reasoning that cite the records (IDs) you relied on.

Then end with one JSON block (```json) holding the structured answer to each question listed
here, with exactly these fields, shaped like {"Q1": {"field": value}, ...}. Name entities by their record ID: the entity_id in the CSV files, or the part of the IRI after lad: in the RDF (E01, not Kestrel Energy plc).

- Q1: rating (a rating, or "none")
- Q2: downgraded ("yes", "no" or "depends")
- Q3: investment_grade ("yes", "no" or "depends"), rating (a rating, or "none")
- Q4: outlook (an outlook)
- Q5: risk_of (a record ID), rating (a rating, or "none")
- Q7: issuers (a list of record IDs)
- Q8: entities (a list of record IDs)
- Q9: count (a number)
- Q10: investment_grade ("yes", "no" or "depends")
- Q11: rating (a rating, or "none")
- Q12: rating (a rating, or "none")
- Q13: count (a number)
- Q14: rating (a rating, or "none")
- Q15: rating (a rating, or "none")
- Q16: changed ("yes", "no" or "depends")
- Q17: downgraded ("yes", "no" or "depends")
- Q18: issuers (a list of record IDs)
- Q19: issuers (a list of record IDs)
- Q20: in_default ("yes", "no" or "depends")
- Q21: entities (a list of record IDs)
- Q22: entities (a list of record IDs)
- Q23: rating (a rating, or "none")
- Q24: investment_grade ("yes", "no" or "depends")
- Q25: count (a number)
- Q26: rating (a rating, or "none")
- Q27: rating (a rating, or "none")
- Q28: rating (a rating, or "none")
- Q29: rating (a rating, or "none")
- Q30: entities (a list of record IDs)
- Q31: any ("yes", "no" or "depends")
- Q32: parent (a record ID)
- Q33: risk_of (a record ID), rating (a rating, or "none")
- Q34: same_group ("yes", "no" or "depends")
- Q35: count (a number)
- Q36: count (a number)
- Q37: count (a number)
- Q38: same ("yes", "no" or "depends")
- Q39: rating (a rating, or "none")
- Q40: count (a number)
- Q41: rating (a rating, or "none")
- Q42: country (a country code)
- Q43: count (a number)
- Q44: local_currency ("yes", "no" or "depends")
- Q45: above_ceiling ("yes", "no" or "depends")
- Q46: issuer_rating ("yes", "no" or "depends")
- Q47: rating (a rating, or "none")
- Q48: count (a number)

Q1. What was Kestrel Energy's rating on 1 January 2025?
Q2. Has Kestrel Energy been downgraded in 2026?
Q3. Is Kestrel Energy's 2031 note investment grade?
Q4. What is Northwind Holdings' current outlook?
Q5. Whose credit risk does a holder of the Northwind Finance 2030 notes take, and how is it rated?
Q6. Why is Valdoria Telecom's foreign-currency rating lower than its local-currency rating?
Q7. Which issuers were downgraded in 2026?
Q8. Which entities were in default on 1 October 2026?
Q9. As of 1 October 2026, how many distinct issuers hold an issuer rating?
Q10. Is Valdoria Telecom investment grade?
Q11. What was Marlow Utilities' rating on 1 June 2025?
Q12. What was Marlow Utilities' rating on 1 January 2024?
Q13. How many times has Marlow Utilities been downgraded?
Q14. What was Halden Foods' rating on 1 January 2024?
Q15. What was Halden Bank's rating on 1 January 2026?
Q16. Has Marlow Utilities' rating changed since 1 January 2025?
Q17. Was Orrin Bank downgraded in 2026?
Q18. Which issuers were on Rating Watch Negative on 1 October 2026?
Q19. Which issuers had a Negative outlook on 1 October 2026?
Q20. Is Pellam Retail in default?
Q21. Which entities had an issuer rating at some point but no longer had one on 1 October 2026?
Q22. Which entities have ever been in default?
Q23. What is Kestrel Energy's short-term rating?
Q24. Is Kestrel Energy's issuer rating investment grade?
Q25. How many instruments held an investment-grade rating on 1 October 2026?
Q26. What is Corvenia Power's local-currency rating?
Q27. How is Corvenia Power's 2032 note rated?
Q28. What is the Republic of Corvenia's foreign-currency issuer rating?
Q29. What is the Republic of Valdoria's issuer rating?
Q30. Which entities had a foreign-currency issuer rating exactly at their country's ceiling on 1 October 2026?
Q31. Did any company have a foreign-currency issuer rating above its country's ceiling on 1 October 2026?
Q32. Who is Halden Leasing's ultimate parent?
Q33. Whose credit risk does a holder of the Halden Leasing 2028 notes take, and how is it rated?
Q34. Is Halden Foods part of the same group as Halden Bank?
Q35. How many entities are in the Halden group, the parent included?
Q36. How many entities are in the Northwind group, the parent included?
Q37. How many distinct legal entities does the data describe?
Q38. Are Orrin Bank AG and Orrin Bancorp Inc the same entity?
Q39. What is Northwind Holdings' current rating?
Q40. How many distinct issuers domiciled in GB held an issuer rating on 1 October 2026?
Q41. What is Brindle Capital's current rating?
Q42. In which country is Halden Bank domiciled?
Q43. How many distinct entities are domiciled in Luxembourg (LU)?
Q44. Is Valdoria Telecom's 2027 note a local-currency obligation?
Q45. Is Valdoria Telecom's 2027 note rated above what Valdoria's Country Ceiling allows?
Q46. Does Halden Leasing have an issuer rating?
Q47. How is Corvenia Power's 2034 note rated?
Q48. How many instruments held a rating on 1 October 2026?
