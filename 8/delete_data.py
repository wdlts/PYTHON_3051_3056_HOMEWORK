import os
from get_data import get_request
def delete():
    word = get_request()
    tempfile = 'logtemp.csv'
    closef = open('log.csv')
    closef.close()

    with open('log.csv', 'r', encoding='utf-8') as f, open(tempfile, 'w', encoding='utf-8') as outf:
        for line in f:
            if word not in line:
                outf.write(line)
    closef.close()
    os.remove('log.csv')
    os.rename('logtemp.csv', 'log.csv')
    return('\nЗапись удалена\n')