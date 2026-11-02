# Q25: NumPy array creation using the array() function

import numpy as np

a1 = np.array([1, 2, 3, 4, 5])                   # 1-D
a2 = np.array([[1, 2, 3], [4, 5, 6]])            # 2-D
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3-D
a4 = np.array([1, 2, 3], dtype=float)            # with dtype
a5 = np.array((10, 20, 30))                      # from a tuple

print("1-D array:\n", a1)
print("2-D array:\n", a2)
print("3-D array:\n", a3)
print("Float array:", a4)
print("From tuple :", a5)
