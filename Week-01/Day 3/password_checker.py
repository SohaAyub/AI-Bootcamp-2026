"""
Project: Password Checker
Week: 01
Day: 03

Description:
Checks whether the entered password matches the predefined password.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

correct_password = "python123"

password = input("Enter Password: ")

if password == correct_password:
    print("Login Successful")
else:
    print("Incorrect Password")
