# # 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка
# # и возвращает словарь, в котором каждый элемент списка является и ключом
# # и значением. Предполагается, что элементы списка будут соответствовать
# # правилам задания ключей в словарях.
#
# def to_dict(lst):
#     print({i:i for i in lst})
# to_dict(['one', 'two', 'three', 'four', 'five'])

# 2. # Иван решил создать самый большой словарь в мире.
# Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и
# обновляет созданный им словарь my_dict, состоящий всего из одного элемента
# «first_one» со значением «we can do it». Воссоздайте эту функцию.

# def biggest_dict():
#     my_dict = {'first_one': 'we can do it'}
#     while True:
#         k = input('Input k')
#         if k == '':
#             break
#         v = input('Input v')
#         my_dict[k] = v
#     print(my_dict)
#     return my_dict
#
#
# biggest_dict()

# def biggestdict(nkeys):
#     r = {'first_one': 'we can do it'}
#     for _ in range(nkeys):
#         print('Enter key (empty enter - exit)')
#         k = input()
#         if k == '':
#             break
#         print('Enter value')
#         v = input()
#         r[k] = v
#     print(r)
#     return r
# biggestdict(2)



# def getDict():
#     r = {}
#     while (True):
#         print('Enter key (empty enter - exit)')
#         k = input()
#         if k == '':
#             break
#         print('Enter value')
#         v = input()
#         r[k] = v
#     return r
#
#
# d = getDict()
# print(d)
# 3.
# Дана строка в виде случайной последовательности чисел от 0 до 9.
# Требуется создать словарь, который в качестве ключей будет принимать данные числа
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence), принимающую строку из цифр.
# Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

stringg = '1 1 1 1 1 1 3 6 6 6 3 8 8 8 8 4 6'
listt = list(stringg.split(' '))


def resultcount(item):
    itemcount = listt.count(item)
    return itemcount

r = {}

for i in range(len(listt)):
    k = int(listt[i])
    v = resultcount(listt[i])
    r[k] = v
print(r)

outdict = {}
sortedkeys = reversed(sorted(r, key=r.get))
for w in sortedkeys:
    outdict[w] = r[w]
print(outdict)

