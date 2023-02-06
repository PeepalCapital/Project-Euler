#Project Euler Problem 53

#Time for execution: 95.08800506591797 ms

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

count = 0

for n in range (1, 101):
    for r in range (1, n + 1):
        numerator = factorial(n)
        denominator = factorial(n - r) * factorial(r)
        result = numerator / denominator
        if result >= 1000000:
            count = count + 1
print(count)
