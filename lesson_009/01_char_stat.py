# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
import zipfile
from pprint import pprint


class TextAnalyzer:

    def __init__(self, file_name):
        self.file_name = file_name
        self.unsorted_result = {}
        self.sorted_result = []

    def unzip_file(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def analyze_text(self):
        if self.file_name.endswith('.zip'):
            self.unzip_file()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for letter in line:
                    if letter.isalpha():
                        if letter in self.unsorted_result:
                            self.unsorted_result[letter] += 1
                        else:
                            self.unsorted_result[letter] = 1

    def sort_results(self):
        for letter, count in self.unsorted_result.items():
            self.sorted_result.append([count, letter])
            self.sorted_result.sort(reverse=True)


        # pprint(self.sorted_result)


    def print_reult(self):
        """шапка таблицы"""
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt: ^14}|'.format(txt='Буква'), '{txt: ^14}|'.format(txt='частота'))
        print('+{txt:-^30}+'.format(txt='+'))
        """тело таблицы, подставлены значения из списка"""
        total_letters = 0
        for i in self.sorted_result:
            letter = i[1]
            count = i[0]
            total_letters += count
            print('|{txt: ^14}|'.format(txt=letter),
                  '{txt: ^14}|'.format(txt=count))
            print('+{txt:-^30}+'.format(txt='+'))
        """закрывающая часть таблицы и вывод общей суммы"""
        print('+{txt:-^30}+'.format(txt='+'))
        print('|{txt: ^14}|'.format(txt='Итого'), '{txt: ^14}|'.format(txt=total_letters))
        print('+{txt:-^30}+'.format(txt='+'))

analyze = TextAnalyzer(file_name ='/Users/ant__on/PycharmProjects/learn/lesson_009/python_snippets/voyna-i-mir.txt.zip')
analyze.analyze_text()
analyze.sort_results()
analyze.print_reult()