#SOLVED by Deepak Venkatesh

#Project Euler Problem 45

list_penta = []
list_hexa = []
list_tri = []   

for i in range (1, 100000):
    hexa = i * ( (2 * i) - 1)
    penta = i * ( (3 * i) - 1) // 2
    tri = i * (i + 1) // 2
    list_hexa.append(hexa)
    list_penta.append(penta)
    list_tri.append(tri)

set_intersection = set(list_penta) & set(list_hexa) & set(list_tri)
print(set_intersection)
