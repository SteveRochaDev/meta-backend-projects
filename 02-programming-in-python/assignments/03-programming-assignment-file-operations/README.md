# Programming Assignment: Read in Data, Store, Manipulate, and Output New Data to a File

## Introduction
This lab focuses on working with file operations in Python. You will practice reading a file, storing its contents in lists, manipulating the data, and writing output to a new file.

## Goal
The goal of this assignment is to use Python’s `open()` function to read and write files, and to practice processing file contents.

## Objectives

- Create a function for reading a file.
- Create a function for writing specific contents to a file.
- Use lists to store file contents for easier data manipulation.

## Project Structure

- `file_ops.py`
- `sampletext.txt`
- `README.md`

## Instructions

1. Verify that `sampletext.txt` and `file_ops.py` exist in your project folder.
2. Run the `file_ops.py` script with:

   ```bash
   python3 file_ops.py
   ```

Complete the following functions in `file_ops.py`:

- `read_file(file_name)` — read the entire contents of the file and return it as a string.

- `read_file_into_list(file_name)` — read the file line by line and return a list with each line as an element.

- `write_first_line_to_file(file_contents, output_filename)` — write only the first line of `file_contents` to a new file.

- `read_even_numbered_lines(file_name)` — return a list of only the even-numbered lines from the file.

- `read_file_in_reverse(file_name)` — return a list of the file lines in reverse order.

Save your changes.

## Key Takeaways

- Python’s file handling allows reading, writing, and processing text files efficiently.
- Lists make it easy to store and manipulate file data.
- Functions help organize code for repeated tasks.

## Status

Lab completed successfully.

**Grade:** 100%