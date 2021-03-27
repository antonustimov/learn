# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
import simple_draw as sd
from random import randint

sd.resolution = (1200, 600)

y = 600
def snowflakes(N, color = sd.COLOR_WHITE, y_shift = 0):
    x = 100
    for _ in range(N):
        sd.snowflake(center=sd.get_point(x, y + y_shift), color=color, length=50)
        x += 150


def falling():
    x = 50
    while True:
        snowflakes(N=8, y_shift=x)
        sd.sleep(0.1)
        snowflakes(N=8, y_shift=x, color=sd.background_color)

        x -= 50
        if sd.user_want_exit():
            break

falling()
sd.pause()