# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.



# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
from pprint import pprint


class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.result = {}

        pass

    def read_file(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                minute = line[1:17]
                if minute in self.result:
                    continue
                else:
                    self.result[minute] = 0


        # pprint(self.result)

    def analyze(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                minute = line[1:17]
                if line.endswith('NOK\n'):
                    self.result[minute] += 1

        pprint(self.result)

    def sort_result(self):
        pass

    def print_result(self):
        pass

lod_parser = LogParser('events.txt')
lod_parser.read_file()
lod_parser.analyze()