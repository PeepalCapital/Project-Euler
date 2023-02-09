#SOLVED by Deepak Venkatesh

#Project Euler Problem 30

#Time for execution: 27547.89400100708 ms

#For each number of digits the maximum limit will be the number of digits * 9^5.
#Max Limit - Lowest Number Possible - Highest Number Possible - (Highest - Max Limit)
#max limit	lowest	highest	
#59049	0	9	-59040
#118098	10	99	-117999
#177147	100	999	-176148
#236196	1000	9999	-226197
#295245	10000	99999	-195246
#354294	100000	999999	645705
#413343	1000000	9999999	9586656
#472392	10000000	99999999	99527607
#531441	100000000	999999999	999468558

#so we can check up to 999,999 as the number for the power of 5


def n_power_digit_sum(n,p):
    string_n = str(n)
    digit_sum = 0
    for i in string_n:
        term = int(i) ** p 
        digit_sum = digit_sum + term
    return digit_sum
list_trial = []
for i in range (0, 10000000):
    term = n_power_digit_sum(i, 5)
    if i == term:
        list_trial.append(i)
    
print(list_trial) 
print(sum(list_trial) - 1)
