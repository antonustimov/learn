# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


class IamGodError(Exception):
    def __init__(self):
        self.message = 'Сегодня кто-то возомнил себя Богом!'

    def __str__(self):
        return self.message


class DrunkError(Exception):
    def __init__(self):
        self.message = 'Нажралось'

    def __str__(self):
        return self.message


class CarCrashError(Exception):
    def __init__(self):
        self.message = 'АВАРИЯ!!! А надо было следить за дорогой'

    def __str__(self):
        return self.message


class GlyttonyError(Exception):
    def __init__(self):
        self.message = 'С глютеном проблемы!'

    def __str__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self):
        self.message = 'Депрессия убивает=('

    def __str__(self):
        return self.message


class SuisideError(Exception):
    def __init__(self):
        self.message = 'Кошкама самоубился!'

    def __str__(self):
        return self.message


def one_day():
    karma = randint(1, 13)
    if karma < 8:
        return karma
    elif karma == 8:
        raise SuisideError
    elif karma == 9:
        raise IamGodError
    elif karma == 10:
        raise DepressionError
    elif karma == 11:
        raise DrunkError
    elif karma == 12:
        raise CarCrashError
    elif karma == 13:
        raise GlyttonyError


ENLIGHTENMENT_CARMA_LEVEL = 777
day_counter = 1
karma_needed = 0

with open('groundhod_day_log.txt', 'a', encoding='utf8') as file:
    while karma_needed < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            karma_needed += one_day()
        except Exception as exc:
            file.write(f'на {day_counter} день : {exc.__str__()}')
            file.write('\n')
        finally:
            day_counter += 1
    print(f'на {day_counter} день достигнуто просветление')
