-- ============================================
-- ETL Reporting Queries
-- ============================================

-- Total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- Total revenue
SELECT
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- Revenue by country
SELECT
    c.country,
    SUM(o.quantity * p.price) AS revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY c.country
ORDER BY revenue DESC;


-- Top-selling products
SELECT
    p.product_name,
    SUM(o.quantity) AS units_sold
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY units_sold DESC;
