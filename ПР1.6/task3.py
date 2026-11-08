# Задание 3. Дано число. Определите будет ли это число четным и кратным 10;

number = int(input())

if number % 10 == 0 and number % 2 == 0:
    print(f"Число {number} четное и кратно 10")
else:
    print(f"Число {number} не подходит условию")