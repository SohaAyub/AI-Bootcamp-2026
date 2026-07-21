"""
Project: Student Grade Calculator
Week: 01
Day: 03

Description:
Calculates the student's grade based on marks.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 50:
    print("Grade: D")

else:
    print("Fail")
