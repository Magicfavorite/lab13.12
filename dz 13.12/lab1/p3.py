"""Написать программу подсчета стоимости разговора
для разных мобильных операторов. Пользователь вводит
стоимость разговора и выбирает с какого на какой опе-
ратор он звонит. Вывести стоимость на экран.
1"""

operators = {
    'МТС': 1.5,
    'Билайн': 2,
    'Мегафон': 1.7,
    'Теле2': 1.2,
}

while True:
    try:
        cost = float(input("Введите стоимость разговора: "))
        from_operator = input("Введите оператора, с которого звоните: ")
        to_operator = input("Введите оператора, на который звоните: ")
        if from_operator not in operators or to_operator not in operators:
            raise ValueError
        cost += cost * operators[from_operator] * operators[to_operator]
        print(f"Стоимость разговора: {cost:.2f}")
        break
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите стоимость разговора и операторов.")
