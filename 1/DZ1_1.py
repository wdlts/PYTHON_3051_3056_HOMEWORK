#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def dayofweek(n):

    if 1 <= n >= 5:
        print('YES')
    else:
        print('NO')


dayofweek(int(input('Input day of week ')))
