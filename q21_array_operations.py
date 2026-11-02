# Q21: Create, display, append, insert and reverse items in an array

from array import array

# Create
arr = array("i", [10, 20, 30, 40])

# Display
print("Array:", arr)
for x in arr:
    print(x, end=" ")
print()

# Append
arr.append(50)
print("After append(50):", arr)

# Insert
arr.insert(2, 25)
print("After insert(2, 25):", arr)

# Reverse
arr.reverse()
print("After reverse():", arr)
