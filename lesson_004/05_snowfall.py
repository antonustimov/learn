# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20
snow_start = []
snow_length = []
y = 800 + sd.random_number(0, 200)
for i in range(N):
    x = sd.random_number(0, 1200)
    snow_start.append(x)
    lenght = sd.random_number(10, 100)
    snow_length.append(lenght)

ran = sd.random_number(0, 19)

while True:
    sd.clear_screen()
    point = sd.get_point(snow_start[ran], y)
    sd.snowflake(center=point, length=snow_length[ran])
    sd.sleep(0.1)
    sd.snowflake(center=point, length=snow_length[ran], color=sd.background_color)
    y -= 10
    if y < 50:
        sd.snowflake(center=point, length=snow_length[ran])
        break


    if sd.user_want_exit():
        break

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()
# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
while True:
    # sd.clear_screen()
    pass
    pass
    pass
    # sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


