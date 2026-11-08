# Задание 1. Дано целое положительное число n. Вычислите произведение натуральных
# чисел, кратных трём и не превышающим число n;

n = int(input())

multiplication = 1

for x in range(0, n + 1, 3):
    if x == 0:
        continue
    multiplication *= x

print(multiplication)
