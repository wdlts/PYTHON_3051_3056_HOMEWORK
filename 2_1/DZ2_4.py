# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


def elemmultiple(n):

    nums = [int(i) for i in input('Введите цифры через пробел ').split(' ')]
    print(nums)
    newlist = []
    for i in range(-n, n+1):
        newlist.append(i)
    print(newlist)

    multres = 1
    for j in nums:
        multres = multres*(newlist[int(j)]) # под позицией понимаются индексы, то есть 1 - второй элемент, первый - 0
    print(multres)


elemmultiple(int(input('Input num ')))