# Q17: Sum all the items in a given dictionary

marks = {"maths": 85, "physics": 78, "chemistry": 92, "english": 88}
print("Dictionary:", marks)

print("Sum of values:", sum(marks.values()))

# Using a loop
total = 0
for v in marks.values():
    total += v
print("Sum (using loop):", total)
