#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["mom", "son", "father"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [["mom", 168], ["son", 150], ['father', 170]]

member = my_family[2]
height = str(my_family_height[2][1])
total_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]

print("my " + member + " height is " + height + " sm")

print("my family total height is " + str(total_height))


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
