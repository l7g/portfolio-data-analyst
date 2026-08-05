# Which Product Categories Are Eroding Profit Margin, and In Which Regions?

## Business Context

A US-based retailer wants to understand where it is losing margin in
order to reallocate budget and optimize its discounting strategy.

## Business Questions

1. Which categories have the lowest average profit margin?
2. Are high discounts actually eroding profit?
3. Are there regions that are systematically less profitable?
4. Which sub-categories should be reduced or discontinued?
5. What is driving the South region's consistently low sales?
6. Are Supplies over-discounted, or do they suffer from high supplier costs?
7. Are Tables sold at full price despite negative margins — suggesting a
   structural cost problem rather than a discounting issue?
8. Is Central's high loss rate driven by specific sub-categories or by
   aggressive discounting in that region?
9. Are Appliances suffering from a structural cost problem independent
   of discounting, given their moderate discount rate but deeply
   negative margin?
10. Are Binders profitable in absolute terms only because of extreme
    volumes, and is that volume sustainable without heavy discounting?
11. What caused the unexpected sales drop in December 2017 despite
    November's historic peak, and was it driven by fulfillment
    bottlenecks or inventory exhaustion?

## Initial Hypotheses (Phase 1 Exploration)

Based on a quick pivot table exploration of the raw data, the following
initial trends were identified to guide the deep-dive analysis:

- **High-Volume vs. High-Profit Disconnect:** Technology drives the
  highest sales overall (led by Copiers and Phones), making it a core
  revenue driver for the Superstore.
- **The Furniture Profit Drain:** Furniture generates significant sales
  volume, but Tables and Bookcases are critically unprofitable, dragging
  down the entire category. Tables alone is the largest profit drain in
  the dataset (over -$17,700).
- **Regional Sales Disparity:** Sales are skewed toward West and East,
  while South consistently lags behind across all major categories.
- **Supplies Anomalies:** Within Office Supplies, Supplies is the only
  sub-category showing a negative net profit, suggesting over-discounting
  or high supplier costs worth investigating further.

## SQL Exploration Findings

1. **Tables is the primary profit destroyer** — -$17,725 in absolute
   profit loss, with a 26% average discount rate confirming discounting
   as a key driver alongside structural cost issues.
2. **Discounting correlates with negative margins** — the top 4 most
   discounted sub-categories (Binders, Machines, Tables, Bookcases) all
   show negative average margins.
3. **Central region has a structural loss problem** — 31.90% of orders
   are unprofitable, more than triple West's rate (9.93%).
4. **Binders anomaly** — highest average discount rate (37%), deeply
   negative margin (-19.96%), yet $30,222 total profit due to extreme
   volume. Sustainability of this model depends on volume continuity.
5. **Appliances cost problem** — moderate discount (17%) but a -15.69%
   margin suggests factors beyond discounting alone.
6. **Strong seasonality** — consistent peaks in September and November
   across all 4 years, with November 2017 as the single highest month
   ($118,447).

## Deep-Dive Findings (Python Analysis)

The SQL exploration surfaced _what_ was underperforming; the following
deep dives establish _why_:

1. **Binders is structurally profitable — the discount policy is the
   problem, not the product.** At full price, Binders reach a 47.54%
   margin. The current 70-80% discount tiers actively generate losses
   ($16k-$21k) and should be eliminated, not the sub-category itself.
2. **Appliances is not uniformly broken — it's bimodal.** A top tier of
   air-cleaner/purifier products drives strong absolute profit and
   margin. The rest of the catalog sits on thin-to-negative margins
   (-9.9% average across 77 SKUs) that survive only because volume
   keeps aggregate profit marginally positive. A handful of specific
   SKUs (disposable bags, one office refrigerator) are genuinely
   catastrophic, down to -275% margin.
3. **Central's loss rate is a local discounting issue, not a market
   problem.** Central discounts Appliances at 44.9% on average (vs. 17%
   nationally) and Binders at 51% (vs. 37% nationally), driving margins
   to -125% and -86% respectively in that region alone — far worse than
   the same sub-categories perform elsewhere.

## Key Findings & Business Recommendations

1. **Tables** is the worst-performing sub-category by absolute profit
   loss (-$17,725, -14.77% average margin) and should be discontinued
   or fundamentally re-priced.
2. Discount and profit show a **weak global inverse correlation**
   (-0.22) — discounting is a real driver but doesn't explain everything;
   several sub-categories (Appliances, Binders) have cost problems
   independent of discounting.
3. **Copiers** has both the highest average margin (31.72%) and the
   highest total profit ($55,618) of any sub-category — the strongest
   candidate for expanded focus and upselling.
4. **Central requires a discount policy review**, specifically for
   Appliances and Binders, before any volume-growth initiative — its
   loss rate is driven by local over-discounting, not an inherently
   weaker regional market.
5. The business should **eliminate the 70-80% discount tiers on
   Binders** and **run a SKU-level cleanup** on the specific catastrophic
   products identified in the Appliances deep dive, rather than treating
   either sub-category as a lost cause.

### Open Questions & Data Limitations

**Q11 — December 2017 Sales Drop**
Despite November 2017 being the historic sales peak ($118,447), December
dropped significantly. Two hypotheses were identified:

- Fulfillment bottlenecks unable to handle post-peak volume
- Inventory exhaustion after the November surge

Answering this requires additional data — inventory levels, fulfillment
times, and order cancellation rates — not available in this dataset.

## Data

- **Source:** Superstore Dataset (Kaggle — Vivek Chowdhury)
- **Period:** 2014–2017
- **Size:** 9,994 orders, 21 columns
- **Limitations:** US only, fictional retailer (but realistic patterns)

## Tech Stack

| Tool                                 | Purpose                   |
| ------------------------------------ | ------------------------- |
| Python (pandas, matplotlib, seaborn) | Cleaning & analysis       |
| PostgreSQL                           | Exploratory SQL queries   |
| Excel                                | Quick initial exploration |

## Process

### 1. Quick Exploration (Excel)

Pivot table to understand category and region distribution before
diving into code.

### 2. Data Cleaning & Analysis (Python)

- Renamed columns to snake_case for easier access
- 11 null values in `postal_code` → kept (no impact on analysis)
- Created `profit_margin` column (Profit / Sales \* 100)
- Correlation analysis between discount and profit

### 3. SQL Queries (PostgreSQL)

See [/sql/queries.sql](./sql/queries.sql) for all annotated queries.

## Limitations

- Dataset is fictional — patterns may not reflect a real retailer
- No data on fixed costs or overhead
- 4 years of data may not be sufficient for robust seasonal trend analysis
