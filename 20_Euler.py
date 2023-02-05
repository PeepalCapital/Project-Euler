#Project Euler Problem 20

#Time for execution: 0.5850791931152344 ms

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n - 1))

digit_sum = 0
output_factorial = factorial(100)
string_output_factorial = str(output_factorial)

for i in range(0, len(string_output_factorial)):
    digit = string_output_factorial[i]
    digit_sum = digit_sum + int(digit)

print(digit_sum)
