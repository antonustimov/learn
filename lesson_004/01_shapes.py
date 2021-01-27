# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
point_0 = sd.get_point(600, 100)
length = 200

def triangle(start_point, angle, length):
    v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v_1.draw()
    v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 120, length=length, width=3)
    v_2.draw()
    v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 240, length=length, width=3)
    v_3.draw()


triangle(start_point=point_0, angle=30, length=length)
# - квадрата

def square(start_point, angle, length):
    v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v_1.draw()
    v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 90, length=length, width=3)
    v_2.draw()
    v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 180, length=length, width=3)
    v_3.draw()
    v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 270, length=length, width=3)
    v_4.draw()


square(start_point=point_0, angle=30, length=length)
# - пятиугольника
def pentacle(start_point, angle, length):
    v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v_1.draw()
    v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 72, length=length, width=3)
    v_2.draw()
    v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 144, length=length, width=3)
    v_3.draw()
    v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 144 + 72, length=length, width=3)
    v_4.draw()
    v_5 = sd.get_vector(start_point=v_4.end_point, angle=angle + 288, length=length, width=3)
    v_5.draw()

pentacle(start_point=point_0, angle=30, length=length)
# - шестиугольника
def sixangle(start_point, angle, length):
    v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v_1.draw()
    v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 60, length=length, width=3)
    v_2.draw()
    v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle + 120, length=length, width=3)
    v_3.draw()
    v_4 = sd.get_vector(start_point=v_3.end_point, angle=angle + 180, length=length, width=3)
    v_4.draw()
    v_5 = sd.get_vector(start_point=v_4.end_point, angle=angle + 240, length=length, width=3)
    v_5.draw()
    v_6 = sd.get_vector(start_point=v_5.end_point, angle=angle + 300, length=length, width=3)
    v_6.draw()

sixangle(start_point=point_0, angle=30, length=length)
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
