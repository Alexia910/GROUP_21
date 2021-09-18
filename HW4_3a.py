while True:
    money = input("Количество денег:")
    if money == "":
        money = input("Вы ввели пустое поле. Введите число.")
    try:
        int(money)
    except ValueError:
        money = input("Вы ввели не число. Введите число.")
    money_byn = int(money)
    if money_byn <= 0:
        money_byn = int(input("Введите положительное число."))
    print("Ты ввёл", money_byn)
    print('Конвертированная сумма в USD =', money_byn / 2.5)
    print('Конвертированная сумма в EUR =', money_byn / 2.9)
    print('Конвертированная сумма в CHF =', money_byn / 2.7)
    print('Конвертированная сумма в GBP =', money_byn / 3.4)
    print('Конвертированная сумма в CNY =', money_byn / 0.38)
    break
