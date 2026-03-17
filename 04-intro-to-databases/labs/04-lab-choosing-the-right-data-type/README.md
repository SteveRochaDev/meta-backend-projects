# Lab 4 – Choosing the Right Data Type

## Description
This lab demonstrates how to choose suitable data types for columns in a MySQL database. We created an `invoice` table to store customer orders and an optional `contactDetails` table.

## Tasks Completed
- Created the database `cm_devices` (if not already present)
- Created the `invoice` table with the following columns:
  - `customerName` VARCHAR(50)
  - `orderDate` DATE
  - `quantity` INT
  - `price` DECIMAL(10,2)
- Optional: Created a `contactDetails` table:
  - `accountNumber` INT
  - `phoneNumber` VARCHAR(14)
  - `email` VARCHAR(255)
- Verified table creation with `SHOW TABLES;` and `SHOW COLUMNS FROM invoice;`

## Status
Lab completed successfully.  
**Grade:** 100%