# Q18: Sort words in a file and write them (lower-cased) to another file

import os

src = "input.txt"
dst = "sorted_output.txt"

# Create a sample input file if none exists
if not os.path.exists(src):
    with open(src, "w") as f:
        f.write("Banana apple Cherry\nZebra mango Apple\norange Grape\n")

with open(src, "r") as f:
    words = f.read().split()

words = sorted(w.lower() for w in words)

with open(dst, "w") as f:
    f.write("\n".join(words))

print(f"Sorted {len(words)} words written to {dst}:")
print(words)
