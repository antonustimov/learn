# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger


import my_burger
print('Lets make tasty burger!')
burger_consists = [
    my_burger.bun(),
    my_burger.patty(),
    my_burger.tomato(),
    my_burger.cucumber(),
    my_burger.cheese(),
    my_burger.sause()
    ]
print('Good appetite!!!')

print('our burger consists from: ', burger_consists)


print('Now it"s time fo DOUBLE CHEESEBURGER!!!')

cheeseburger_consists = [
    my_burger.bun(),
    my_burger.patty(),
    my_burger.cheese(),
    my_burger.patty(),
    my_burger.cheese(),
    my_burger.tomato(),
    my_burger.cucumber(),
    my_burger.cheese(),
    my_burger.sause()
    ]
print('EAT IT FASTER WHILE IT STILL HOT!!!')

print('our cheeseburger consists from: ', cheeseburger_consists)

