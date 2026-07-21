"""
Project: Even or Odd Checker
Week: 01
Day: 03

Description:
This program checks whether a number entered by the user is even or odd.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
