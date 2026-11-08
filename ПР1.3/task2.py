# Задание 2. Дан файл(nums.txt), содержащий целые числа, через пробел. Удалите из него
# все четные числа;

with open("nums.txt", "r") as input_file:
    numbers = list(map(int, input_file.read().split()))

with open("nums.txt", "w") as output_file:
    for i in numbers:
        if i % 2 != 0:
            output_file.write(str(i) + " ")
