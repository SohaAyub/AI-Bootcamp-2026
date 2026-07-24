"""
Project: Factorial Calculator
Week: 01
Day: 05

Description:
This program calculates the factorial of a number using a function.

Concepts Covered:
- Functions
- Loops
- Return Statement

Learning Objective:
To combine functions with loops for mathematical calculations.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

num = int(input("Enter a Positive Number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(num))
