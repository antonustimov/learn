# -*- coding: utf-8 -*-


# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.


from nim_engine import put_stones, take_stone, stones_position, is_gameover
from termcolor import cprint

cprint('ДА НАЧНЕТСЯ ИГРА!!!', color='red')
put_stones()
counter = 1
while True:
    cprint('Текущая позиция:', color='yellow', on_color='on_grey')
    cprint(stones_position(), color='red')
    color = 'blue' if counter == 1 else 'green'
    cprint('Ходит игрок номер ' + str(counter), color=color)
    cprint('Из какой кучки берем?', color=color)
    stack_number = int(input()) - 1
    cprint('Сколько берем?', color=color)
    number_of_stones = int(input())
    take_stone(stack_number=stack_number, number_of_stones=number_of_stones)

    if is_gameover():
        break
    counter = 2 if counter == 1 else 1

cprint('Победил игрок номер ' + str(counter) + '!!!', color=color, on_color='on_grey')

