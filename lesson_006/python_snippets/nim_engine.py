from random import randint

_stack_list = []
NUMBER_OF_STACKS = 5

def put_stones():
    for _ in range(NUMBER_OF_STACKS):
        _stack_list.append(randint(1, 20))
    return _stack_list

def take_stone(stack_number, number_of_stones):
    if 0 <= stack_number < len(_stack_list):
        _stack_list[stack_number] -= number_of_stones



def stones_position():
    return _stack_list

def is_gameover():
    if sum(_stack_list) == 0:
        return True
