"""
Check your answer.  Run this after you think you have the solution.
"""
import hashlib

answer = input("Enter your answer: ").strip()
h = hashlib.sha256(answer.encode()).hexdigest()

if h == "f08b3bd8029bbe43fe921048288df01a36f04ac50db61575174717756321c9c0":
    print("Correct!")
else:
    print("Not quite -- try again.")
