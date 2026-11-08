# Задание 3. Дан файл, содержащий несколько целых чисел количеством i. Создайте массив
# height длиной i. Каждый элемент массива это вертикальная линия определенной длины.
# Найдите две линии, которые вместе с осью x образуют контейнер, содержащий наибольшее
# количество воды;

with open("heights.txt","r") as file:
    height = list(map(int, file.read().split()))

max_area = 0
for x in range(len(height)):
    for i in range(x + 1, len(height)):

        length = i - x
        min_height = min(height[x], height[i])

        area = min_height * length

        if area > max_area:
            max_area = area

print(max_area)