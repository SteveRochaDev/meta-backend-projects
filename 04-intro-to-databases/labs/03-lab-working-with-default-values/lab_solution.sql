-- Task 1: Use the database
CREATE DATABASE IF NOT EXISTS cm_devices;
USE cm_devices;

-- Task 2: Create the address table with default value for town
CREATE TABLE address (
    id INT NOT NULL,
    street VARCHAR(255),
    postcode VARCHAR(10),
    town VARCHAR(30) DEFAULT "Harrow"
);

-- Optional Task: Create the address table with default values for postcode and town
DROP TABLE IF EXISTS address;

CREATE TABLE address (
    id INT NOT NULL,
    street VARCHAR(255),
    postcode VARCHAR(10) DEFAULT "HA97DE",
    town VARCHAR(30) DEFAULT "Harrow"
);