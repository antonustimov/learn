from open_as_list import opener
from pprint import pprint








file_for_analyze = opener('/Users/ant__on/PycharmProjects/learn/113k_dict.txt')
list_of_palindroms = []
for word in file_for_analyze:
    if word[:] == word[::-1]:
        list_of_palindroms.append(word)

pprint(list_of_palindroms)
