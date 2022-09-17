# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


def primefactor(n):

    factorlist = []

    for i in range(2, n):
        while n % i == 0:
            n //= i
            factorlist.append(i)

    print(factorlist)


primefactor(20)