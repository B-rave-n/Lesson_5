import random
from random import randint
e = int(input(print('Скільски рядків та стовпчиків ми створимо?')))
matrix = []
for i in range(e):
    matrix.append([])
    for j in range(e):
        matrix[i].append(randint(10, 99))
for i in matrix:
    print(i, sep = '\n')
lst = []
index = 0
for i in matrix:
    lst.append(i[index])
    index += 1
print('Максимальне значення допоміжної діагоналі:', max(lst))
print('Мінімальне значення допоміжної діагоналі:', min(lst))
suma = 0
index = 0
for i in matrix[::-1]:
    suma += i[index]
    index += 1
print('Сума чисел головної діагоналі:', suma)
number_of_column = int(input(print('Введи стовпчик, значення якого треба вивести на екран:')))
while number_of_column > e:
    number_of_column = int(input(print('Там немає стількох, їх там всього', e, '. Введи щось адекватне:')))
number_of_column -= 1
for i in matrix:
    print(i[number_of_column])
number_of_line = int(input(print('Тепер введи рядок, значення якого треба вивести на екран:')))
while number_of_line > e:
    number_of_line = int(input(print('Там немає стількох, їх там всього', e, '. Введи щось адекватне:')))
number_of_line -= 1
for i in matrix[number_of_line]:
    print(i, end = ' ')
    print()
number_of_column_1 = int(input(print('Будемо міняти стовпчики місцями. Введи перший номер стовпчика:')))
while number_of_column_1 > e:
    number_of_column_1 = int(input(print('Тобі вже говорили, їх там всього', e, '. Введи щось адекватне:')))
number_of_column_1 -= 1
number_of_column_2 = int(input(print('Тепер введи номер стовпчика, з яким буде заміна:')))
while number_of_column_2 > e:
    number_of_column_2 = int(input(print('Тобі вже говорили, їх там всього', e, '. Введи щось адекватне:')))
number_of_column_2 -= 1
for i in matrix:
    i[number_of_column_1], i[number_of_column_2] = i[number_of_column_2], i[number_of_column_1]
for i in matrix:
    print(i, sep = '\n')
number_of_line_1 = int(input(print('Тепер будемо міняти рядки місцями, введи номер першого рядка:')))
while number_of_line_1 > e:
    number_of_line_1 = int(input(print('Тобі уже казали, їх там всього', e, '. Введи щось адекватне:')))
number_of_line_1 -= 1
number_of_line_2 = int(input(print('Тепер будемо міняти рядки місцями, введи номер першого рядка:')))
while number_of_line_2 > e:
    number_of_line_2 = int(input(print('Тобі уже казали, їх там всього', e, '. Введи щось адекватне:')))
number_of_line_2 -= 1
matrix[number_of_line_1], matrix[number_of_line_2] = matrix[number_of_line_2], matrix[number_of_line_1]
for i in matrix:
    print(i, sep = '\n')
