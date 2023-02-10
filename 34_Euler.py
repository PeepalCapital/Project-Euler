#SOLVED by Deepak Venkatesh

#Project Euler Problem 34

#Time for execution: 4517.972946166992 ms

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

def digit_factorial_sum(n):
    string = str(n)
    temp_sum = 0
    for i in string:
        temp_sum = temp_sum + factorial(int(i))
    return temp_sum

curious = []
for i in range(0, 1000000):
    test = i - digit_factorial_sum(i)
    if test == 0:
        curious.append(i)
print(sum(curious[2:]))
