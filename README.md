# Student Grade Calculator

## Project Overview

The Student Grade Calculator is a Python program that calculates a student's grade based on their marks.

The program:
- Takes the student's name as input
- Accepts marks between 0 and 100
- Assigns a grade from A to F
- Provides an encouraging message based on the grade
- Validates invalid and non-numeric inputs

 ## Grade Criteria

| Marks    | Grade |
|----------|-------|
| 90 - 100 |   A   |
| 80 - 89  |   B   |
| 70 - 79  |   C   |
| 60 - 69  |   D   |
| 0 - 59   |   F   |

## Technologies Used

- Python

## Features

- Grade calculation using `if-elif-else`
- Input validation
- `while` loop for invalid input
- Functions for grade calculation and messages
- Error handling using `try-except`
- Encouraging messages for each grade

## How to Run

1. Open `grade_calculator.py`
2. Run the program using Python
3. Enter the student's name
4. Enter marks between 0 and 100
5. The program displays the student's grade and message

## Testing

The program was tested with:
- Grade boundary values such as 100, 90, 89, 80, 79, 70, 69, 60, 59 and 0
- Invalid marks such as 101 and -1
- Non-numeric input such as `abc`

## Project Files

- `grade_calculator.py` - Main Python program
- `README.md` - Project documentation
- `test_cases.txt` - Testing evidence
