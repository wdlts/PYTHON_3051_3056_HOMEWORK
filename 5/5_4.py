# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# 6A1F2D7C1A17E

import re

#это сжатие
def RLEconvert(file):
    f = open(file)
    strng = str(f.read())
    outlist = ''.join([str(len(i)) + i[0] for i in [m.group(0) for m in re.finditer(r"(.)\1*", strng)]])
    f = open('5_4_output.txt', 'w')
    f.write(str(outlist))

# это восстановление данных
    templist = [str(len(i)) + i[0] for i in [m.group(0) for m in re.finditer(r"(.)\1*", strng)]]

    def numstostr(strng):
        numstr = [char for char in strng]
        numstr1 = int(''.join(i for i in numstr if i.isdigit()))
        return numstr1

    listnums = [numstostr(i) for i in templist]
    listletters = [i[-1] for i in templist if not i.isdigit()]
    outlistdecoded = ''.join([listnums[i]*listletters[i] for i in range(len(listnums))])
    f.write(str(' \n'))
    f.write(str(outlistdecoded))

RLEconvert('5_4_input.txt')
