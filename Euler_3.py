#Project Euler Problem 3

def max_prime_factor(n):
    i = 2
    while i <= (int(n ** 0.5) + 1):
        if n%i:
            i +=1
        else:
            n //= i
    return n

print(max_prime_factor(600851475143))
