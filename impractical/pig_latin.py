"""pig latin"""
def input_and_check():
    """w8 and chek inputed word from user
    if input is correct - start convert"""
    while True:
        user_input = input('pls enter any word: \n')
        if user_input.isalpha():
            convert_word(user_input=user_input)
            break


def convert_word(user_input):
    """converting word inputed by user to a
    pig-latin style"""
    vovels = ['a', 'e', 'i', 'o', 'u', 'y']
    new_word = str
    if user_input[0].lower() in vovels:
        new_word = user_input[1:] + 'way'
        print(new_word)
    else:
        new_word = user_input[1:] + user_input[0] + 'ay'
    print(new_word)

input_and_check()
