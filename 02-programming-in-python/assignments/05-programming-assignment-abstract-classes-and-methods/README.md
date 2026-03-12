# Programming Assignment: Abstract Classes and Methods

## Introduction
In this lab, you will create an abstract class for a bank and use it to develop a specific bank class. The abstract class outlines the essential structure, while the regular bank class implements these methods to simulate basic bank functions.

## Goal
To practice using Python’s `ABC` and `@abstractmethod` decorators to create abstract classes and methods, and to understand how to implement them in subclasses.

## Objectives

- Create an Abstract Base Class.
- Define and implement abstract methods.
- Implement inheritance and method overriding.
- Handle data with class and instance variables.
- Perform conditional checks.
- Practice return values and print statements for outputs.

## Project Structure

- `bank.py`
- `README.md`

## Instructions

### Part 1: Create the abstract bank class

1. Open `bank.py`.
2. Create a class `Bank` that inherits from `ABC`.
3. Implement the `basicinfo()` method:
   - Print `"This is a generic bank"`.
   - Return `"Generic bank: 0"`.
4. Define the abstract method `withdraw()` using the `@abstractmethod` decorator.
   - Leave the body empty using `pass`.

### Part 2: Create the Swiss bank subclass

1. Create a class `Swiss` that inherits from `Bank`.
2. Implement the constructor `__init__` to initialize an instance variable `bal` to `1000`.
3. Override the `basicinfo()` method:
   - Print `"This is the Swiss Bank"`.
   - Return `"Swiss Bank: "` followed by the current balance.
4. Override the `withdraw(amount)` method:
   - If `amount <= bal`, deduct it from `bal`, print the withdrawn amount and new balance, and return the new balance.
   - If `amount > bal`, print `"Insufficient funds"` and return the original balance.

### Part 3: Running your code

1. Open a terminal in VSCode.
2. Run the Python file with:

   ```bash
   python3 bank.py
   ```

3. Verify the output matches the expected format:

   - `basicinfo()` prints and returns the correct bank message and balance.
   - `withdraw()` updates the balance when funds are sufficient.
   - `withdraw()` displays `"Insufficient funds"` when attempting to withdraw too much.

## Key Takeaways

- Abstract classes define a common interface for subclasses.
- Subclasses implement abstract methods and can extend functionality.
- Instance variables allow each bank object to maintain its own balance.
- Conditional logic ensures safe withdrawals.

## Status

Lab completed successfully.

**Grade:** 100%