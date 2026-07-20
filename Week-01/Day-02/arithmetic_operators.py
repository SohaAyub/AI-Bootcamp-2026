"""
Project: Arithmetic Operators
Week: 01
Day: 02

Description:
This program demonstrates the use of arithmetic operators in Python.
It performs addition, subtraction, multiplication, division, floor
division, modulus, and exponentiation using two user-provided numbers.

Concepts Covered:
- Arithmetic Operators
- User Input
- Variables
- Type Conversion

Learning Objective:
To understand how mathematical operations are performed in Python.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

print("=" * 45)
print("      ARITHMETIC OPERATORS")
print("=" * 45)

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\nResults")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Cannot divide by zero.")

print("Power:", num1 ** num2)
