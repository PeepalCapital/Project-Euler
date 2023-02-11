#SOLVED by Deepak Venkatesh

#Project Euler Problem 39

#This is a scrappy solution but gets the job done.

perimeter = []
for c in range(1, 501):
    for a in range(1, 501):
        for b in range(1, 501):
            term = a * a + b * b - c * c
            if term == 0:
                p = a + b + c
                if p <= 1000:
                    perimeter.append(p)
freq = []
for i in perimeter:
    frequency = perimeter.count(i)
    if i <= 1000:
        freq.append(frequency)
        print(frequency, i)
print(max(freq))
