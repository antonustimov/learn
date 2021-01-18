# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

'''FUNCTION FOR DRAW CIRCLE'''
# def bubble(my_point, step, my_colour):
#     my_radius = 50
#     for _ in range(3):
#         my_radius += step
#
#         sd.circle(center_position=my_point, radius=my_radius, width=1, color=my_colour)
#
#
#
# # for x in range(100, 1001, 100):
# #     for y in range(200, 500, 100):
# #         my_point = sd.get_point(x, y)
# #         bubble(my_point, 4)
#
#
# for x in range(100):
#     my_point = sd.random_point()
#     r = random.randint(1, 255)
#     g = random.randint(1, 255)
#     b = random.randint(1, 255)
#     my_colour = (r,g,b)
#     bubble(my_point, random.randint(0, 7), my_colour)
"""CLOCK"""
import math


angle_min = random.randint(0, 360)
angle_hour = random.randint(0, 360)

radius = random.randint(100, 200)
COLOR_RED = (255, 0, 0)
x_mid, y_mid = 500, 300
mid = sd.get_point(x_mid, y_mid)

x_min = x_mid + radius * math.cos(angle_min)
y_min = y_mid + radius * math.sin(angle_min)
min = sd.get_point(x_min, y_min)

x_hour = x_mid + (radius - 50) * math.cos(angle_hour)
y_hour = y_mid + (radius - 50) * math.sin(angle_hour)
hour = sd.get_point(x_hour, y_hour)



sd.circle(center_position=mid, radius=radius, width=0)
sd.line(start_point=mid, end_point=min, color=COLOR_RED, width=5)
sd.line(start_point=mid, end_point=hour, color=COLOR_RED, width=5)




sd.pause()


