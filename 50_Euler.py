#SOLVED by Deepak Venkatesh

#Project Euler Problem 50

#Just a scrappy solution to arrive at the answer. But it's effective

import numpy as np

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

prime_list = prime_till_n(3947)
length = len(prime_list)
k = 0
sigma_list = []
series_list = []


for i in range(0, length):
    for j in range(length, 0, -1):
        new_list = prime_list[i:j]
        if is_prime(sum(new_list)) == True:
            sigma_list.append(sum(new_list))
            series_list.append(len(new_list))

print(len(series_list))
print(len(sigma_list))

max_value_loc = np.argmax(series_list)
consecutive_prime = sigma_list[max_value_loc]
print(consecutive_prime)
