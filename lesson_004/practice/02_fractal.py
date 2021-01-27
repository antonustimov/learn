# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(600, 5)

angle_0 = 90
length_0 = 200
delta = 30


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
def branch(start_point, angle, length, delta):
    if length < 1:
        return
    v_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
    v_1.draw()
    start_point = v_1.end_point
    angle = angle - delta
    length = length * 0.75
    branch(start_point=start_point, angle=angle,length=length, delta=delta)



for i in range(0, 51, 10):
    branch(start_point=point_0, angle=angle_0, length=length_0, delta=i)
for i in range(0, -51, -10):
    branch(start_point=point_0, angle=angle_0, length=length_0, delta=i)

# angle_0 = 90
# length_0 = 200
# branch(start_point=point_0, angle=angle_0, lenght=length_0)


# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов




# сделать функцию branch рекурсивной

# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
#
#
# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)


sd.pause()

