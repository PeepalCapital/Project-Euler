#Project Euler Problem 10

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, (int(n ** 0.5) + 1)):
        if n%i == 0:
            return False
    return True

limit = 2000000
sum_primes = 0
j = 0

while j < limit:
    if is_prime(j):
        sum_primes = sum_primes + j
    else:
        sum_primes = sum_primes
    j += 1
        
print(sum_primes)
