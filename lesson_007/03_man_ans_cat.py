# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.
from random import randint
from termcolor import cprint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.

class Man():

    def __init__(self, name):
        self.satiety = 10
        self.name = name
        self.home = None

    def eat(self):
        if self.home.food > 50:
            cprint('{} вкусно покушал'.format(self.name), color='grey')
            self.home.food -= 50
            self.satiety += 50
        else:
            self.buy_food()

    def play_game(self):
        cprint('{} поиграл в игры'.format(self.name), color='cyan')
        self.satiety -= 20

    def go_work(self):
        cprint('{} сходил на работу'.format(self.name), color='magenta')
        self.home.money += 150
        self.satiety -= 10

    def buy_food(self):
        if self.home.money > 0:
            cprint('{} сходил в магазин'.format(self.name), color='blue')
            self.home.money -= 50
            self.home.food += 50
            self.satiety -= 10
        else:
            self.go_work()

    def buy_cat_food(self):
        if self.home.money > 0:
            cprint('{} купил еды коту'.format(self.name), color='blue')
            self.home.money -= 50
            self.home.cat_food += 50
            self.satiety -= 10
        else:
            self.go_work()

    def clean_home(self):
        cprint('{} убрался в доме'.format(self.name))
        self.satiety -= 10
        home.dirty -= 100


    def go_into_house(self):
        print('{} заселился в {}'.format(self.name, home.name))
        self.home = home
        self.satiety += 10

    def take_cat_from_street(self):
        self.cat = cat


    def act(self):
        dice = randint(1, 6)
        if vasya.satiety <= 10:
            cprint('{} помирет с голоду!!!'.format(self.name), color='red', on_color='on_grey')
            self.eat()
        elif home.cat_food <= 10:
            self.buy_cat_food()
        elif dice == 6:
            self.eat()
        elif dice == 5:
            self.clean_home()
        elif home.dirty > 100:
            self.clean_home()
        elif self.home.food < 50:
            self.buy_food()
        elif self.home.money < 10:
            self.go_work()
        elif dice == 1:
            self.go_work()
        else:
            self.play_game()


class Home():

    def __init__(self, name):
        self.name = name
        self.dirty = 10
        self.food = 50
        self.money = 50
        self.cat_food = 0

class Cat():
    def __init__(self, name):
        self.name = name
        self.satiety = 10
        self.home = home

    def eat(self):
        if home.cat_food > 0:
            cprint('{} покушал'.format(self.name), color='yellow')
            home.cat_food -= 50
            self.satiety += 50

    def play(self):
        cprint('{} дерет обои'.format(self.name))
        home.dirty += 50
        self.satiety -= 10

    def sleep(self):
        cprint('{} свернулся колечком и спит'.format(self.name))
        self.satiety -= 10

    def cat_act(self):
        global cat_dice
        cat_dice = randint(1,3)
        if cat_dice == 1:
            self.eat()
        elif self.satiety < 10:
            self.eat()
        elif cat_dice == 2:
            self.play()
        elif cat_dice == 3:
            self.sleep()

vasya = Man(name='Вася')
home = Home(name="HomeSweetHome")
cat = Cat(name='Барсик')

vasya.go_into_house()

for day in range(1, 366):
    vasya.act()
    cat.cat_act()
    home.dirty += 10
    cprint('===================День {}====================='.format(day), color='green')
    cprint('Еды : {}, Денег : {}, Сытость : {}, Сытость кота : {}, Кошачьей еды : {}, порядок : {}'.format(
        home.food, home.money, vasya.satiety, cat.satiety, home.cat_food, home.dirty), color='yellow')

    if day == 3:
        cprint('{} подобрал кота на улице'.format(vasya.name), color='red', on_color='on_grey')
        vasya.take_cat_from_street()


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
