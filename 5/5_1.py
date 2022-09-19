# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def redstring(file):

    f = open(file, encoding='utf-8')
    inputstr = str(f.read())
    result = ' '.join([i for i in inputstr.split(' ') if 'абв' not in i])
    f = open('5_1_output.txt', 'w')
    f.write(str(result))


redstring('5_1_input.txt')

