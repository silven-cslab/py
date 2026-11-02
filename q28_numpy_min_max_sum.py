# Q28: Min, max, sum and cumulative sum of an array

import numpy as np

arr = np.array([5, 3, 8, 1, 9, 2])
print("Array:", arr)

print("Min           :", arr.min())
print("Max           :", arr.max())
print("Sum           :", arr.sum())
print("Cumulative sum:", arr.cumsum())

m = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array:\n", m)
print("Sum of columns (axis=0):", m.sum(axis=0))
print("Sum of rows    (axis=1):", m.sum(axis=1))
print("Cumulative sum (axis=1):\n", m.cumsum(axis=1))
