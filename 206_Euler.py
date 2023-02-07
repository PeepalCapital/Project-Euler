#Project Euler Problem 206

#Time for execution: 152825.90532302856 ms

#Very poor performance. Perhaps a much better way exists to solve this one.

lower = 1020304050607080900
higher = 1929394959697989990
lower_root = int(lower ** 0.5) - 1
higher_root = int(higher ** 0.5) + 1
print(lower_root, higher_root)

char_0 = "1"
char_2 = "2"
char_4 = "3"
char_6 = "4"
char_8 = "5"
char_10 = "6"
char_12 = "7"
char_14 = "8"
char_16 = "9"
char_18 = "0"


for i in range(lower_root, higher_root +1):
    square_num = i * i
    str_square_num = str(square_num)
    if (str_square_num[0] == char_0 and str_square_num[2] == char_2 and str_square_num[4] == char_4 and
        str_square_num[6] == char_6 and str_square_num[8] == char_8 and str_square_num[10] == char_10 and
        str_square_num[12] == char_12 and str_square_num[14] == char_14 and str_square_num[16] == char_16 and
        str_square_num[18] == char_18):
        print(i)
