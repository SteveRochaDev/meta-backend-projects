# Working with Default Values in MySQL

## Description
This lab demonstrates how to use default values in a MySQL database. We created an `address` table to store customer addresses with a default value for the town column. Additionally, we optionally set a default value for the postcode column.

## Tasks Completed
- Created the database `cm_devices` (if not already present)
- Created the table `address` with the following columns:
  - `id` INT NOT NULL
  - `street` VARCHAR(255)
  - `postcode` VARCHAR(10) DEFAULT "HA97DE" (optional)
  - `town` VARCHAR(30) DEFAULT "Harrow"
- Verified table creation with `SHOW TABLES;` and `SHOW COLUMNS FROM address;`
- Practiced using the `DEFAULT` keyword in SQL to simplify data entry

## Status
Lab completed successfully.  
**Grade:** 100%