while True:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    znak = input("Введіть знак (+, -, *, /): ")

    if znak == "+":
        print("Результат:", num1 + num2)

    elif znak == "-":
        print("Результат:", num1 - num2)

    elif znak == "*":
        print("Результат:", num1 * num2)

    elif znak == "/":
        if num2 != 0:
            print("Результат:", num1 / num2)
        else:
            print("На нуль ділити не можна")

    else:
        print("Невірний знак")

    answer = input("Продовжити? (y/n): ")

    if answer != "y":
        print("Калькулятор завершив роботу")
        break
