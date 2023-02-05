#Project Euler Problem 4

#Time for execution: 998.5802173614502 ms

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

list_largest_palindrome = []

for i in range (100, 1000):
    for  j in range (100, 1000):
        product = i * j
        if palindrome(product) == True:
            list_largest_palindrome.append(product)

print(max(list_largest_palindrome))  
