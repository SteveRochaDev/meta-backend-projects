# Working with Strings in MySQL

## Description
This lab demonstrates how to work with string values in a MySQL database. We created a `customers` table to store customer username, full name, and email. Additionally, we created a `feedback` table to store customer feedback including feedback ID, type, and comment.

## Tasks Completed
- Created the database `cm_devices` (if not already present)
- Created the table `customers` with the following columns:
  - `username` CHAR(9)
  - `fullName` VARCHAR(100)
  - `email` VARCHAR(255)
- Verified table creation with `SHOW TABLES;` and `SHOW COLUMNS FROM customers;`
- Completed additional task by creating the `feedback` table:
  - `feedbackID` CHAR(8)
  - `feedbackType` VARCHAR(100)
  - `comment` TEXT(500)
- Tested all tables and verified their structures in MySQL

## Status
Lab completed successfully.  
**Grade:** 100%