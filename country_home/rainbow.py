# -*- coding: utf-8 -*-
# модуль рисующий радугу

import simple_draw as sd

sd.resolution = (1800, 800)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

step = 10
i = 0
step = 0
for i in range(7):
    center = sd.get_point(450, -100)
    color = rainbow_colors[i]
    sd.circle(center_position=center, radius=1000 + step, color=color, width=10)
    step += 10

# sd.pause()
