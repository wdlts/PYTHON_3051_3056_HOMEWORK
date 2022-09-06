# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


def elemmultiple(n):

    newlist = []
    for i in range(-n, n+1):
        newlist.append(i)
    print(newlist)


    nums = open("file.txt", encoding='utf-8')

    multres = 1

    for j in nums:
        multres = multres*(newlist[int(j)]) # под позициями здесь понимаются индексы, то есть 1 - вторая позиция, первая - 0
    print(multres)


elemmultiple(int(input('Input num ')))