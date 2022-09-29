from data_provider import get_search
def search(word):
    with open("log.csv", encoding='utf-8') as f:
        print(str(''.join([' '.join(line.split(';')[:-1]) + '\n' for line in f if word in line])))
search(get_search())







