# Programming Assignment: Import and Scope

## Introduction
In this lab, you’ll practice using Python's `import` statement to bring external code into the scope of a project. You will import a built-in package as well as specific functions and variables from another Python file.

## Goal
- Import a built-in package and use it within the code.
- Import specific functions and variables from an external file.

## Objectives

- Use the `import` statement to import the built-in Python package `json`.
- Import specific functions and variables from another file within the same project.
- Practice manipulating data with imported components to build and save structured information.

## Project Structure

- `employee.py`
- `employee.json`
- `jsongenerator.py`
- `README.md`

## Instructions

### Part 1: Import statements

1. Open `jsongenerator.py`.
2. Import the built-in package `json`.
3. From `employee.py`, import:
   - the `details` function
   - variables: `employee_name`, `age`, `title`

### Part 2: Create the employee dictionary

1. Implement the `create_dict()` function.
2. Return a dictionary with three key-value pairs:
   - `"first_name"` → `employee_name` (string)
   - `"age"` → `age` (integer)
   - `"title"` → `title` (string)

### Part 3: Convert dictionary to JSON

1. Use the `dumps()` function from the `json` module to convert `employee_dict` into a JSON string.
2. Store the result in `json_object`. Example:

   ```python
   json_object = json.dumps(employee_dict)
   ```

### Part 4: Write JSON to file

1. Implement the `write_json_to_file(output_file, json_object)` function.
2. Open a file with the name `output_file` in write mode (`"w"`) and assign it to `newfile`.
3. Write `json_object` to `newfile` and close the file. Example:

   ```python
   with open(output_file, "w") as newfile:
       newfile.write(json_object)
   ```

### Part 5: Run your code

1. Open a terminal in the project directory.
2. Execute:

   ```bash
   python3 jsongenerator.py
   ```

3. Verify the output. The script should display or produce the following (format may vary depending on implementation):

- Employee details from `details()`
- The employee dictionary
- The JSON-formatted string

## Key Takeaways

- Python’s `import` statement allows bringing built-in and external code into your current scope.
- `json.dumps()` converts a dictionary into JSON format.
- Writing JSON to a file ensures data is structured and stored correctly.

## Status

Lab completed successfully.

**Grade:** 100%
