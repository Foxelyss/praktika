# Задание 2. Дан файл numsTask2.txt с словами расположенными в столбик. Из заданных
# слов составьте одну длинную строку (разделить каждое слово пробелом);

with open("numsTask2.txt", "r") as file:
    for i in file.read().split():
        print(i, end=" ")