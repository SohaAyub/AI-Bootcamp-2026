"""
Project: Calculator Using Functions
Week: 01
Day: 05

Description:
This program performs basic arithmetic operations using separate functions.

Concepts Covered:
- Functions
- Parameters
- Arguments
- Return Values

Learning Objective:
To learn how functions make programs reusable and organized.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nResults")
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
