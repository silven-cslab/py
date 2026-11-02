# Q7: Function with multiple return values

def arithmetic(a, b):
    """Returns sum, difference, product and quotient as a tuple."""
    return a + b, a - b, a * b, a / b


s, d, p, q = arithmetic(20, 4)
print("Sum        :", s)
print("Difference :", d)
print("Product    :", p)
print("Quotient   :", q)

result = arithmetic(9, 3)
print("Returned as tuple:", result)
