"""
Check your answer.  Run this after you think you have the solution.
"""
import hashlib

answer = input("Enter your answer: ").strip()
h = hashlib.sha256(answer.encode()).hexdigest()

if h == "795730d7f5ffe95c2d3b4ad5b5dfbdc44298e33fb83ebaad59865de8655b73ec":
    print("Correct!")
else:
    print("Not quite -- try again.")
