#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

zoo.append(birds[0])
zoo.append(birds[1])
zoo.append(birds[2])

print(zoo)

# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')

print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
a = input()
if a in zoo :
    position = str(zoo.index(a) + 1)
    print(a + " sit in cage number " + position)

else : print("this animal is not in zoo")


