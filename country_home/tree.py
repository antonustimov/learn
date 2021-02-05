# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1800, 800)

def draw_branches(start_point, angle, length):
    if length < 5:
        return
    angle_shift = sd.random_number(10 - 0.40 * 10, 10 + 0.40 * 10)
    length_shift = round(sd.random_number(75 - 0.2 * 50, 75 + 0.2 * 50)) / 100
    v_1 = sd.get_vector(start_point=start_point, length=length, angle=angle + angle_shift, width=2)
    v_1.draw(sd.COLOR_GREEN)
    v_2 = sd.get_vector(start_point=start_point, length=length, angle=angle - angle_shift, width=2)
    v_2.draw(sd.COLOR_DARK_GREEN)
    draw_branches(start_point=v_1.end_point, length=round(length * length_shift), angle=angle + 25)
    draw_branches(start_point=v_2.end_point, length=round(length * length_shift), angle=angle - 25)

root_point = sd.get_point(1200, 1)
draw_branches(start_point=root_point, angle=90, length=80)

# sd.pause()


