#SOLVED by Deepak Venkatesh

#Project Euler Problem 29

power_list = []
for a in range (2, 101):
    for b in range (2, 101):
        term = a ** b
        power_list.append(term)
print(len(set(power_list)))
