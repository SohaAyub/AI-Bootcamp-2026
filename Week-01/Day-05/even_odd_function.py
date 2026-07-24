"""
Project: Even or Odd Function
Week: 01
Day: 05

Description:
This program checks whether a number is even or odd using a function.

Concepts Covered:
- Functions
- Parameters
- if-else

Learning Objective:
To practice using functions with conditional statements.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

def check_even_odd(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

num = int(input("Enter a Number: "))

print(check_even_odd(num))
