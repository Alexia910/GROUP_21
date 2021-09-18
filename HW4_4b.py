def get_money():
    input_data = input("Введите сумму ")
    return input_data


def get_cur():
    print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
    cur = input()
    return cur


def check_data(input_data):
    if input_data == "":
        input_data = input("Вы ввели пустое поле. Введите число.")
    try:
        int(input_data)
    except ValueError:
        input_data = input("Вы ввели не число. Введите число.")
    money_byn = int(input_data)
    if money_byn <= 0:
        money_byn = int(input("Введите положительное число."))
    return money_byn


def usd_ex(input_data):
    rez = input_data / 2.5
    return rez


def eur_ex(input_data):
    rez = input_data / 2.9
    return rez


def chf_ex(input_data):
    rez = input_data / 2.7
    return rez


def gbp_ex(input_data):
    rez = input_data / 3.4
    return rez


def cny_ex(input_data):
    rez = input_data / 0.38
    return rez


def rez_message(cur, rez):
    print("конвертированная сумма в", cur, "=", rez)


def message(cur, money):
    print("Вы ввели сумму", money, "и валюту", cur)


def main():
    cur = get_cur()
    money = get_money()
    byn_money = check_data(money)
    message(cur, byn_money)
    if cur == "USD":
        rez = usd_ex(byn_money)
    if cur == "EUR":
        rez = eur_ex(byn_money)
    if cur == "CHF":
        rez = chf_ex(byn_money)
    if cur == "GBP":
        rez = gbp_ex(byn_money)
    if cur == "CNY":
        rez = cny_ex(byn_money)
    rez_message(cur,rez)

while True:
    main()


