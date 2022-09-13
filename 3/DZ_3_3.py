# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 10.01] => 0.19

def minusdecimal(listt):

    decimalpartlist = [round(i-int(i), 10) for i in listt]      #здесь ограничился двумя знаками после запятой
    minfloat = min(decimalpartlist)
    maxfloat = max(decimalpartlist)
    result = maxfloat-minfloat
    print(round(result, 10))   #здесь тоже


minusdecimal([1.10, 1.2, 3.1, 10.01])

