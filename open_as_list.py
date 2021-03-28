

def opener(file):
    try:
        with open(file=file, mode='r') as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except Exception as exc:
        print(exc.args)

