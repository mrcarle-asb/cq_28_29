"""
CodingQuest Problem 20: Tic tac toe

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line represents one game of tic-tac-toe.
The numbers on each line are the squares played, in order (X goes first).
Squares are numbered like this:

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Process each game until someone wins (3 in a row), then stop.
If nobody wins after 9 moves, it's a draw.

Your answer is: (games won by X) * (games won by O) * (drawn games)

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
