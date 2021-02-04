# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
# from pprint import pprint
# import district
# from district import central_street
# from district import soviet_street
# from district.central_street import house1
# from district.central_street import house2
from district.central_street.house1 import room1 as a
from district.central_street.house1 import room2 as b
from district.central_street.house2 import room1 as c
from district.central_street.house2 import room2 as d
# from district.soviet_street import house1
# from district.soviet_street import house2
from district.soviet_street.house1 import room1 as a_1
from district.soviet_street.house1 import room2 as b_1
from district.soviet_street.house2 import room1 as c_1
from district.soviet_street.house2 import room2 as d_1


residents = []
residents.extend(a.folks)
residents.extend(b.folks)
residents.extend(c.folks)
residents.extend(d.folks)
residents.extend(a_1.folks)
residents.extend(b_1.folks)
residents.extend(c_1.folks)
residents.extend(d_1.folks)

print('на районе обитают :', ', '.join(residents))




