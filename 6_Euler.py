#Project Euler Problem 6

#Time for execution: 2.254009246826172 ms

square_of_sum = 0
sum_of_square = 0
for i in range (1, 101):
    squares = i * i
    sum_of_square = sum_of_square + squares
    for j in range (1, 101):
        product = i * j
        square_of_sum = square_of_sum + product

print(square_of_sum - sum_of_square)
