import random
from random import randint

matrix = []
for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(randint(10, 99))
for i in matrix:
    print(i, sep = '\n')
suma = 0
index1 = 0
for i in matrix[::-1]:
    suma += i[index1]
    index1 += 1
print(suma)


