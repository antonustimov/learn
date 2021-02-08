# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

from random import randint

_number = set()
_number_list = []



def put_number():
    while len(_number) < 4:
        _number.add(randint(0, 9))
    for i in _number:
        _number_list.append(i)
    if _number_list[0] == 0:
        _number_list.append(_number_list.pop(0))


put_number()
def check_number(user_input):
    user_input_list = []
    sys_answer = dict()
    cows = 0
    bulls = 0
    for i in user_input:
        user_input_list.append(int(i))

    for i in range(len(_number_list)):
        if user_input_list[i] in _number_list:
            cows += 1
        if user_input_list[i] == _number_list[i]:
            bulls += 1
    sys_answer = {'bulls': bulls, 'cows': cows - bulls}
    return sys_answer





print(_number_list)
print(check_number(user_input='1234'))
print(check_number(user_input='2345'))
print(check_number(user_input='3456'))
print(check_number(user_input='4567'))