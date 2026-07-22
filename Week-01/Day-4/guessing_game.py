"""
Project: Number Guessing Game
Week: 01
Day: 04

Description:
This program asks the user to guess a secret number until the correct number
is entered.

Concepts Covered:
- while loop
- if statement
- User Input

Learning Objective:
To combine loops and conditions in a simple interactive game.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

secret_number = 7

guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it correctly.")
    else:
        print("❌ Wrong guess. Try again.")
