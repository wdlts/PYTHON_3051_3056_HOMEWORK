# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def polynominal(k):

    output = []
    for i in range(1, k):
        output.append(f'{random.randint(0, 100)}x^{k}')
        k -= 1
    checkstr = [i for i in output if int(i[0]) != 0]
    klast = random.randint(0, 100)
    if klast > 0:
        result = str(' + '.join(checkstr)) + ' + ' f'{klast}'' = 0'
    else:
        result = str(' + '.join(checkstr)) + ' = 0'
    f = open('file.txt', 'w')
    f.write(str(result))
    print(result)


polynominal(2)