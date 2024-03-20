"""Пользователь вводит с клавиатуры номер дня недели
(1-7). Необходимо вывести на экран названия дня неде-
ли. Например, если 1, то на экране надпись понедельник,"""

while True:
    try:
        number = int(input("Введите число от 1 до 100: "))
        if number < 1 or number > 100:
            raise ValueError
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите число от 1 до 100.")

