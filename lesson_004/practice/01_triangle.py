# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

point = sd.get_point(300, 300)
# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length = 200


# v_1 = sd.get_vector(start_point=point, angle=120, length=200, width=3)
# v_1.draw()
# v_2 = sd.get_vector(start_point=v_1.end_point, angle=240, length=200, width=3)
# v_2.draw()
# v_3 = sd.get_vector(start_point=v_2.end_point, angle=0, length=200, width=3)
# v_3.draw()


# определить функцию рисования треугольника из заданной точки с заданным наклоном
def triangle(start_point, angle):
    v_1 = sd.get_vector(start_point=start_point, angle=angle + 120, length=200, width=3)
    v_1.draw()
    v_2 = sd.get_vector(start_point=v_1.end_point, angle=angle + 240, length=200, width=3)
    v_2.draw()
    v_3 = sd.get_vector(start_point=v_2.end_point, angle=angle, length=200, width=3)
    v_3.draw()


for i in range(0, 361, 30):
    angle = i
    triangle(start_point=point, angle=angle)

sd.pause()

