"""
Project: Student Marks Manager
Week: 01
Day: 06

Description:
Stores student marks in a list and displays them.

Author: Soha Ayub
Repository: AI-Bootcamp-2026
"""

marks = [85, 90, 78, 92, 88]

print("Student Marks:")
for mark in marks:
    print(mark)

print("\nTotal Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
