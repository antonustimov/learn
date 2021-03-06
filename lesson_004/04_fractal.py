# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
def draw_branches(start_point, angle, length):
    if length < 5:
        return
    angle_shift = sd.random_number(30 - 0.40 * 30, 30 + 0.40 * 30)
    length_shift = sd.random_number(75 - 0.2 * 75, 75 + 0.2 * 75) / 100
    v_1 = sd.get_vector(start_point=start_point, length=length, angle=angle + angle_shift, width=2)
    v_1.draw(sd.COLOR_GREEN)
    v_2 = sd.get_vector(start_point=start_point, length=length, angle=angle - angle_shift, width=2)
    v_2.draw(sd.COLOR_DARK_GREEN)
    draw_branches(start_point=v_1.end_point, length=length * length_shift, angle=angle + 30)
    draw_branches(start_point=v_2.end_point, length=length * length_shift, angle=angle - 30)
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисоватьr
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
root_point = sd.get_point(300, 30)
draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


