# Вычислить число c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141
import math

def accuracy(num):

    accuracy = len(num)
    pinum = list(str(math.pi))
    print(math.pi)
    print(float(''.join(pinum[:accuracy])))

accuracy(str(input('Input accuracy ')))