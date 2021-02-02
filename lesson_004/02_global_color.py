# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 600)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()

# Результат решения см lesson_004/results/exercise_02_global_color.jpg



colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


point_0 = sd.get_point(600, 100)
length = 200
inputed_number = int(input('Choose you color and type it number:''\n''1 : red''\n''2 : orange''\n''3 : yellow''\n'
                          '4 : green''\n''5 : cyan''\n''6 : blue''\n''7 : purple''\n'))

while inputed_number < 1 and inputed_number > 7:
    print('PLEASE ENTER CORRCT NUMBER')
    inputed_number = int(input('Choose you color and type it number:''\n''1 : red''\n''2 : orange''\n''3 : yellow''\n'
                              '4 : green''\n''5 : cyan''\n''6 : blue''\n''7 : purple''\n'))
choosen_color = colors[inputed_number - 1]
def draw_lines(start_point, length, angle_shift, color):
    point_0 = start_point
    for x in range(0, (360 - angle_shift), angle_shift):

        v_1 = sd.get_vector(start_point=start_point, angle=x, length=length,)
        sd.line(start_point=v_1.start_point, end_point=v_1.end_point, color=color, width=3)
        start_point = v_1.end_point
        if x > 359 - angle_shift * 2:
            sd.line(start_point=v_1.end_point, end_point=point_0, color=color, width=3)
    return




# треугольник
def triangle(start_point, angle_number, length, color):
    angle_shift = round(360 / angle_number)
    draw_lines(start_point=start_point, length=length, angle_shift=angle_shift, color=choosen_color)

triangle(start_point=point_0, length=length, color=choosen_color, angle_number = 3)

# - квадрат
def quad(start_point, angle_number, length, color):
    angle_shift = round(360 / angle_number)
    draw_lines(start_point=start_point, length=length, angle_shift=angle_shift, color=choosen_color)

quad(start_point=point_0, length=length, color=choosen_color, angle_number = 4)

# пятиугольник
def pent(start_point, angle_number, length, color):
    angle_shift = round(360 / angle_number)
    draw_lines(start_point=start_point, length=length, angle_shift=angle_shift, color=choosen_color)

pent(start_point=point_0, length=length, color=choosen_color, angle_number = 5)

# # - шестиугольника
def sixangle(start_point, angle_number, length, color):
    angle_shift = round(360 / angle_number)
    draw_lines(start_point=start_point, length=length, angle_shift=angle_shift, color=choosen_color)

sixangle(start_point=point_0, length=length, color=choosen_color, angle_number = 6)


sd.pause()
