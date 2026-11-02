# Q19: Print each line of a file in reverse order

import os

src = "input.txt"

# Create a sample input file if none exists
if not os.path.exists(src):
    with open(src, "w") as f:
        f.write("Hello World\nPython Programming\nSkill Enhancement Course\n")

with open(src, "r") as f:
    for line in f:
        print(line.rstrip("\n")[::-1])
