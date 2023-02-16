#SOLVED by Deepak Venkatesh

#Project Euler Problem 92

#Time for execution: 105830.17230033875 ms

#A much better method via cache and limited but all possible permutations will be a solve in a few milli seconds. Below is brute force.

from collections import Counter 

def square_digit(n):
    a = str(n)
    sum_square_a = 0
    for i in range (0, len(a)):
        sq_digit = int(a[i]) * int(a[i])
        sum_square_a = sum_square_a + sq_digit
    return sum_square_a

def count_termination(n):        
    if n == 1:
        return 1
    if n == 89:
        return 89
    else:
        a = square_digit(n)
        return count_termination(a)
        
i = 1
series_list = []

while i < 10000000:
    a = count_termination(i)
    series_list.append(a)
    i = i + 1

print(Counter(series_list))
