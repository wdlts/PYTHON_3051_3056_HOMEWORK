# 3.
# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

stringg = '1 1 1 1 1 1 3 6 6 6 3 8 8 8 8 4 6'
listt = list(stringg.split(' '))


def count_it(item):
    itemcount = listt.count(item)
    return itemcount
r = {}
for i in range(len(listt)):
    k = int(listt[i])
    v = str(count_it(listt[i]))
    r[k] = v

outdict = {}
sortedkeysdict = reversed(sorted(r, key=r.get))
for w in sortedkeysdict:
    outdict[w] = r[w]

indexlist = [k for k, v in outdict.items()][:3]
outdict2 = {}
for w in indexlist:
    outdict2[w] = r[w]
print(outdict2)