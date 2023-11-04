#SOLVED by Deepak Venkatesh

#Project Euler Problem 52

control_variable = 1
test_num = 1

while control_variable == 1:
    double_num = 2 * test_num
    three_num = 3 * test_num
    four_num = 4 * test_num
    five_num = 5 * test_num
    six_num = 6 * test_num

    test_num_list = []
    test_num_str = str(test_num)

    for i in range (0, len(test_num_str)):
        temp_list = test_num_str[i]
        test_num_list.append(temp_list)

    double_num_list = []
    double_num_str = str(double_num)

    for i in range (0, len(double_num_str)):
        temp_list_double = double_num_str[i]
        double_num_list.append(temp_list_double)  
    
    three_num_list = []
    three_num_str = str(three_num)

    for i in range (0, len(three_num_str)):
        temp_list_three = three_num_str[i]
        three_num_list.append(temp_list_three)

    four_num_list = []
    four_num_str = str(four_num)

    for i in range (0, len(four_num_str)):
        temp_list_four = four_num_str[i]
        four_num_list.append(temp_list_four)
    
    five_num_list = []
    five_num_str = str(five_num)

    for i in range (0, len(five_num_str)):
        temp_list_five = five_num_str[i]
        five_num_list.append(temp_list_five)
    
    six_num_list = []
    six_num_str = str(six_num)

    for i in range (0, len(six_num_str)):
        temp_list_six = six_num_str[i]
        six_num_list.append(temp_list_six)

    if set(test_num_list) == set(double_num_list) == set(three_num_list) == set(four_num_list) == set(five_num_list) == set(six_num_list):
        control_variable = 0
    else:
        control_variable = 1
    test_num += 1
    
 
print(test_num - 1)
