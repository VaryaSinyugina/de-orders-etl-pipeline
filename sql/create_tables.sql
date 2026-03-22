CREATE TABLE IF NOT EXISTS fact_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    total_almount NUMERIC
);