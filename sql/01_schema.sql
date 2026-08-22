-- PostgreSQL schema
CREATE TABLE sales_2025 (
    order_id VARCHAR(20) PRIMARY KEY,
    order_date DATE,
    product_id VARCHAR(20),
    product_name VARCHAR(150),
    category VARCHAR(50),
    brand VARCHAR(50),
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    city VARCHAR(50),
    quantity INT,
    unit_price NUMERIC(14,2),
    discount NUMERIC(5,4),
    revenue NUMERIC(16,2),
    cost NUMERIC(16,2),
    channel VARCHAR(30),
    payment_method VARCHAR(30)
);
