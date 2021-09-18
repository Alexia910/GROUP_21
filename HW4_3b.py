def get_money():
    input_data = input("Количество денег ")
    return input_data


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


def rez_message(money_byn):
    print("Ты ввёл", money_byn)
    print('Конвертированная сумма в USD =', money_byn / 2.5)
    print('Конвертированная сумма в EUR =', money_byn / 2.9)
    print('Конвертированная сумма в CHF =', money_byn / 2.7)
    print('Конвертированная сумма в GBP =', money_byn / 3.4)
    print('Конвертированная сумма в CNY =', money_byn / 0.38)


def main():
    money = get_money()
    byn_money = check_data(money)
    rez_message(byn_money)


while True:
    main()
    break
