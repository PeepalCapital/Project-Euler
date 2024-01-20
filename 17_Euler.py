#SOLVED by Deepak Venkatesh

#Project Euler Problem 17

num_dict = {
    0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
    10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 7
}

sum_teens = 0
for a in range (1, 20):
    sum_teens = sum_teens + num_dict[a]
    
#print(sum_teens)

sum_twodigits = 0
for b in range (20, 100):
    if (b % 10 == 0):
        sum_twodigits = sum_twodigits + num_dict[b]
    else:
        sum_twodigits = sum_twodigits + num_dict[b % 10]
        sum_twodigits = sum_twodigits + num_dict[b - (b % 10)]

#print(sum_twodigits)

sum_threedigits_teens = 0
for d in range (100, 120):
    if (d == 100):
        sum_threedigits_teens = sum_threedigits_teens + 10
    if (d >= 101 and d < 110):
        sum_threedigits_teens = sum_threedigits_teens + num_dict[d % 10] + 13
    if (d >= 110 and d < 120):
        sum_threedigits_teens = sum_threedigits_teens + num_dict[d % 100] + 13
    


sum_threedigits = 0
for c in range (120, 1000):
    if (c % 100 == 0):
        sum_threedigits = sum_threedigits + num_dict[c // 100] + num_dict[100]
    else:
        sum_threedigits = sum_threedigits + num_dict[c // 100] + num_dict[100] + 3
        if (c % 100) < 20:
            sum_threedigits = sum_threedigits + num_dict[c % 100]
        else:
            sum_threedigits = sum_threedigits + num_dict[c % 100 - c % 10] + num_dict[c % 10]
        
        
    
        
        
total_sum = sum_teens + sum_twodigits + sum_threedigits_teens + sum_threedigits + 11
print(total_sum)        
