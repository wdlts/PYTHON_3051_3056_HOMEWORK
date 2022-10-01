from get_data import get_request


def search():
    word = get_request()
    with open("log.csv", encoding='utf-8') as f:
        return ((str(''.join([' '.join(line.split(';')[:-1]) + '\n' for line in f if word in line]))))
def search_null():
    word = ''
    with open("log.csv", encoding='utf-8') as f:
        return ((str(''.join([' '.join(line.split(';')[:-1]) + '\n' for line in f if word in line]))))
