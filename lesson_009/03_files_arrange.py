# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#    os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#    time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
from pprint import pprint

class FileSorter:

    def __init__(self, target_folder):
        self.target_folder = target_folder
        self.sorted_file_path = {}

    def collect_file_path(self):
        """take all files from choosen type and add it path in dict as key. value is None
        next fuct will add time of creation as value."""
        file_path_list = []

        count = 0

        for dirpath, dirnames, filenames in os.walk(self.target_folder):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                file_path_list.append(file_path)
                count += 1
            for file in file_path_list:
                if file.endswith('png'):
                    self.sorted_file_path[file] = None


    def time_collect(self):
        for path, creation_time in self.sorted_file_path.items():
            time_unformated = os.path.getmtime(path)
            self.sorted_file_path[path] = time.gmtime(time_unformated)



    def format_date(self):
        for file_path, file_date in self.sorted_file_path.items():
            year = self.sorted_file_path[file_path][0]
            month = self.sorted_file_path[file_path][1]
            self.sorted_file_path[file_path] = str(year) + '-' + str(month)
        pprint(self.sorted_file_path)

    def create_dirs(self, target_dir):
        """пробегает по словарю и для каждого файла пытается создать директорию, если она не существовала.
        если директория уже есть - копирует тудаэтот файл"""
        for file_path, file_date in self.sorted_file_path.items():
            try:
                os.makedirs(target_dir + file_date, 0o777)
            except FileExistsError:
                shutil.copy2(file_path, target_dir + file_date)





sorter = FileSorter(target_folder='icons')
sorter.collect_file_path()
sorter.time_collect()
sorter.format_date()
sorter.create_dirs(target_dir='sorted_icons/')