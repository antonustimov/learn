# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snow():
    x = sd.random_number(0, 1100)
    y = 600


    length = sd.random_number(20, 70)
    f_a = sd.random_number(2, 8) / 10
    f_b = sd.random_number(20, 70) / 100
    f_c = sd.random_number(30, 75)


    while True:
        # sd.clear_screen()

        sd.snowflake(center=sd.get_point(x, y), length=length, factor_a=f_a, factor_b=f_b, factor_c=f_c)
        pass
        pass
        sd.sleep(0.1)
        sd.snowflake(center=sd.get_point(x, y), length=length, color=sd.background_color,
                     factor_a=f_a, factor_b=f_b, factor_c=f_c)
        y -= 50

        if y < length:
            sd.snowflake(center=sd.get_point(x, y), length=length, factor_a=f_a, factor_b=f_b, factor_c=f_c)
            y = 600
            x = sd.random_number(0, 1100)
            snow()
        if sd.user_want_exit():
            break

snow()



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


