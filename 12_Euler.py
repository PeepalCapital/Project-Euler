#SOLVED by Deepak Venkatesh

#Project Euler Problem 12

#Time for execution: 371.8836307525635 ms

from collections import Counter 

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

flag = True
i = 1

while flag == True:
    n = i * (i + 1) // 2
    divisor_dict = Counter(prime_factors(n))
    divisor_prime = 1
    for values in divisor_dict.values():
        divisor_prime = divisor_prime * (values + 1)
    if divisor_prime >= 499:
        print(n, divisor_prime)
        flag = False
    i = i + 1
