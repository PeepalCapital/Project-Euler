#Project Euler Problem 9

#This is too much of a brute force. 

for a in range (1, 1001):
    for b in range (1, 1001):
        for c in range (1, 1001):
            if (a*a + b*b - c*c) == 0:
                if a + b + c == 1000:
                    print(a, b, c)
                    print(a*b*c)
