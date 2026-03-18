-- Task 1: Create and use database
CREATE DATABASE IF NOT EXISTS Chinook;
USE Chinook;

-- Task 2: Create Customer table
CREATE TABLE Customer (
    CustomerId INT NOT NULL,
    FirstName VARCHAR(40) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Company VARCHAR(80),
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60) NOT NULL,
    SupportRepId INT,
    CONSTRAINT PK_Customer PRIMARY KEY (CustomerId)
);

-- Task 3: Insert sample data
INSERT INTO Customer VALUES
(1, 'Luís', 'Gonçalves', 'Embraer', 'Address1', 'São José dos Campos', 'SP', 'Brazil', '12227-000', '111', '222', 'luis@email.com', 3),
(2, 'Eduardo', 'Martins', 'Woodstock', 'Address2', 'São Paulo', 'SP', 'Brazil', '01007-010', '111', '222', 'eduardo@email.com', 4),
(3, 'Alexandre', 'Rocha', 'Banco do Brasil', 'Address3', 'São Paulo', 'SP', 'Brazil', '01310-200', '111', '222', 'alex@email.com', 5),
(4, 'Roberto', 'Almeida', 'Riotur', 'Address4', 'Rio de Janeiro', 'RJ', 'Brazil', '20040-020', '111', '222', 'roberto@email.com', 3),
(5, 'Mark', 'Philips', 'Telus', 'Address5', 'Edmonton', 'AB', 'Canada', 'T6G 2C7', '111', '222', 'mark@email.com', 5),
(6, 'Jennifer', 'Peterson', 'Rogers', 'Address6', 'Vancouver', 'BC', 'Canada', 'V6C 1G8', '111', '222', 'jennifer@email.com', 3);

-- Task 1: Display selected columns
SELECT CustomerID, FirstName, LastName, City, State, Country
FROM Customer;

-- Task 2: Sort by FirstName (A-Z)
SELECT CustomerID, FirstName, LastName, City, State, Country
FROM Customer
ORDER BY FirstName;

-- Task 3: Filter by Country (Brazil)
SELECT CustomerID, FirstName, LastName, City, State, Country
FROM Customer
WHERE Country = "Brazil";

-- Combined: Filter + Sort
SELECT CustomerID, FirstName, LastName, City, State, Country
FROM Customer
WHERE Country = "Brazil"
ORDER BY FirstName;

-- Optional Task
SELECT FirstName, Country
FROM Customer
WHERE Country = "Canada"
ORDER BY FirstName;