#SOLVED by Deepak Venkatesh

#Project Euler Problem 36

def palindrome(n):
    str_n = str(n)
    len_str = len(str_n)
    list_palindrome = []
    list_reverse_palindrome = []
    for i in range (0, len_str):
        char_palindrome = str_n[i]
        list_palindrome.append(char_palindrome)
    list_reverse_palindrome = list_palindrome[::-1]
    if list_palindrome == list_reverse_palindrome:
        return True
    else:
        return False

def binary(n):
    bin_a = str(bin(n))
    binary_a = bin_a[2:]
    final = int(binary_a)
    return final
    
list_num = []

for i in range (0, 1000000):
    if palindrome(i) == True and palindrome(binary(i)) == True:
        list_num.append(i)

print(sum(list_num))
print(list_num)
