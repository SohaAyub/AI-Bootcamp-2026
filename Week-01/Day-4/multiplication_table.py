"""
Project: Multiplication Table
Week: 01
Day: 04

Description:
This program prints the multiplication table of a number entered by the user.

Concepts Covered:
- for loop
- input()
- range()

Learning Objective:
To practice loops by generating multiplication tables.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}\n")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
