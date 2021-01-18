# -*- coding: utf-8 -*-


import simple_draw as sd
sd.resolution = (1200, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
brick_height = 50
for y in range(0, 600, 50):
    if y / 50 % 2 == 0:
        shift = 50
    else: shift = 0
    horisontal_start_point = sd.get_point(1, y)
    horisontal_end_point = sd.get_point(1200, y)
    sd.line(start_point=horisontal_start_point, end_point=horisontal_end_point, color=sd.COLOR_RED, width=3)
    for x in range(1, 1200, 100):
        vertical_start_point = sd.get_point(x + shift, y)
        vertical_end_point = sd.get_point(x + shift, y + brick_height)
        sd.line(start_point=vertical_start_point, end_point=vertical_end_point, color=sd.COLOR_RED, width=3)
        vertical_start_point_1 = sd.get_point(x + shift + 2, y + 2)
        vertical_end_point_1 = sd.get_point(x + shift + 2, y + brick_height - 1)
        sd.line(start_point=vertical_start_point_1, end_point=vertical_end_point_1, color=sd.COLOR_DARK_RED, width=2)





print("we don't need your education")
sd.pause()
