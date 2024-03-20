"""Пользователь вводит два числа. Определить, равны
ли эти числа, и, если нет, вывести их на экран в порядке
возрастания.
"""

while True:
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
        if number1 == number2:
            print("Введенные числа равны.")
            break
        elif number1 < number2:
            print(f"Введенные числа в порядке возрастания: {number1} {number2}")
            break
        else:
            print(f"Введенные числа в порядке возрастания: {number2} {number1}")
            break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите числа.")
