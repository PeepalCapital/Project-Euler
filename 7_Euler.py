#Project Euler Problem 7

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, (int(n ** 0.5) + 1)):
        if n%i == 0:
            return False
    return True

count = 0
input_number = 0

while count < 10001:
    if is_prime(input_number) == True:
        count = count + 1
    input_number = input_number + 1
        

print(input_number - 1)
