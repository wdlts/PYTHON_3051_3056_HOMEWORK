# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def digitsum(n):
    summ = 0
    for i in range(len(n)):
        if n[i].isdigit():
            summ = summ + int(n[i])
    print(summ)


digitsum(str(input('Input num ')))