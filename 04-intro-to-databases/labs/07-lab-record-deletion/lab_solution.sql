-- Use existing database
USE bookshop;

-- Clean table to avoid duplicates
TRUNCATE TABLE customers;

-- Insert sample data
INSERT INTO customers (customerID, customerName, customerAddress) VALUES
(1, 'Jack', '115 Old street Belfast'),
(2, 'James', '24 Carlson Rd London'),
(4, 'Maria', '5 Fredrik Rd, Bedford'),
(5, 'Jade', '10 Copland Ave Portsmouth'),
(6, 'Yasmine', '15 Fredrik Rd, Bedford'),
(3, 'Jimmy', '110 Copland Ave Portsmouth');

-- Delete Jimmy (required task)
DELETE FROM customers WHERE customerID = 3;

-- Optional: Delete Yasmine
DELETE FROM customers WHERE customerID = 6;

-- Verify remaining records
SELECT * FROM customers;