"""
Project: Password Retry System
Week: 01
Day: 04

Description:
This program gives the user three attempts to enter the correct password.
If the password is entered correctly, login is successful. Otherwise,
the account is locked.

Concepts Covered:
- while loop
- if statement
- Counter
- User Input

Learning Objective:
To learn how loops can limit user attempts in login systems.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

correct_password = "python123"

attempts = 3

while attempts > 0:

    password = input("Enter Password: ")

    if password == correct_password:
        print("✅ Login Successful!")
        break

    else:
        attempts -= 1
        print("❌ Incorrect Password")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\n🔒 Account Locked!")
