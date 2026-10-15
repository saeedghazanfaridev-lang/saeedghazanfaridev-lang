# Python Task Tracker

A small terminal-based learning project built while practicing Python fundamentals.

## Features

- Add a task
- List tasks and their completion status
- Mark a task as done
- Remove a task
- Handle empty task titles, invalid menu choices, and non-numeric task numbers

## Requirements

- Python 3.10 or newer

## Run it

From this directory, run:

```bash
python3 main.py
```

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

## What this project practices

- Lists and dictionaries
- Strings and user input
- `if` / `elif` / `else`
- `while` and `for` loops
- Functions and return values
- `enumerate()` and `pop()`
- Basic input validation
- Unit tests with Python's standard-library `unittest` module

## Current limitations

Tasks are stored in memory, so they are cleared when the program exits. Saving tasks to a file and adding more test cases are possible next steps.

## Learning note

This is an early-stage practice project, not a production task manager. It is meant to improve problem-solving and code organization through small, understandable changes.
