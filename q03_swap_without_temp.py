# Q3: Swap two numbers without using a temporary variable

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Before swap: a =", a, ", b =", b)

# Method 1: arithmetic
a = a + b
b = a - b
a = a - b
print("After swap (arithmetic): a =", a, ", b =", b)

# Method 2: tuple unpacking (swaps back)
a, b = b, a
print("After swap (tuple unpacking): a =", a, ", b =", b)

# Method 3: XOR (swaps again)
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap (XOR): a =", a, ", b =", b)
