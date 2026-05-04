number = input("Введіть 4-значне число: ")

if len(number) == 4 and number.isdigit():

    print(number[0])
    print(number[1])
    print(number[2])
    print(number[3])
else:
    print("Помилка: потрібно ввести рівно 4 цифри.")
