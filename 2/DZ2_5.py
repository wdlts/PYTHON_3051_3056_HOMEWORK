# Реализуйте алгоритм перемешивания списка.
import random

# random.shuffle(newlist) #это вариант со встроенной функцией


#а это чуть более сложный вариант с перемешиванием индексов списка, а не самого списка

newlist = [1, 2, 3, 4, 5]
shuffledlist = [] # результирующий список с перемешанными элементами

newindlist = []         #создание списка с индексами
for i in range(len(newlist)):
    newindlist.append(i)

random.shuffle(newindlist) #перемешивание индексов

for j in newindlist:        #формирование результирующего списка по перемешанным индексам
    shuffledlist.append(newlist[j])
print(shuffledlist)


