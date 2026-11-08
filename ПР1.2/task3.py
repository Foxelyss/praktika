# Задание 3. Заполните квадратную матрицу n x n так, чтобы все числа первого столбца и
# первой строки равны 1, а каждое из оставшихся чисел равно сумме верхнего и левого
# соседей. Выведите на экран получившеюся матрицу;

matrice = []

n = 5

for x in range(n):
    array = []
    for y in range(n):
        array.append(1)
    matrice.append(array)

for x in range(1, n):
    for y in range(1, n):
        matrice[x][y] = matrice[x - 1][y] + matrice[x][y - 1]

for x in matrice:
    print(*x, sep='\t')
