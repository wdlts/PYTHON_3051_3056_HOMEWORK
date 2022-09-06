# Задайте список из n чисел последовательности (1+(1/n))^n и выведите на экран их сумму.


def listsum(n):

    res = []

    for i in range(n):
        res.append(((1 + (1 / (i+1))) ** (i+1))) # числа начинаются с 1, иначе деление на 0

    print(res)
    print(sum(res))


listsum(int(input('Введите число ')))