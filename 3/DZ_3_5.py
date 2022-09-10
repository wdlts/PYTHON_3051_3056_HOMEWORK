# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negafibonacci(n):

    fib1 = -1
    fib2 = 1
    positivelist = []
    i = 0
    while i < n+3:
        fib_sum = fib1+fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        positivelist.append(fib2)

    templistneg = [(positivelist[i]*(-1)) if i % 2 == 0 else positivelist[i] for
                   i in range(len(positivelist))][:-2]

    resultposneg = list(list(reversed(templistneg))+positivelist[1:-2])
    print((resultposneg))


negafibonacci(8)