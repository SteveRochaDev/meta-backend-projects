# Programming Assignment: Type Casting Input

## Introduction
This lab focuses on handling user input in Python and applying explicit type casting. You will learn how to convert input strings to the correct data types so they can be used in calculations or logical operations.

## Goal
The goal of this assignment is to ensure user input data is properly processed using Python type casting. By completing this lab, you will correctly handle strings, integers, floats, and boolean values.

## Objectives

- Convert user input to a string, integer, float, and boolean as required
- Calculate the total bill from multiple numeric inputs
- Use explicit type casting to ensure correct data types for calculations

## Project Structure

- `exercise1.py`
- `exercise2.py`
- `README.md`

## Instructions

### Exercise 1: Type Casting for User Input

1. Open the `exercise1.py` file.
2. Modify the script under the `# Modify the line below` comments:
   - Convert `name` to a string
   - Convert `age` to an integer
   - Convert `height` to a float
   - Convert `loyalty` input to a boolean (e.g., "yes"/"true"/"1" → `True`, otherwise `False`)
3. Save the file.
4. Run the script in the terminal with:

   ```bash
   python3 exercise1.py
   ```

### Exercise 2: Calculate and Display Total Bill

1. Open the `exercise2.py` file.
2. Modify the script under the `# Modify the line below` comments:
   - Convert all three item inputs to floats
   - Calculate the total bill
   - Round the total bill to two decimal places
3. Save the file.
4. Run the script in the terminal with:

   ```bash
   python3 exercise2.py
   ```

## Key Takeaways

- User input from `input()` is always a string, so explicit type conversion is often required
- Numeric inputs must be cast to `int` or `float` before performing calculations
- Boolean values require converting user input to `True` or `False` based on expected responses
- Rounding is essential for displaying monetary values

## Status

Lab completed successfully.
**Grade:** 100%