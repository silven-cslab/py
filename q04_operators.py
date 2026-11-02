# Q4: Demonstrate operators in Python

a, b = 17, 5

print("i) Arithmetic Operators")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

print("\nii) Relational Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\niii) Assignment Operators")
x = 10
print("x = 10        ->", x)
x += 5;  print("x += 5        ->", x)
x -= 3;  print("x -= 3        ->", x)
x *= 2;  print("x *= 2        ->", x)
x /= 4;  print("x /= 4        ->", x)
x = 17
x //= 5; print("x //= 5       ->", x)
x %= 2;  print("x %= 2        ->", x)
x = 3
x **= 3; print("x **= 3       ->", x)
x &= 6;  print("x &= 6        ->", x)
x |= 1;  print("x |= 1        ->", x)
x ^= 2;  print("x ^= 2        ->", x)
x <<= 2; print("x <<= 2       ->", x)
x >>= 1; print("x >>= 1       ->", x)

print("\niv) Logical Operators")
p, q = True, False
print("p and q:", p and q)
print("p or q :", p or q)
print("not p  :", not p)

print("\nv) Bitwise Operators (a=12, b=10)")
m, n = 12, 10
print("m & n  =", m & n)
print("m | n  =", m | n)
print("m ^ n  =", m ^ n)
print("~m     =", ~m)
print("m << 2 =", m << 2)
print("m >> 2 =", m >> 2)

print("\nvi) Ternary Operator")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} ->", status)

print("\nvii) Membership Operators")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits     :", "apple" in fruits)
print("'mango' not in fruits :", "mango" not in fruits)

print("\nviii) Identity Operators")
l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]
print("l1 is l2    :", l1 is l2)
print("l1 is l3    :", l1 is l3)
print("l1 == l3    :", l1 == l3)
print("l1 is not l3:", l1 is not l3)
