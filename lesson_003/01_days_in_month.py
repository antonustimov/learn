# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
month_names = {1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august',
               9 : 'september', 10 : 'october', 11 : 'november', 12 : "december"}
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

while month > 12:
    print('You type wrong number, please try again')
    user_input = input("Введите, пожалуйста, номер месяца: ")
    month = int(user_input)

    print('Вы ввели', month)
if 7 >= month and month % 2 != 0:
    print('in ',month_names[month], ' 31 days')
elif 7 < month and month % 2 == 0:
    print('in ',month_names[month], ' 31 days')
elif month == 2:
    print('in ',month_names[month], ' 28 days')
else:
    print('in ',month_names[month], ' 30 days')
