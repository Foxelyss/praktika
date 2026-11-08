# Задание 4. Напишите программу, вычисляющую среднюю температуру за год. Создайте
# двумерный рандомный массив temperature 12 на 30, в котором будет храниться
# температура для каждого дня месяца (предполагается, что в каждом месяце 30 дней).
# Сгенерируйте значения температур случайным образом (в рамках разумного). Для каждого
# месяца распечатайте среднюю температуру. Для этого напишите функцию, которая по
# массиву temperature для каждого месяца вычисляет среднюю температуру в нем, и в
# качестве результата возвращает массив средних температур. Полученный массив средних
# температур отсортируйте по возрастанию;

from random import randint


def get_avarage_temperatures(temperature):
    array = []
    for i in range(12):
        array.append(sum(temperature[i]) / 30)
    return array


temperature = []

for _ in range(12):
    month = []
    for i in range(30):
        month.append(randint(0, 31))
    temperature.append(month)

avarage_temperatures = sorted(get_avarage_temperatures(temperature))

print(avarage_temperatures)
