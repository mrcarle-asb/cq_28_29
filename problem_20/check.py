"""
Check your answer.  Run this after you think you have the solution.
"""
import hashlib

answer = input("Enter your answer: ").strip()
h = hashlib.sha256(answer.encode()).hexdigest()

if h == "1214aa7ce4dc1d7cf539fe4f2a5a2a415f9d0a0dcef458f124911393e441bd0f":
    print("Correct!")
else:
    print("Not quite -- try again.")
