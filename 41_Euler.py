#SOLVED by Deepak Venkatesh

#Project Euler Problem 41

#Time for execution: 1059.419870376587 ms

from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, (int(n ** 0.5) + 1)):
        if n%i == 0:
            return False
    return True

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
check_list = []

for i in digits:
    temp_list = digits[0:i]
    comb = permutations(temp_list, i)
    for j in comb:
        j_list = list(j)
        concat = ''.join(map(str, j_list))
        if is_prime(int(concat)) == True:
            check_list.append(int(concat))
            
print(max(set(check_list)))
