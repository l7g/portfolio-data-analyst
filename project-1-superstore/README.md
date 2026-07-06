# Which product categories are eroding profit margin,

# and in which regions?

## Business Context

A US-based retailer wants to understand where it is losing
margin in order to reallocate budget and optimize
its discounting strategy.

## Business Questions

1. Which categories have the lowest average profit margin?
2. Are high discounts actually eroding profit?
3. Are there regions that are systematically less profitable?
4. Which sub-categories should be reduced or discontinued?
5. What is driving the South region's consistently low sales?
6. Are Supplies over-discounted, or do they suffer from high supplier costs?
7. Are Tables sold at full price despite negative margins - suggesting a structural cost problem rather than a discounting issue?
8. Is Central's high loss rate driven by specific sub-categories or by aggressive discounting in that region?
9. Are Appliances suffering from a structural cost problem indipendent of discounting, given their moderate discount rate but deeply negative margin?
10. Are Binders profitable in absolute terms only because of extreme volumes, and is that volume sustainable without heavy discounting?
11. What caused the unexpected sales drop in December 2017 despite November's historic peak, and was it driven by fulfillment bottlenecks or inventory exhaustion?

## Initial Hypotheses (Phase 1 Exploration)

Based on a quick pivot table exploration of the raw data, the following initial trends and patterns were identified to guide the upcoming deep-dive analysis:

- **High-Volume vs. High-Profit Disconnect:** The "Technology" category appears to drive the highest sales overall (particularly led by Copiers and Phones as seen in the sub-category breakdown), making it a core revenue driver for the Superstore.
- **The Furniture Profit Drain:** While "Furniture" generates significant sales volume across multiple regions, its sub-categories **Tables** and **Bookcases** are critically unprofitable, dragging down the entire category's performance. **Tables** alone represent the largest profit drain in the entire dataset (over -$17,700).
- **Regional Sales Disparity:** Regional sales are heavily skewed, with the **West** and **East** regions dominating total revenue, while the **South** consistently lags behind across all major product categories.
- **Supplies Anomalies:** Within Office Supplies, **Supplies** is the only sub-category showing a negative net profit, suggesting potential issues with over-discounting or high supplier costs that warrant further programmatic investigation.

## SQL Exploration Findings

### Key findings from the SQL analysis:

1. **Tables is the primary profit destroyer** — -$17,725 in absolute profit loss, with a 26% average discount rate confirming discounting as a key driver alongside structural cost issues.

2. **Discounting strongly correlates with negative margins** — the top 4 most discounted sub-categories (Binders, Machines, Tables, Bookcases) all show negative average margins.

3. **Central region has a structural loss problem** — 31.90% of orders are unprofitable, nearly double the West (9.93%).

4. **Binders anomaly** — highest discount rate average (37%), deeply negative margin (-19.96%), yet $30,221 total profit due to extreme volume.Sustainability of this model depends on volume continuity.

5. **Appliances cost problem** — moderate discount (17%) but -15.69% margin suggests supplier cost issues independent of discounting.

6. **Strong seasonality** — consistent peaks in September and November across all 4 years, with November 2017 as the highest single month ($118,447).

## Key Findings

## Business Recommendations

### Open Questions & Data Limitations

The following questions emerged from the analysis but could not be fully answered with the available dataset:

**Q11 — December 2017 Sales Drop**
Despite November 2017 being the historic sales peak ($118,447), December dropped significantly. Two hypotheses were identified:

- Fulfillment bottlenecks unable to handle post-peak volume
- Inventory exhaustion after the November surge

Answering this requires additional data: inventory levels, fulfillment times, and order cancellation rates — not available in this dataset.

## Data

- **Source:** Superstore Dataset (Kaggle — Vivek Chowdhury)
- **Period:** 2014–2017
- **Size:** 9,994 orders, 21 columns
- **Limitations:** US only, fictional retailer
  (but realistic patterns)

## Tech Stack

| Tool                                 | Purpose                   |
| ------------------------------------ | ------------------------- |
| Python (pandas, matplotlib, seaborn) | Cleaning & analysis       |
| PostgreSQL                           | Exploratory SQL queries   |
| Excel                                | Quick initial exploration |
| Power BI                             | Interactive dashboard     |

## Process

### 1. Quick Exploration (Excel)

Pivot table to understand category and region distribution
before diving into code.

### 2. Data Cleaning & Analysis (Python)

- Renamed columns to snake_case for easier access
- 11 null values in `postal_code` → kept
  (no impact on analysis)
- Created `profit_margin` column (Profit / Sales \* 100)
- Correlation analysis between discount and profit

### 3. SQL Queries (PostgreSQL)

See [/sql/queries.sql](./sql/queries.sql)
for all annotated queries.

### 4. Dashboard (Power BI)

See [/dashboard/](./dashboard/) for screenshots
and the `.pbix` file.

## Key Findings

1. **Tables** is the worst-performing sub-category
   with an average margin of **-55%**
2. Discount and profit show a **weak inverse correlation**
   (-0.22) — discounts alone don't explain margin erosion,
   other factors are at play
3. **Copiers** have the highest average profit per order
   ($817) — a strong candidate for increased focus
4. The **West region** leads in both volume and sales,
   but margin distribution varies significantly
   across sub-categories

## Business Recommendation

Discontinue or significantly reduce the **Tables**
sub-category. Review discounting policy specifically
for **Furniture**, which combines low volume
and negative margins. Prioritize **Copiers**
and **Technology** for upselling initiatives.

## Limitations

- Dataset is fictional — patterns may not reflect
  a real retailer
- No data on fixed costs or overhead
- 4 years of data may not be sufficient
  for robust seasonal trend analysis

## Dashboard Preview

![Dashboard](./dashboard/screenshot-powerbi.png)
