# Temperature Converter

## Description
A Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin. It uses separate functions for each conversion and displays results neatly to two decimal places.

## Features
- Converts between Celsius, Fahrenheit, and Kelvin.
- Uses six separate conversion functions.
- Validates user input and temperature units.
- Rejects temperatures below absolute zero.
- Handles non-numeric inputs.
- Formats results to two decimal places.
- Supports converting a temperature to the same unit.

## Conversion Formulas
- Celsius to Fahrenheit: `(C × 9/5) + 32`
- Fahrenheit to Celsius: `(F − 32) × 5/9`
- Celsius to Kelvin: `C + 273.15`
- Kelvin to Celsius: `K − 273.15`
- Fahrenheit to Kelvin: `(F − 32) × 5/9 + 273.15`
- Kelvin to Fahrenheit: `(K − 273.15) × 9/5 + 32`

## Requirements
- Python 3.x
- No external libraries required.

## How to Run
1. Save the program as `temperature_converter.py`.
2. Open a terminal in the project folder.
3. Run the command:

   `python temperature_converter.py`

## Example Output
```text
Temperature Converter
Units: C = Celsius, F = Fahrenheit, K = Kelvin
Enter temperature: 37
Convert from (C/F/K): C
Convert to (C/F/K): F
Converted temperature: 98.60 F
```

## Concepts Used
- Functions
- Dictionaries
- Conditional statements
- User input and output
- Exception handling
- String formatting with f-strings

## Purpose
This project demonstrates how to organize Python code using reusable functions, validate user input, and perform mathematical calculations accurately.
