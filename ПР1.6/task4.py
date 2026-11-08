# Задание 4. Вводятся положительные числа. Определите сумму чисел, делящихся на
# положительное число a нацело. При вводе отрицательного числа закончите работу;

a = int(input("Введите a: "))
print("Введите числа(отрицательное число = стоп):")

positive_number = 0
sum_positive_number = 0

while positive_number >= 0:
    if positive_number % a == 0:
        sum_positive_number += positive_number
    positive_number = int(input())

print("Сумма положительных и кратных числу а чисел:\n"+ str(sum_positive_number))
