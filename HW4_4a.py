while True:
    print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
    cur = input()
    money = input("Введите сумму ")
    if money == "":
        money = input("Вы ввели пустое поле. Введите число.")
    try:
        int(money)
    except ValueError:
        money = input("Вы ввели не число. Введите число.")
    money_byn = int(money)
    if money_byn <= 0:
        money_byn = int(input("Введите положительное число."))
    print("Вы ввели сумму", money, "и валюту", cur)
    if cur == "USD":
        rez = money_byn / 2.5
    if cur == "EUR":
        rez = money_byn / 2.9
    if cur == "CHF":
        rez = money_byn / 2.7
    if cur == "GBP":
        rez = money_byn / 3.4
    if cur == "CNY":
        rez = money_byn / 0.38
    print("конвертированная сумма в", cur, "=", rez)