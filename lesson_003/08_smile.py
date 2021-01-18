# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd
sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(coordinates, color):
    sd.circle(center_position=coordinates, radius=100, color=color, width=0)
    left_eye = sd.get_point(x - 40, y + 25)
    sd.circle(center_position=left_eye, radius=18, color=sd.COLOR_BLACK, width=6)
    right_eye = sd.get_point(x + 40, y + 25)
    sd.circle(center_position=right_eye, radius=18, color=sd.COLOR_BLACK, width=6)
    mouth_points  = (sd.get_point(x - 40,y - 25), sd.get_point(x - 25, y - 35), sd.get_point(x - 11, y - 40),
                     sd.get_point(x + 11, y - 40),sd.get_point(x + 25, y - 35), sd.get_point(x + 40, y - 25))
    sd.lines(point_list=mouth_points,color=sd.COLOR_BLACK, width=4)

for _ in range(10):
    x = random.randint(50, 1150)
    y = random.randint(50, 650)
    coordinates = sd.get_point(x, y)
    color = sd.COLOR_YELLOW
    smile(coordinates, color)




sd.pause()
