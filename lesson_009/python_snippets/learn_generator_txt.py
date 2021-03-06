# -*- coding: utf-8 -*-
from pprint import pprint
from random import randint
import zipfile

class AutoWriter():



    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.analyze = 5

    def unzip_file(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for file_name in zfile.namelist():
            zfile.extract(file_name)
        self.file_name = file_name


    def get_statistic(self):

        self.stat = {}
        up_level_char = ' ' * self.analyze
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for low_level_char in line:
                    if up_level_char in self.stat:
                        if low_level_char in self.stat[up_level_char]:
                            self.stat[up_level_char][low_level_char] += 1
                        else:
                            self.stat[up_level_char][low_level_char] = 1
                    else:
                        self.stat[up_level_char] = {low_level_char: 1}
                    up_level_char = low_level_char
        # pprint(self.stat)


    def prepare_for_generate(self):
        self.totals = {}
        self.stat_for_generate = {}
        for up_level_char, char_stat in self.stat.items():
            self.totals[up_level_char] = 0
            self.stat_for_generate[up_level_char] = []
            for low_level_char, count in char_stat.items():
                self.totals[up_level_char] += count
                self.stat_for_generate[up_level_char].append([count, low_level_char])
            self.stat_for_generate[up_level_char].sort(reverse=True)

# pprint(totals)
# pprint(stat_for_generate)
    def generate_text(self):
        N = 1000
        printed = 0
        up_level_char = ' ' * self.analyze
        space_counter = 0
        chars_printed = 0
        while printed < N:
            char_stat = self.stat_for_generate[up_level_char]
            total = self.totals[up_level_char]
            dice = randint(1, total)
            pos = 0
            for count, char in char_stat:
                pos += count
                if dice <= pos:
                    break
                chars_printed += 1
            if chars_printed >= 300:
                print(char)
                chars_printed = 0
            else:

                print(char, end='')

            if char == ' ':
                space_counter += 1
                if space_counter >= 10:
                    space_counter = 0
            up_level_char = char
            printed += 1

writer = AutoWriter(file_name = 'voyna-i-mir.txt')
writer.get_statistic()
writer.prepare_for_generate()
writer.generate_text()