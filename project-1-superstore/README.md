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
