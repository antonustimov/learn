# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water():
    def __init__(self):
        self.name = 'Water'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Wind':
            return Storm()
        elif other.name == 'Fire':
            return Steam()
        elif other.name == 'Earth':
            return Dirt()
        else:
            return None


class Wind():
    def __init__(self):
        self.name = 'Wind'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Water':
            return Storm()
        elif other.name == 'Fire':
            return Lightning()
        elif other.name == 'Earth':
            return Dust()
        else:
            return None


class Fire():
    def __init__(self):
        self.name = "Fire"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Water':
            return Steam()
        elif other.name == 'Wind':
            return Lightning()
        elif other.name == 'Earth':
            return Lava()
        else:
            return None


class Earth():
    def __init__(self):
        self.name = "Earth"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other.name == 'Water':
            return Dirt()
        elif other.name == 'Fire':
            return Lava()
        elif other.name == 'Wind':
            return Dust()
        else:
            return None


class Storm():
    def __init__(self):
        self.name = 'Storm'

    def __str__(self):
        return self.name


class Steam():
    def __init__(self):
        self.name = "Steam"

    def __str__(self):
        return self.name


class Dirt():
    def __init__(self):
        self.name = "Dirt"

    def __str__(self):
        return self.name


class Lightning():
    def __init__(self):
        self.name = "Lightning"

    def __str__(self):
        return self.name


class Lava():
    def __init__(self):
        self.name = "Lava"

    def __str__(self):
        return self.name


class Dust():
    def __init__(self):
        self.name = "Dust"

    def __str__(self):
        return self.name


print(Water() + Wind())
print(Water() + Fire())
print(Water() + Earth())
print(Wind() + Water())
print(Wind() + Fire())
print(Wind() + Earth())
print(Fire() + Water())
print(Fire() + Wind())
print(Fire() + Earth())
print(Earth() + Water())
print(Earth() + Wind())
print(Earth() + Fire())
print(Wind() + Wind())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
