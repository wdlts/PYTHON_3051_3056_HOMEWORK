# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def unrepeated(lst):

    def counter(n):
        cnt = 0
        for i in lst:
            if i == n:
                cnt += 1
        return(cnt)

    print([i for i in lst if counter(i) == 1])


unrepeated([1, 1, 2, 3, 4, 6, 4, 5, 5])