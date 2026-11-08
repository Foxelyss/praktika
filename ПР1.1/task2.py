# Задание 2. Добавляйте новые числа в список до тех пор, пока пользователь не введет 0.
# Выведите в консоль сумму и произведение всех элементов списка. Выведите среднее,
# среди всех элементов списка. Добавьте обработку исключений, чтобы приложение аварийно
# не завершалось;

def get_int_value_from_user():
    try:
        return int(input())
    except:
        print("Введите число")
        return get_int_value_from_user()


number = get_int_value_from_user()

summary = 0
multiplication = 1

quantity = 0

while number != 0:
    summary += number
    multiplication *= number

    quantity += 1

    number = get_int_value_from_user()

avarage_number = summary / quantity

print("Сумма чисел", summary)
print("Умножение чисел", multiplication)
print("Среднее чисел", avarage_number)
