-- Task 1: Use the database
CREATE DATABASE IF NOT EXISTS cm_devices;
USE cm_devices;

-- Task 2: Create the customers table
CREATE TABLE customers (
    username CHAR(9),
    fullName VARCHAR(100),
    email VARCHAR(255)
);

-- Optional Task: Create the feedback table
CREATE TABLE feedback (
    feedbackID CHAR(8),
    feedbackType VARCHAR(100),
    comment TEXT(500)
);