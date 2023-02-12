#SOLVED by Deepak Venkatesh

#Project Euler Problem 12

#Scrappy solution and had to do 8 iterations of ranges. Not an intelligent method to solve

def generate_collatz(n):
    collatz_list = []
    collatz_list.append(n)
    flag = True
    while flag == True:
        if n == 1:
            flag = False
        elif n % 2 == 0:
            n = n // 2
            collatz_list.append(n)
        elif n % 2 != 0:
            n = (3 * n) + 1
            collatz_list.append(n)
    return collatz_list

c = 0
max_chain = []
max_i = []

for i in range (1000000, 800000, -1):
    a = generate_collatz(i)
    b = len(a)
    max_chain.append(b)
    c = a[0]
    max_i.append(c)


print(max_chain)
print(max_i)


max_value = max(max_chain)
max_index = max_chain.index(max_value)

print(max_index)
collatz_start_max = max_i[max_index]
print(collatz_start_max)

#129-871 
#3829-6171
#22969-77031
#43841-156159
#169369-230631
#88065-511935
#173669-626331
#162201-837799
