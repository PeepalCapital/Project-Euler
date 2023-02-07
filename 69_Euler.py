#SOLVED by Deepak Venkatesh

#Project Euler Problem 69

#Time for execution: 15682.605743408203 ms

#This problem actually doesn't require code to solve it. I also think this problem's difficulty rating should be reduced.
#Euler's totient function can be used. n/phi(n) needs to be maximised.
#This leads to maximising the reciprocal of (1 - 1/p1) * (1 - 1/p2) * ... (1 - 1/pi).
#This is simply maximising each value of 'p'. The number n can be got as n = p1 * p2 * p3 .... pi where pi is the prime where n remains under a million.
#So n = 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510. Note if we multiply by 19 next the value of n crosses a million to 9699690 which is more than a million.

#Suppose the question was to find instead of maximum of n/phi(n) but to find minimum of n/phi(n) how would you do it? I doesn't require code again.
#In fact it's even simpler.

#Anyways a brute force code in python is also below. Please excuse the code as I am a newbie in coding/ds/algo.



def unique_prime_factors(n):
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
    return list(set(factors))


n_by_phi_list = []

for i in range (2, 20):
    list_prime_factors = unique_prime_factors(i)
    n_by_phi = 1
    for j in range (0, len(list_prime_factors)):
        term = 1 / (1 - (1 / list_prime_factors[j]))
        n_by_phi = n_by_phi * term
    n_by_phi_list.append(n_by_phi)

print(n_by_phi_list)
index = n_by_phi_list.index(min(n_by_phi_list)) + 2
print(index)
