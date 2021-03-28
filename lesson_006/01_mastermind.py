# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from mastremind_engine import put_number, check_number
from termcolor import cprint
cprint('ДА НАЧНЕТСЯ ИГРА!!!', color='red', on_color='on_grey')

cprint('Компьтер загадал четырехзначное число, где все цифры разные,'
       '\nкомпьютер сообщает о количестве «быков» и «коров» в загаданном числе,'
       '\n«бык» — цифра есть в записи задуманного числа и стоит в той же позиции'
       '\nчто и в задуманном числе'
       '\n«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,'
       '\nчто и в задуманном числе', color='yellow')
put_number()
while True:
    cprint('Введи четырехзнычное число', color='cyan')
    user_input = input()
    answer = check_number(user_input=user_input)
    cprint('Быков - ' + str(answer['bulls']), color='green')
    cprint('Коров - ' + str(answer['cows']), color='blue')
    if answer['bulls'] == 4:
        cprint('ТЫ УГАДАЛ!!! ЭТО БЫЛО ЧИСЛО ' + str(user_input), color='red', on_color='on_grey')
        break

