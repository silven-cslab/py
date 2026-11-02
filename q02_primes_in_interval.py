# Q2: Display all prime numbers within an interval

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

print(f"Prime numbers between {lower} and {upper}:")
for num in range(max(lower, 2), upper + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
