# Lab: Exploring Shell Commands for File and Text Processing

## Introduction
Working efficiently with files and text is a fundamental skill when using Unix-based systems. Command-line tools such as `cat`, `wc`, `grep`, and redirection operators allow developers to inspect, process, and analyze text files quickly and accurately.

This lab focuses on practicing these core commands to gain confidence in file handling, text processing, and error redirection.

## Goal
The goal of this lab is to explore and apply essential Unix shell commands for file creation, text processing, searching, and error handling.

## Objectives
- Create and write content to files using command-line tools.
- Count words and characters in files.
- Redirect error output to a file.
- Search for substrings in files using pattern matching.
- Combine commands using pipes for efficient text processing.

## Tasks Completed

### 1. Count Words in a File
- Created a file named `file.txt`.
- Added text content using output redirection.
- Displayed file content using `cat`.
- Counted words using `wc -w` with a pipe.

### 2. Redirect Errors to a File
- Attempted to list a non-existent directory.
- Redirected the error output (`stderr`) to `error.txt`.
- Counted the number of characters in the error file using `wc -c`.

### 3. Search for Substrings in a File
- Appended additional text to `file.txt`.
- Used `grep` with case-insensitive search to find occurrences of a substring.
- Counted matching words using `wc -w`.

## Commands Practiced
- `touch`
- `echo`
- `cat`
- `wc -w`
- `wc -c`
- `ls`
- `grep`
- Pipes (`|`)
- Input and output redirection (`>`, `>>`, `2>`)

## Key Takeaways
- Pipes allow commands to work together efficiently.
- Redirection makes it possible to capture output and errors into files.
- Text-processing tools like `grep` and `wc` are powerful for analyzing file content.
- Understanding standard output and standard error is essential for debugging.

## Status
Lab completed successfully.  
**Grade:** 100%
