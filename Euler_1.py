sum_three = 0
sum_five = 0
sum_fifteen = 0

for i in range (1, 1000):
    if i%3 == 0:
        sum_three = sum_three + i
    else:
        sum_three = sum_three 
        
for j in range (1, 1000):
    if j%5 == 0:
        sum_five = sum_five + j
    else:
        sum_five = sum_five  
        
for k in range (1, 1000):
    if k%15 == 0:
        sum_fifteen = sum_fifteen + k
    else:
        sum_fifteen = sum_fifteen 
        
total_sum = sum_three + sum_five - sum_fifteen
print(total_sum)
