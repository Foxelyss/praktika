# Задание 5. В строке, которую вводит пользователь, определите количество слов,
# добавьте в начало строки слово Start и в конец строки слово End;

string = input()

words_count = len(string.split())

string = "Start " + string + " End"

print("Количество слов:", words_count)
print("Итоговая строка:", string)
