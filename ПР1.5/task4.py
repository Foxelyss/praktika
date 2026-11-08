# Задание 4. Дан файл numsTask4.txt с целыми числами. Вычислите сумму элементов,
# отличающихся от максимального на 1;

with open("numsTask4.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

max_number = max(numbers)

print(numbers.count(max_number - 1))
