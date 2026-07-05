-- ============================================
-- Superstore Sales Analysis — SQL Queries
-- All queries run on the orders_clean table
-- ============================================


-- ============================================
-- Q1: Total Sales and Profit by Category
-- Identifies which categories drive revenue
-- vs which actually generate profit
-- ============================================

SELECT category,
       ROUND(SUM(sales)::numeric, 2) AS total_sales,
       ROUND(SUM(profit)::numeric, 2) AS total_profit,
       ROUND(AVG(profit_margin)::numeric, 2) as avg_margin_pct
FROM orders_clean
GROUP BY category
ORDER BY total_profit DESC;

-- ============================================
-- Q2: Average Profit Margin by Sub-Category
-- Sorted ascending to surface worst performers
-- Margin normalizes for price differences
-- ============================================

SELECT category,
       sub_category, 
       ROUND(AVG(profit_margin)::numeric, 2) as avg_margin_pct
FROM orders_clean
GROUP BY category, sub_category
ORDER BY avg_margin_pct ASC;

-- ============================================
-- Q3: Orders with Negative Profit by Region
-- Percentage normalizes for volume differences
-- Reveals structural loss patterns by region
-- ============================================

SELECT region,
       COUNT(*) AS total_orders,
       COUNT(CASE WHEN profit < 0 THEN 1 END) AS neg_profit_orders,
       ROUND((COUNT(CASE WHEN profit < 0 THEN 1 END)::float / COUNT(*)* 100)::numeric, 2)  AS neg_orders_pct
FROM orders_clean
GROUP BY region
ORDER BY neg_orders_pct DESC;

-- ============================================
-- Q4: Top 10 Products by Total Sales
-- Revenue champions — to be cross-referenced
-- with margin data in Python analysis
-- ============================================

SELECT product_name,
       ROUND(SUM(sales)::numeric, 2) AS total_sales
FROM orders_clean
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- ============================================
-- Q5: Average Discount and Margin by Sub-Category
-- Tests whether discounting drives margin erosion
-- High discount + negative margin = likely cause
-- ============================================

SELECT category,
       sub_category,
       AVG(discount) AS avg_discount,
       ROUND(AVG(profit_margin)::numeric, 2) AS avg_pct_margin
FROM orders_clean
GROUP BY category, sub_category
ORDER BY avg_discount DESC;

-- ============================================
-- Q6: Monthly Sales Trend
-- Identifies seasonal peaks for inventory
-- and staffing planning
-- ============================================

SELECT EXTRACT(YEAR FROM order_date)::int as year,
       EXTRACT(MONTH FROM order_date)::int as month,
       ROUND(SUM(sales)::numeric, 2) AS month_sales
FROM orders_clean
GROUP BY year, month
ORDER BY year, month;

-- ============================================
-- Q7: Absolute Profit Loss by Sub-Category
-- Ranks sub-categories by total dollar impact
-- Complements margin efficiency analysis in Q2
-- ============================================

SELECT category,
       sub_category,
       AVG(discount) AS avg_discount,
       ROUND(AVG(profit_margin)::numeric, 2) AS avg_pct_margin,
       ROUND(SUM(profit)::numeric, 2) AS total_profit
FROM orders_clean
GROUP BY category, sub_category
ORDER BY total_profit ASC;