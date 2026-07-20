"""
Project: Type Conversion
Week: 01
Day: 02

Description:
This program demonstrates how to convert data from one type to another
using int(), float(), and str().

Concepts Covered:
- Type Conversion
- int()
- float()
- str()

Learning Objective:
To understand why type conversion is important when taking user input.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

print("=" * 45)
print("      TYPE CONVERSION")
print("=" * 45)

age = int(input("Enter your age: "))
height = float(input("Enter your height (meters): "))

print("\nConverted Values")
print("Age:", age)
print("Height:", height)

number = 100
text = str(number)

print("String Value:", text)
print("Type of text:", type(text))
