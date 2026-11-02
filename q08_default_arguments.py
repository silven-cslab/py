# Q8: Function using default arguments

def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}!")


def power(base, exponent=2):
    return base ** exponent


greet()                       # both defaults
greet("Alice")                # default greeting
greet("Bob", "Good morning")  # no defaults
greet(greeting="Welcome")     # keyword argument

print("power(5)    =", power(5))
print("power(2, 5) =", power(2, 5))
