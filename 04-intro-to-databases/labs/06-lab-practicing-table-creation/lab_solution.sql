-- Task 1: Create the database
CREATE DATABASE IF NOT EXISTS football_club;

-- Task 2: Use the database
USE football_club;

-- Task 3: Create the players table
CREATE TABLE players (
    playerID INT,
    playerName VARCHAR(50),
    age INT
);

-- Optional Task: Create the games table
CREATE TABLE games (
    gameID INT,
    gameDate DATE,
    score INT
);

-- Verify tables
SHOW TABLES;