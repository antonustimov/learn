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
# colors = ['COLOR_RED', 'COLOR_ORANGE', 'COLOR_YELLOW', 'COLOR_GREEN', 'COLOR_CYAN', 'COLOR_BLUE', 'COLOR_PURPLE']
point_0 = sd.get_point(600, 100)
length = 100
choosen_color = sd.COLOR_GREEN








def draw_lines(start_point, length, angle_shift, color):
    point_0 = start_point
    for x in range(0, (360 - angle_shift), angle_shift):

        v_1 = sd.get_vector(start_point=start_point, angle=x, length=length,)
        sd.line(start_point=v_1.start_point, end_point=v_1.end_point, color=color, width=1)
        start_point = v_1.end_point
        print(x)
        if x > 359 - angle_shift * 2:
            sd.line(start_point=v_1.end_point, end_point=point_0, color=color, width=1)
    return





def triangle(start_point, angle_number, length, color):
    angle_shift = round(360 / angle_number)
    draw_lines(start_point=start_point, length=length, angle_shift=angle_shift, color=choosen_color)




triangle(start_point=point_0, length=length, color=choosen_color, angle_number = 10)


# - квадрата

# def square(start_point, angle, length):
#     v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v_1.draw()
#     v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 90, length=length, width=3)
#     v_2.draw()
#     v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 180, length=length, width=3)
#     v_3.draw()
#     v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 270, length=length, width=3)
#     v_4.draw()
#
#
# square(start_point=point_0, angle=30, length=length)
# # - пятиугольника
# def pentacle(start_point, angle, length):
#     v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v_1.draw()
#     v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 72, length=length, width=3)
#     v_2.draw()
#     v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 144, length=length, width=3)
#     v_3.draw()
#     v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 144 + 72, length=length, width=3)
#     v_4.draw()
#     v_5 = sd.get_vector(start_point=v_4.end_point, angle=angle + 288, length=length, width=3)
#     v_5.draw()
#
# pentacle(start_point=point_0, angle=30, length=length)
# # - шестиугольника
# def sixangle(start_point, angle, length):
#     v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
#     v_1.draw()
#     v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 60, length=length, width=3)
#     v_2.draw()
#     v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 120, length=length, width=3)
#     v_3.draw()
#     v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 180, length=length, width=3)
#     v_4.draw()
#     v_5 = sd.get_vector(start_point=v_4.end_point, angle=angle + 240, length=length, width=3)
#     v_5.draw()
#     v_6 = sd.get_vector(start_point=v_5.end_point, angle=angle + 300, length=length, width=3)
#     v_6.draw()
#
# sixangle(start_point=point_0, angle=30, length=length)


sd.pause()
