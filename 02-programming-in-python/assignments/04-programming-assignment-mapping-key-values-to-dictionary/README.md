# Programming Assignment: Mapping key-values to Dictionary data structures

## Introduction
In this lab, you will use Python techniques to modify sequences using functions like `map()` and comprehensions for both lists and dictionaries. Your goal is to create usernames for employees at Little Lemon and organize employee initials and IDs in a dictionary for easy access.

## Goal
Practice using Python's `map()` function and comprehensions to efficiently transform and organize data in lists and dictionaries.

## Objectives

- Use the `map()` function to apply a custom function to all elements in a list.
- Apply list comprehension to create and format strings based on given conditions.
- Use dictionary comprehension to create key-value mappings for organized data access.

## Project Structure

- `comprehensions.py`
- `README.md`

## Instructions

### Part 1: Modifying employee list

1. Open `comprehensions.py`.
2. Implement the `to_mod_list()` function using the `map()` function.
3. The `mod()` function should be applied to all employees to generate a list of `"name_department"` strings.

### Part 2: Generating usernames

1. Implement the `generate_usernames()` function.
2. Use list comprehension to replace all spaces with underscores (`_`) in the modified employee list.

### Part 3: Mapping IDs to initials

1. Implement the `map_id_to_initial()` function.
2. Use dictionary comprehension to create a dictionary where the **key** is the first letter of the employee's name and the **value** is their ID.

### Part 4: Running your code

1. Open a terminal in VSCode.
2. Run the Python file with:

   ```bash
   python3 comprehensions.py
   ```

3. Verify that the output matches the expected format:

   - List of modified employee strings

   - List of usernames

   - Dictionary mapping initials to IDs

## Status

Lab completed successfully.

**Grade:** 100%

