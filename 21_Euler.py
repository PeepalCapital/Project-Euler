#SOLVED by Deepak Venkatesh

#Project Euler Problem 21

amicable_list = []

def sum_divisors(num):
    temp_sum = 0
    for i in range (1, ((num + 1) // 2) + 1):
        if (num % i == 0):
            temp_sum = temp_sum +i
    return temp_sum


for i in range (1, 10000):
    if ((sum_divisors(sum_divisors(i)) == i) and (i != sum_divisors(i))):
        amicable_list.append(i)

print(amicable_list)

sum_amicable_list = 0
for j in range (0, len(amicable_list)):
    sum_amicable_list = sum_amicable_list + amicable_list[j]
print(sum_amicable_list)
