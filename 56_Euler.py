#SOLVED by Deepak Venkatesh

#Project Euler Problem 56

#Time for execution: 169.09003257751465 ms

def digit_sum(n):
    string_n = str(n)
    sum_string = 0
    for i in range (0, len(string_n)):
        sum_string = sum_string + int(string_n[i])
    return sum_string

digit_sum_list = []

for a in range (0, 100):
    for b in range (0, 100):
        compute = pow(a, b)
        compute_digitsum = digit_sum(compute)
        digit_sum_list.append(compute_digitsum)
set_digit_sum_list = set(digit_sum_list)
print(max(set_digit_sum_list))
