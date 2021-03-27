# -*- coding: utf-8 -*-

# Есть файл calc.txt с записями операций - текстовый калькулятор. Записи вида
#
# 100 + 34
# 23 / 4
#
# то есть ОПЕРАНД_1 ОПЕРАЦИЯ ОПЕРАНД_2, разделенные пробелами.
# Операндны - целые числа. Операции - арифметические, целочисленное деление и остаток от деления.
#
# Нужно вычислить все операции и найти сумму их результата.
from pprint import pprint


def calc(line):
    operand_1, operation, operand_2 = line.split(' ')

    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        return operand_1 + operand_2
    elif operation == '-':
        return operand_1 - operand_2
    elif operation == '*':
        return operand_1 * operand_2
    elif operation == '/':
        return operand_1 / operand_2
    elif operation == '//':
        return operand_1 // operand_2
    elif operation == '%':
        return operand_1 % operand_2
    else:
        print('wrong input data')


total_summ = 0
with open('calc.txt', 'r') as file:
    line_count = 0
    mistake_log = []
    for line in file:
        line = line[:-1]
        line_count += 1
        try:
            total_summ += calc(line)
        except Exception:
            mistake_log.append(line_count)

with open('calc.txt', 'a') as file:
    file.write(f'total summ = {total_summ}')
    file.write(f'в строках {mistake_log} содержатся ошибки и посчитать их не удалось')
    file.close()
print(len(mistake_log))
