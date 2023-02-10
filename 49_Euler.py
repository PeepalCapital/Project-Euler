#SOLVED by Deepak Venkatesh

#Project Euler Problem 49

#Just a scrappy solution to arrive at the answer. But it's effective

from itertools import permutations

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

four_digit_prime_list = prime_till_n(10000)[169:]
check_list = []
minus_list = []

for j in four_digit_prime_list:
    a = permutations(str(j))
    for i in a:
        number = i[0] + i[1] + i[2] + i[3]
        test = int(number)
        if is_prime(test) == True:
            check_list.append(int(number))
            for k in check_list:
                if len(str(k)) < 4:
                    check_list.remove(k)
    check_list.sort()
    for a in check_list:
        t1 = a + 3330
        if t1 in check_list:
            t2 = a + 6660
            if t2 in check_list:
                print(set(check_list))
        t1 = 0
        t2 = 0
    check_list.clear()
