# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# step = 50
# for i in range(7):
#     start = sd.get_point(step, 50)
#     finish = sd.get_point(300 + step, 450)
#     color = rainbow_colors[i]
#     step += 5
#     sd.line(start_point=start, end_point=finish, color=color, width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
step = 10
for i in range(7):
    center = sd.get_point(600, -250)
    color = rainbow_colors[i]
    sd.circle(center_position=center, radius=700 + step, color=color, width=10)
    step += 10

sd.pause()
