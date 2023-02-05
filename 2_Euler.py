#Project Euler Problem 2

t = 0
t1 = 1
t2 = 2
even_sum = 0

while t <= 4000000:
    t = t1 + t2
    if t%2 == 0:
        even_sum = even_sum + t
    else:
        even_sum = even_sum
    t1 = t2
    t2 = t
        
print(even_sum + 2)
