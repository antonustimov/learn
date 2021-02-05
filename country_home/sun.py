# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1800, 800)
center_of_sun = sd.get_point(1700, 700)

sd.circle(center_position=center_of_sun, radius=70, color=sd.COLOR_YELLOW, width=0)

angle = 170
light_length = 0
while True:
    v_1 = sd.get_vector(start_point=center_of_sun, length=100, angle=angle, width=0)
    v_2 = sd.get_vector(start_point=center_of_sun, length=100 + light_length, angle=angle, width=0)
    sd.line(start_point=v_1.end_point, end_point=v_2.end_point, color=sd.COLOR_YELLOW, width=5)

    v_3 = sd.get_vector(start_point=center_of_sun, length=100, angle=angle + 30, width=0)
    v_4 = sd.get_vector(start_point=center_of_sun, length=100 + light_length, angle=angle + 30, width=0)
    sd.line(start_point=v_3.end_point, end_point=v_4.end_point, color=sd.COLOR_YELLOW, width=5)

    v_5 = sd.get_vector(start_point=center_of_sun, length=100, angle=angle + 60, width=0)
    v_6 = sd.get_vector(start_point=center_of_sun, length=100 + light_length, angle=angle + 60, width=0)
    sd.line(start_point=v_5.end_point, end_point=v_6.end_point, color=sd.COLOR_YELLOW, width=5)

    v_7 = sd.get_vector(start_point=center_of_sun, length=100, angle=angle + 90, width=0)
    v_8 = sd.get_vector(start_point=center_of_sun, length=100 + light_length, angle=angle + 90, width=0)
    sd.line(start_point=v_7.end_point, end_point=v_8.end_point, color=sd.COLOR_YELLOW, width=5)

    sd.sleep(0.1)
    light_length += 10

    if light_length > 100:
        sd.line(start_point=v_1.end_point, end_point=v_2.end_point, color=sd.background_color, width=8)
        sd.line(start_point=v_3.end_point, end_point=v_4.end_point, color=sd.background_color, width=8)
        sd.line(start_point=v_5.end_point, end_point=v_6.end_point, color=sd.background_color, width=8)
        sd.line(start_point=v_7.end_point, end_point=v_8.end_point, color=sd.background_color, width=8)

        light_length = 0
        angle += 20
        if angle > 190:
            angle = 170


    if sd.user_want_exit():
        break





sd.pause()
