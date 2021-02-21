# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_in_bedside = 100
        self.eat_in_refrigerator = 50
        self.dirt_in_house = 0

    def __str__(self):
        return 'Денег в доме :{}, Еды в холодильнике : {}, Уровень грязи : {}'.format(
            self.money_in_bedside, self.eat_in_refrigerator, self.dirt_in_house)

class Human:

    def __init__(self):
        self.satiety = 30
        self.happines = 100

    def __str__(self):
        return ' Сытость : {}, Уровень счастья : {}'.format(self.satiety, self.happines)



class Husband(Human):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def __str__(self):
        return '{} :'.format(self.name) + super().__str__()

    def act(self):
        self.satiety -= 10
        if self.satiety <= 20:
            self.eat()
        elif home.money_in_bedside <= 30:
            self.work()
        else: self.gaming()

    def eat(self):
        self.satiety += 10
        if home.eat_in_refrigerator >= 30:
            self.satiety += 30
            home.eat_in_refrigerator -= 30
            cprint('{} вкусно покушал!!!'.format(self.name), color='green')

        elif home.eat_in_refrigerator >0:
            self.satiety += home.eat_in_refrigerator
            home.eat_in_refrigerator = 0
            cprint('{} покушалб но мало!!!'.format(self.name), color='green')

        else: cprint('В холодильнике нет еды!!!', color='red')
        pass
    def work(self):
        home.money_in_bedside += 150
        cprint('{} сходил на работу!!!'.format(self.name), color='white')

    def gaming(self):
        self.happines += 20
        cprint('{} весь день играл в танки'.format(self.name), color='green')


class Wife(Human):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def __str__(self):
        return '{} :'.format(self.name) + super().__str__()

    def act(self):
        if  self.satiety <= 20:
            self.eat()
        elif home.eat_in_refrigerator <=30:
            self.shopping()
        elif home.dirt_in_house >= 0:
            self.clean_house()
        else: self.buy_fur_coat()

    def eat(self):
        if home.eat_in_refrigerator >= 30:
            self.satiety += 30
            home.eat_in_refrigerator -= 30
            cprint('{} вкусно покушала!!!'.format(self.name), color='green')

        elif home.eat_in_refrigerator >0:
            self.satiety += home.eat_in_refrigerator
            home.eat_in_refrigerator = 0
            cprint('{} покушала но мало!!!'.format(self.name), color='green')

        else: cprint('В холодильнике нет еды!!!', color='red')


    def shopping(self):
        self.satiety -= 10
        if home.money_in_bedside >= 50:
            home.money_in_bedside -= 50
            home.eat_in_refrigerator += 50
            cprint('{} купила еды'.format(self.name))
        elif home.money_in_bedside >= 0:
            home.eat_in_refrigerator += home.money_in_bedside
            home.money_in_bedside -= home.money_in_bedside
            cprint('{} купила немного еды'.format(self.name))
        else: cprint('В доме нет денег!!!', color='red')



    def buy_fur_coat(self):
        self.satiety -= 10
        if home.money_in_bedside >= 350:
            home.money_in_bedside -= 350
            self.happines += 60
            cprint('{} купила шубу'.format(self.name), color='green')
        else: cprint('Денег на шуб не хватает=(')

    def clean_house(self):
        self.satiety -= 10
        cprint('{} навела дома порядок'.format(self.name), color='white')
        if home.dirt_in_house >= 100:
            home.dirt_in_house -= 100
        elif home.dirt_in_house > 0:
            home.dirt_in_house -= home.dirt_in_house

class Child(Human):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def __str__(self):
        return '{} :'.format(self.name) + super().__str__()

    def act(self):
        if self.satiety <= 20:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        home.eat_in_refrigerator -= 10
        self.satiety += 10
    def sleep(self):
        self.satiety -= 10


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
for day in range(366):
    cprint('================== День {} =================='.format(day), color='grey')
    home.dirt_in_house += 5

    if serge.satiety <= 0:
        cprint('{} УМЕР С ГОЛОДУ!!!'.format(serge.name), color='red')
        break
    elif masha.satiety <= 0:
        cprint('{} УМЕРЛА С ГОЛОДУ!!!'.format(masha.name), color='red')
        break
    elif masha.satiety <= 0:
        cprint('{} УМЕР С ГОЛОДУ!!!'.format(masha.name), color='red')
        break

    serge.act()
    masha.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='magenta')
    cprint(kolya, color='magenta')
    cprint(home, color='yellow')

#
# ######################################################## Часть вторая
# #
# # После подтверждения учителем первой части надо
# # отщепить ветку develop и в ней начать добавлять котов в модель семьи
# #
# # Кот может:
# #   есть,
# #   спать,
# #   драть обои
# #
# # Люди могут:
# #   гладить кота (растет степень счастья на 5 пунктов)
# #
# # В доме добавляется:
# #   еда для кота (в начале - 30)
# #
# # У кота есть имя и степень сытости (в начале - 30)
# # Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# # Еда для кота покупается за деньги: за 10 денег 10 еды.
# # Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# # Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
# #
# # Если кот дерет обои, то грязи становится больше на 5 пунктов
#
#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#
#
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
#
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.
#
#
# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#
#
# # Усложненное задание (делать по желанию)
# #
# # Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# # Коты должны выжить вместе с семьей!
# #
# # Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# # Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
# #
# # Дополнительно вносить некий хаос в жизнь семьи
# # - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# # - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# # Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
# #   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
# #
# # в итоге должен получится приблизительно такой код экспериментов
# # for food_incidents in range(6):
# #   for money_incidents in range(6):
# #       life = Simulation(money_incidents, food_incidents)
# #       for salary in range(50, 401, 50):
# #           max_cats = life.experiment(salary)
# #           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#
