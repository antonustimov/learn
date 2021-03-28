from pprint import pprint

def my_dict(alphabet):
    """creates dict with keys - letters of alpha
    and values are 0 and returns it"""
    my_dict = {}
    for i in alphabet:
        my_dict[i] = []
    return my_dict

def analyzer(text, dict_for_data):
    with open(text_for_analyze, 'r') as file:
        for line in file:
            for letter in line:
                if letter in dict_for_data:
                    dict_for_data[letter].append(letter)
    return dict_for_data











alphabet = 'abcdefghijklmnopqrstwvyz'
text_for_analyze = '/Users/ant__on/PycharmProjects/learn/lesson_009/python_snippets/byron.txt'
dict_for_data = my_dict(alphabet)
result = analyzer(text_for_analyze, dict_for_data)

pprint(result)