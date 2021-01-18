# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(my_point, step, my_colour):
    my_radius = 50
    for _ in range(3):
        my_radius += step

        sd.circle(center_position=my_point, radius=my_radius, width=1, color=my_colour)



# for x in range(100, 1001, 100):
#     for y in range(200, 500, 100):
#         my_point = sd.get_point(x, y)
#         bubble(my_point, 4)


for x in range(100):
    my_point = sd.random_point()
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    my_colour = (r,g,b)
    bubble(my_point, random.randint(0, 7), my_colour)


sd.pause()


