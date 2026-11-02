# Q20: Count characters, words and lines in a file

import os

src = "input.txt"

# Create a sample input file if none exists
if not os.path.exists(src):
    with open(src, "w") as f:
        f.write("Hello World\nPython Programming\nSkill Enhancement Course\n")

with open(src, "r") as f:
    content = f.read()

chars = len(content)
words = len(content.split())
lines = len(content.splitlines())

print("Characters:", chars)
print("Words     :", words)
print("Lines     :", lines)
