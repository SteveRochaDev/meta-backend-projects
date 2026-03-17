-- Task 1: Use the database
CREATE DATABASE IF NOT EXISTS cm_devices;
USE cm_devices;

-- Task 2: Create the invoice table
CREATE TABLE invoice (
    customerName VARCHAR(50),
    orderDate DATE,
    quantity INT,
    price DECIMAL(10,2)
);

-- Optional Task: Create a contact details table
CREATE TABLE contactDetails (
    accountNumber INT,
    phoneNumber VARCHAR(14),
    email VARCHAR(255)
);