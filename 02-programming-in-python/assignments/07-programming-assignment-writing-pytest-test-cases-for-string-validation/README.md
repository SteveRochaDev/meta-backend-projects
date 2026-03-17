# Programming Assignment: Writing PyTest Test Cases for String Validation

## Introduction
In this lab, you will validate a string input using two specific tests: one to check the length and structure of the input string, and another to verify basic grammar rules. This involves creating automated test cases using PyTest to ensure these checks are met.

## Goal
Learn to create automated test cases using PyTest to validate code functionality based on predefined criteria.

## Objectives

- Verify that string inputs meet specified length constraints (word and character limits).
- Ensure that string inputs adhere to basic structural rules, such as starting with an uppercase letter and ending with a period.

## Project Structure

- `spellcheck.py`
- `test_spellcheck.py`
- `README.md`

## Instructions

### Part 1: Setup

1. Open the `test_spellcheck.py` file in the project folder.

### Part 2: Import Required Modules

1. Import the `pytest` module.
2. Import the `spellcheck` module which contains the functions to be tested.

### Part 3: Define Test String Variables

1. Two variables are defined:
   - `alpha`: a string that should pass the tests.
   - `beta`: a string that should fail one of the tests (for bonus step).
2. Comment out `beta` for now.

### Part 4: Create PyTest Fixture

1. Create a fixture named `input_value()` that returns `alpha` as the default input string.

### Part 5: Write Test Functions

#### Function `test_length()`

- Verify that the string has fewer than 10 words using `spellcheck.word_count()`.
- Verify that the string has fewer than 50 characters using `spellcheck.char_count()`.

#### Function `test_struc()`

- Verify that the first character is uppercase using `spellcheck.first_char()` and `.isupper()`.
- Verify that the last character is a period using `spellcheck.last_char()`.

### Part 6: Save and Run Tests

1. Save the file.
2. In the terminal, run:

```bash
python3 -m pytest test_spellcheck.py
```

Both tests should pass when using `alpha` as input.

## Bonus Step

Change the `input_value` fixture to return `beta` instead of `alpha` and rerun the tests to see one fail, demonstrating the tests detect incorrect input.

## Expected Output

- With `alpha` as input: both tests pass.
- With `beta` as input: one test fails.

## Status

Lab completed successfully.

**Grade:** 100%