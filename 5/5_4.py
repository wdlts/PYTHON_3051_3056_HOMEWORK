# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# 6A1F2D7C1A17E

import re

def RLEconvert(file):

    f = open(file)
    strng = str(f.read())
    outlist = ''.join([str(len(i))+i[0] for i in [m.group(0) for m in re.finditer(r"(.)\1*", strng)]])
    f = open('5_4_output.txt', 'w')
    f.write(str(outlist))


RLEconvert('5_4_input.txt')