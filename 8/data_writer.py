def first_name_writer(data):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n'.format(data))
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};'.format(data))


def last_name_writer(data):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n'.format(data))
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};'.format(data))


def telephone_writer(data):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n'.format(data))
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};'.format(data))


def description_writer(data):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n\n'.format(data))
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{};\n'.format(data))

