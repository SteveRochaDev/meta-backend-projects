-- Task 1: Create database
CREATE DATABASE cm_devices;

-- Use the database
USE cm_devices;

-- Task 2: Create the devices table
CREATE TABLE devices (
    deviceID int,
    deviceName varchar(50),
    price decimal
);

-- Optional Task: Create the stock table
CREATE TABLE stock (
    deviceID int,
    quantity int,
    totalCost decimal
);