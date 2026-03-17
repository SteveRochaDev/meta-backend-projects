-- Task 1: Create the bookshop database
CREATE DATABASE IF NOT EXISTS bookshop;

-- Task 2: Select the database
USE bookshop;

-- Task 3: Create the customers table
CREATE TABLE customers (
    customerID INT,
    customerName VARCHAR(50),
    customerAddress VARCHAR(255)
);

-- Task 4: Insert first customer
INSERT INTO customers(customerID, customerName, customerAddress)
VALUES (1, "Jack", "115 Old street Belfast");

-- Optional Task: Insert second customer
INSERT INTO customers(customerID, customerName, customerAddress)
VALUES (2, "James", "24 Carlson Rd London");

-- Task 5: Verify content
SELECT * FROM customers;