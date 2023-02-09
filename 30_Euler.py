#SOLVED by Deepak Venkatesh

#Project Euler Problem 30

#this is not the correct way to solve it. not at all a good way. but gets the job done

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
