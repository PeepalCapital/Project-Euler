#SOLVED by Deepak Venkatesh

#Project Euler Problem 80

#Time for execution: 6.360054016113281 ms

import numpy as np
from decimal import *
getcontext().prec = 150

def perfect_square(n):
    sq_root = np.sqrt(n)
    if sq_root - int(sq_root) == 0:
        return True
    else:
        return False

natural = []
irrational = []
digit_sums = []

for i in range (1, 101):
    natural.append(i)
for j in natural:
    if perfect_square(j) == False:
        irrational.append(j)
for k in irrational:
    a = Decimal(k).sqrt()
    c = int(a * (10**100))
    d = str(c)
    e = d[0:100]
    digitalsum = 0
    for m in range(0, len(e)):
        digitalsum = digitalsum + int(e[m])
    digit_sums.append(digitalsum)

print(sum(digit_sums))
