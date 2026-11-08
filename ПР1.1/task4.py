# Задание 4. Напишите функцию, которая заполняет список случайными числами в диапазоне,
# указанном пользователем. Функция принимает начало диапазона и его конец, и возвращает
# целочисленный массив. С помощью специальной формы цикла for выведете элементы
# получившегося массива с добавление индекса. Например: 0 –> 29;

from random import randint


def generate_array_of_random_int(start, end):
    array = [randint(start, end) for _ in range(10)]
    return array


start, end = int(input()), int(input())
save = generate_array_of_random_int(start, end)

for i in range(10):
    print(f"{i} -> {save[i]}")
