# -*- coding: utf-8 -*-

import simple_draw as sd
from random import randint
sd.resolution = (1800, 800)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake():

    def __init__(self):
        self.x = randint(50, 1750)
        self.y = 800
        self.length = randint(30, 100)
        self.factor_a = randint(30, 60) / 100
        self.factor_b = randint(20, 50) / 100
        self.factor_c = randint(30, 60)

    def draw(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length,
                     factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c )

    def move(self):
        self.y -= randint(10, 30)

    def clear_previous_picture(self):
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=sd.background_color,
                     factor_a=self.factor_a, factor_b=self.factor_b, factor_c=self.factor_c)

    def cant_fall(self):
        if self.y <= self.length / 2:
            return True

    def fall(self):
        while True:
            self.clear_previous_picture()
            self.move()
            self.draw()
            if self.cant_fall():
                break
            sd.sleep(0.1)
            if sd.user_want_exit():
                break


flake = Snowflake()

flake.fall()


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if flake.cant_fall():
#         flake = Snowflake()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
