"""
Project: Maximum Number Finder
Week: 01
Day: 05

Description:
This program finds the largest number between two numbers using a function.

Concepts Covered:
- Functions
- Parameters
- if-else

Learning Objective:
To learn decision-making inside functions.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

def maximum(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both numbers are equal"

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Largest Number:", maximum(num1, num2))
