"""Написать программу, которая по выбору пользова-
теля возводит введенное им число в степень от нулевой
до седьмой включительно."""

while True:
    try:
        number = int(input("Введите число: "))
        sila = int(input("Введите степень: "))
        if sila < 0 or sila > 7:

        result = number**sila
        print(result)
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите число и степень.")
