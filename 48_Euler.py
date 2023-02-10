#SOLVED by Deepak Venkatesh

#Project Euler Problem 48

intermediate_sigma = 0
for i in range (1, 101):
    series = i**i
    intermediate_sigma = intermediate_sigma + series

last_ten_intermediate_sigma = intermediate_sigma % 10**10

new_intermediate_sigma = 0
for j in range (101, 1000):
    j_last_ten = (j**j) % 10**10
    new_intermediate_sigma = new_intermediate_sigma + j_last_ten

new_last_ten_intermediate_sigma =  new_intermediate_sigma % 10**10

ten_digits = new_last_ten_intermediate_sigma + last_ten_intermediate_sigma
result = ten_digits % 10**10

print(result)
