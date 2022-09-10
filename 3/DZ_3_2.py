# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]


def pairmultiply(listnum):

    length = round(len(listnum)/2)
    if len(listnum) % 2 == 1:
        list1 = [i for i in listnum[:length+1]]
    else:
        list1 = [i for i in listnum[:length]]
    list2 = [j for j in listnum[length:]]
    result = [i * j for i, j in zip(list1, reversed(list2))]
    print(result)


pairmultiply([2, 3, 5, 6])