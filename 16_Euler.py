#Project Euler Problem 16

#Time for execution: 0.6730556488037109 ms

power = pow(2,1000)
str_power = str(power)
power_digit_sum = 0

for i in range (0, len(str_power)):
    power_digit_sum = power_digit_sum + int(str_power[i])

print(power_digit_sum)
