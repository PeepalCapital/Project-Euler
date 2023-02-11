#SOLVED by Deepak Venkatesh

#Project Euler Problem 46

#This is a scrappy solution but gets the job done.

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, (int(n ** 0.5) + 1)):
        if n%i == 0:
            return False
    return True

def prime_till_n(n):
    list_prime = []
    for j in range (0, n):
        if is_prime(j) == True:
            list_prime.append(j)
    return list_prime

def is_perfect_square(n):
    square_root = int(n**0.5)
    if square_root**2 == n:
        return True
    else:
        return False

primes =  [2]
all_odd_composite = []
satisfy = []
k = 10000

for i in range(1, k):
    number = 2 * i + 1
    if is_prime(number) == True:
        primes.append(number)
    else:
        all_odd_composite.append(number)
        for j in range(0, len(primes)):
            diff = number - primes[j]
            even_term = diff * 0.5
            if is_perfect_square(even_term) == True:
                satisfy.append(number)
                diff = 0
                even_term = 0
            else:
                pass

test = set(all_odd_composite) - set(satisfy)
print(test)
