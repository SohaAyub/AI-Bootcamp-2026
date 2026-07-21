"""
Project: Positive or Negative Number Checker
Week: 01
Day: 03

Description:
Checks whether the entered number is positive, negative, or zero.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

number = float(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")
