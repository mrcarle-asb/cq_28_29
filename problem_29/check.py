"""
Check your answer.  Run this after you think you have the solution.
"""
import hashlib

answer = input("Enter your answer: ").strip()
h = hashlib.sha256(answer.encode()).hexdigest()

if h == "d57d82621c05a35d04475a369b6ebeb3712bd0fa462f66d7f78fd0e1254f7b94":
    print("Correct!")
else:
    print("Not quite -- try again.")
