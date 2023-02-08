#Feel a little bit stupid in my approach. The solution was to go 'n' rights and 'n' downs in a n by n matrix.
#Paths = (2n)! / (n!)^2
#But since I wanted to put it in code it took me days to solve this!

#Clean code with Permutations & Combination approach

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

result = factorial(40) / (factorial(20) ** 2)
print(result)

#And here is my silly code which counts for every right move possibilities into next column and keeps summing them up. 

#Project Euler Problem 15

#Time for execution: 0.9129047393798828 ms

square_sides = 20 # for equal to 2 or above sides of squares

rows =  square_sides
columns = square_sides

summation_list = []
sigma_list = []

for m in range (1, rows + 2):
    sigma_list.append(0)

for i in range (1, rows + 2):
    summation_list.append(i)

for k in range (0, columns - 2):    
    for j in range (0, len(summation_list)):
        sigma = sum(summation_list[0:j+1])
        sigma_list[j] = sigma
    for n in range(0, len(sigma_list)):
        summation_list[n] = sigma_list[n]    

final_sum = sum(summation_list)

print(final_sum)
