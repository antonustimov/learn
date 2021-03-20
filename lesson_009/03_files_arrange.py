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

    def __init__(self, file_name):
        self.file_name = file_name
        self.sorted_file_path = {}

    def collect_file_path(self):
        """take all files from choosen type and add it path in dict as key. value is None
        next fuct will add time of creation as value."""
        file_path_list = []

        count = 0

        for dirpath, dirnames, filenames in os.walk(self.file_name):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                file_path_list.append(file_path)
                count += 1
            for file in file_path_list:
                if file.endswith('png'):
                    self.sorted_file_path[file] = None

        # pprint(file_path_list)
        print(count)

    def time_collect(self):
        for path, creation_time in self.sorted_file_path.items():
            time_unformated = os.path.getmtime(path)
            self.sorted_file_path[path] = time.gmtime(time_unformated)
        pprint(self.sorted_file_path)


sorter = FileSorter('icons')
sorter.collect_file_path()
sorter.time_collect()