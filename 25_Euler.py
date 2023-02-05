#Project Euler Problem 25

#Time for execution: 963.9558792114258 ms

def fib(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        f1 = 1
        f2 = 1
        for i in range (0, n-2):
            f = f1 + f2
            f1 = f2
            f2 = f
        return f
                
j = 1
while len(str(fib(j))) < 1000:
    j = j + 1
    
print(j)
