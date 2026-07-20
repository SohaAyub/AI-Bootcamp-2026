"""
Project: Simple Calculator
Week: 01
Day: 02

Description:
This Python program is a simple calculator that takes two numbers from the
user and performs basic arithmetic operations, including addition,
subtraction, multiplication, division, modulus, floor division, and
exponentiation (power).

The project helps beginners understand how arithmetic operators work and how
user input can be converted into numerical data using type conversion.

Concepts Covered:
- Variables
- User Input (input())
- Type Conversion (float())
- Arithmetic Operators
- Formatted Output

Learning Objective:
To learn how to perform mathematical calculations using Python and understand
the importance of converting user input into numeric data types before
performing operations.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

print("=" * 45)
print("      SIMPLE PYTHON CALCULATOR")
print("=" * 45)

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n===== RESULTS =====")

# Arithmetic Operations
print("Addition (+):", num1 + num2)
print("Subtraction (-):", num1 - num2)
print("Multiplication (*):", num1 * num2)

# Division
if num2 != 0:
    print("Division (/):", num1 / num2)
    print("Floor Division (//):", num1 // num2)
    print("Modulus (%):", num1 % num2)
else:
    print("Division (/): Cannot divide by zero")
    print("Floor Division (//): Cannot divide by zero")
    print("Modulus (%): Cannot divide by zero")

# Exponentiation
print("Power (**):", num1 ** num2)

print("=" * 45)
print("Thank you for using the Python Calculator!")
print("=" * 45)
