# Задание 5. Выполните задание 4, используя Dict<key, value>. В качестве ключей
# используйте названия месяцев, а в качестве значений – массив температур по дням.
# Напишите функцию, которая используя данные из словаря вычислит среднюю температуру
# для каждого месяца, и вернет словарь(Dict) средних температур (В качестве ключа
# название месяца, в качестве значения коллекция средних температура);

from random import randint

months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]


def get_avarage_temperatures(temperature):
    averages = {}
    for month in temperature.keys():
        averages[month] = sum(temperature[month]) / 30
    return averages


temperature = {}

for x in months:
    month = []

    for i in range(30):
        month.append(randint(0, 31))

    temperature[x] = month

avarage_temperatures = get_avarage_temperatures(temperature)

for key, value in avarage_temperatures.items():
    print(f"Месяц {key}. Средняя температура: {value}")
