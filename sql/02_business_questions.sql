-- Business questions for the portfolio project

-- 1. Doanh thu và lợi nhuận theo tháng
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(revenue) AS revenue,
    SUM(revenue - cost) AS profit
FROM sales_2025
GROUP BY 1
ORDER BY 1;

-- 2. Top 10 sản phẩm theo doanh thu
SELECT product_name,
       SUM(quantity) AS units_sold,
       SUM(revenue) AS revenue,
       SUM(revenue - cost) AS profit
FROM sales_2025
GROUP BY product_name
ORDER BY revenue DESC
LIMIT 10;

-- 3. Hiệu quả theo kênh bán hàng
SELECT channel,
       COUNT(DISTINCT order_id) AS orders,
       SUM(revenue) AS revenue,
       SUM(revenue - cost) AS profit
FROM sales_2025
GROUP BY channel
ORDER BY revenue DESC;

-- 4. Thành phố có doanh thu cao nhất
SELECT city,
       SUM(revenue) AS revenue,
       SUM(revenue - cost) AS profit
FROM sales_2025
GROUP BY city
ORDER BY revenue DESC;

-- 5. Danh mục có biên lợi nhuận tốt
SELECT category,
       SUM(revenue) AS revenue,
       SUM(revenue - cost) AS profit,
       ROUND(100.0 * SUM(revenue - cost) / NULLIF(SUM(revenue),0), 2) AS margin_pct
FROM sales_2025
GROUP BY category
ORDER BY margin_pct DESC;
