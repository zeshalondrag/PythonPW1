import math
def operations():
    print("Операции калькулятора:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - Возведение в степень")
    print("6 - Квадратный корень")
    print("7 - Факториал")
    print("8 - Синус")
    print("9 - Косинус")
    print("10 - Тангенс")
    print("0 - Выход из калькулятора")
def calculator():
    while True:
        operations()
        chop = input("Введите номер операции: ")
        if chop == '0':
            print("Выход из калькулятора.")
            break
        if chop in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                if chop == '1':
                    res = num1 + num2
                elif chop == '2':
                    res = num1 - num2
                elif chop == '3':
                    res = num1 * num2
                elif chop == '4':
                    if num2 == 0:
                        print("Ошибка: деление на 0.")
                        continue
                    res = num1 / num2
                elif chop == '5':
                    res = num1 ** num2
                else:
                    print("Ошибка: Неправильный выбор операции.")
                    continue
                print(f"Результат: {res}")
            except ValueError:
                print("Ошибка: Введите корректные числа.")
            except ZeroDivisionError:
                print("Ошибка: деление на 0.")
        elif chop in ('6', '7', '8', '9', '10'):
            try:
                num = float(input("Введите число: "))
                if chop == '6':
                    if num < 0:
                        print("Ошибка: квадратный корень отрицательного числа.")
                        continue
                    res = math.sqrt(num)
                elif chop == '7':
                    if num < 0:
                        print("Ошибка: факториал отрицательного числа.")
                        continue
                    res = math.factorial(int(num))
                elif chop == '8':
                    res = math.sin(num)
                elif chop == '9':
                    res = math.cos(num)
                elif chop == '10':
                    res = math.tan(num)
                else:
                    print("Ошибка: Неправильный выбор операции.")
                    continue
                print(f"Результат: {res}")
            except ValueError:
                print("Ошибка: Введите корректное число.")
        else:
            print("Ошибка: Неправильный выбор операции.")
calculator()