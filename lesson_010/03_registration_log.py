# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.



def check_line(line, line_count):
    name, email, age = line.split(' ')
    pass

def good_data():
    with open('registrations_good.log', 'a', encoding='utf8'):
        pass

def bad_data(exc_args, line_count):
    with open('registrations_bad.log', 'a', encoding='utf8'):
        pass

with open('registrations.txt', 'r', encoding='utf8') as init_file:
    line_count = 1
    for line in init_file:
        line = line[:-1]
        line_count += 1
        try:
            check_line(line, line_count)
        except Exception as exc:
            bad_data(exc.args, line_count)
