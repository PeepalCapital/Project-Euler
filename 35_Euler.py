#Project Euler Problem 35

#Time for execution: 8776.46517753601 ms

def reverse_string(n):
    string = str(n)
    reverse_list = []
    for i in string:
        new_string = string[len(string) - 1] + string[0:len(string) - 1]
        reverse_list.append(new_string)
        string = new_string
    return reverse_list

def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, (int(n ** 0.5) + 1)):
        if n%i == 0:
            return False
    return True

def prime_till_n(n):
    list_prime = []
    for j in range (0, n):
        if is_prime(j) == True:
            list_prime.append(j)
    return list_prime

prime_list = prime_till_n(1000000)
circluar_primes_list = []

for i in prime_list:
    check_string = reverse_string(i)
    check_prime_list = []
    for j in check_string:
        check_prime = int(j)
        if is_prime(check_prime) == True:
            check_prime_list.append(0)
        else:
            check_prime_list.append(1)
    if sum(check_prime_list) == 0:
        for k in check_string:
            circluar_primes_list.append(k)
        
count_circluar_primes = len(set(circluar_primes_list))
print(set(circluar_primes_list))
print(count_circluar_primes)
