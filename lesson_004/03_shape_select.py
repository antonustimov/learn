# -*- coding: utf-8 -*-


import simple_draw as sd
sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
point_0 = sd.get_point(600, 100)
side_length = 200


number_of_angles = int(input("Type number of angles from 3 to 20 pls: "))
while number_of_angles < 3:
    print("You enter wrong data! Please try again")
    number_of_angles = int(input("Type number of angles from 3 to 20 pls: "))



def shape(number_of_angles, start_point_0, angle_0, length):
    side_angle = 360 / number_of_angles
    next_angle = angle_0
    start_point = start_point_0
    print(angle_0)
    if next_angle > 360 - side_angle:
        v_end = sd.line(start_point=start_point, end_point=point_0, width=3)
        return
    v_1 = sd.get_vector(start_point=start_point, angle=next_angle, length=length, width=3)
    v_1.draw()
    next_angle += side_angle
    shape(number_of_angles=number_of_angles, start_point_0=v_1.end_point, angle_0=next_angle, length=side_length)


print(shape(number_of_angles=number_of_angles, start_point_0=point_0, angle_0=20, length=side_length))
# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg



sd.pause()
