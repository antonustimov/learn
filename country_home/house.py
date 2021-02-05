import simple_draw as sd


sd.resolution = (1800, 800)

# wall of bricks
brick_height = 30
for y in range(0, 400, 30):
    if y / 30 % 2 == 0:
        shift = 30
    else: shift = 0
    horisontal_start_point = sd.get_point(300, y)
    horisontal_end_point = sd.get_point(900, y)
    sd.line(start_point=horisontal_start_point, end_point=horisontal_end_point, color=sd.COLOR_RED, width=3)
    for x in range(300, 900, 60):
        vertical_start_point = sd.get_point(x + shift, y)
        vertical_end_point = sd.get_point(x + shift, y + brick_height)
        sd.line(start_point=vertical_start_point, end_point=vertical_end_point, color=sd.COLOR_RED, width=3)
        vertical_start_point_1 = sd.get_point(x + shift + 2, y + 2)
        vertical_end_point_1 = sd.get_point(x + shift + 2, y + brick_height - 1)
        sd.line(start_point=vertical_start_point_1, end_point=vertical_end_point_1, color=sd.COLOR_DARK_RED, width=2)

# left side of house
sd.line(start_point=sd.get_point(300, 0), end_point=sd.get_point(300, 420), color=sd.COLOR_RED, width=3)
sd.line(start_point=sd.get_point(302, 2), end_point=sd.get_point(302, 419), color=sd.COLOR_DARK_RED, width=2)

# right side of house
sd.line(start_point=sd.get_point(900, 0), end_point=sd.get_point(900, 421), color=sd.COLOR_RED, width=3)
sd.line(start_point=sd.get_point(902, 0), end_point=sd.get_point(902, 421), color=sd.COLOR_DARK_RED, width=2)

# top of house
sd.line(start_point=sd.get_point(300, 420), end_point=sd.get_point(900, 420), color=sd.COLOR_RED, width=3)

# roof
sd.line(start_point=sd.get_point(300, 420), end_point=sd.get_point(600, 620), color=sd.COLOR_RED, width=3)
sd.line(start_point=sd.get_point(600, 620), end_point=sd.get_point(900, 420), color=sd.COLOR_RED, width=3)
# window
sd.square(left_bottom=sd.get_point(543, 152), side=116, color=sd.COLOR_RED, width=6)
sd.square(left_bottom=sd.get_point(543, 152), side=116, color=sd.COLOR_ORANGE, width=0)

# sd.pause()

