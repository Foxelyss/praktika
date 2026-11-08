# Задание 5. Дана прямоугольная матрица a, имеющей n строк и m столбцов. Исходная
# матрица состоит из нулей и единиц. Добавьте к матрице еще один столбец, каждый
# элемент которого делает количество единиц в каждой строке четным;

from random import randint

def print_matrice(matrice):
    for x in matrice:
        print(*x,sep='\t')


a = []
n = randint(2, 6)
m = randint(2, 6)

for y in range(n):
    row = []
    for x in range(m):
        row.append(randint(0, 1))
    a.append(row)

print("Изначанальная матрица")
print_matrice(a)

for y in range(n):
    value_to_add = 1 if sum(a[y]) % 2 != 0 else 0
    a[y].append(value_to_add)

print("Матрица с чётным количеством единиц:")
print_matrice(a)
