

import simple_draw as sd
sd.resolution = (1800, 800)

coordinates = sd.get_point(600, 210)
def smile(coordinates, color):
    sd.circle(center_position=coordinates, radius=50, color=color, width=0)
    left_eye = sd.get_point(x - 20, y + 12)
    sd.circle(center_position=left_eye, radius=9, color=sd.COLOR_BLACK, width=0)
    right_eye = sd.get_point(x + 20, y + 12)
    sd.circle(center_position=right_eye, radius=9, color=sd.COLOR_BLACK, width=0)
    mouth_points  = (sd.get_point(x - 25,y - 12), sd.get_point(x - 15, y - 18), sd.get_point(x - 11, y - 20),
                     sd.get_point(x + 11, y - 20),sd.get_point(x + 15, y - 18), sd.get_point(x + 25, y - 12))
    sd.lines(point_list=mouth_points,color=sd.COLOR_BLACK, width=3)


x = 600
y = 210
coordinates = sd.get_point(x, y)
smile(coordinates=coordinates, color=sd.COLOR_YELLOW)


# sd.pause()