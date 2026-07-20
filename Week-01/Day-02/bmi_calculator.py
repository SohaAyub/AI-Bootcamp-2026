"""
Project: BMI Calculator
Week: 01
Day: 02

Description:
This Python program calculates the Body Mass Index (BMI) of a user based on
their weight and height. The program accepts user input, performs the BMI
calculation using the standard formula, and displays the result.

Concepts Covered:
- Variables
- User Input (input())
- Type Conversion (float())
- Arithmetic Operators
- Mathematical Formula
- Formatted Output

Learning Objective:
To understand how mathematical formulas can be implemented in Python while
practicing user input, arithmetic operations, and type conversion.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

print("=" * 45)
print("         BMI CALCULATOR")
print("=" * 45)

# User Input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

# BMI Formula
bmi = weight / (height ** 2)

print("\n===== RESULT =====")
print("Your BMI is:", round(bmi, 2))

print("=" * 45)
print("Thank you for using the BMI Calculator!")
print("=" * 45)
