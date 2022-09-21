# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные
# (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.
# 1.
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#ПРЕДЫДУЩЕЕ РЕШЕНИЕ
# - 6782 -> 23
# - 0,56 -> 11
#
# def digitsum(n):
#     summ = 0
#     for i in range(len(n)):
#         if n[i].isdigit():
#             summ += int(n[i])
#     print(summ)
#
#
# digitsum(str(input('Input num ')))

#НОВОЕ РЕШЕНИЕ
# inputnum = '6782'
# result = sum(int(i) for i in inputnum if i.isdigit())
# print(result)

# 2.
# Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.

#ПРЕДЫДУЩЕЕ РЕШЕНИЕ

# def listsum(n):
#
#     res = []
#
#     for i in range(n):
#         res.append(((1 + (1 / (i + 1))) ** (i + 1))) # числа начинаются с 1, иначе деление на 0
#
#     print(res)
#     print(sum(res))
#
#
# listsum(int(input('Введите число ')))

# НОВОЕ РЕШЕНИЕ
# n = 10
# result = [((1 + (1 / (i+1))) ** (i+1)) for i in range(n)]
#
# print(result)


# 3.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]

#ПРЕДЫДУЩЕЕ РЕШЕНИЕ

# def pairmultiply(listnum):
#
#     length = round(len(listnum)/2)
#     if len(listnum) % 2 == 1:
#         list1 = [i for i in listnum[:length+1]]
#     else:
#         list1 = [i for i in listnum[:length]]
#     list2 = [j for j in listnum[length:]]
#     result = [i * j for i, j in zip(list1, reversed(list2))]
#     print(result)



# НОВОЕ РЕШЕНИЕ
# import math
#
# listt = [2, 3, 4, 5, 6]
# listt2 = [i for i in reversed(listt)]
# result = list(map(lambda x, y: x * y, listt, listt2))
# print([result[i] for i in range((math.ceil(len(result) / 2)))])







