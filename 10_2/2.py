# 2. Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось

listt = ['3 4 5 6 7 8 3 5 3 6 9 6 0']
strsep = str(*listt)
listsep = list(strsep.split(' '))



resultlist1 = ['YES' if listsep[i] in listsep[:i] else 'NO' for i in range(len(listsep))]

resultlist2 = ['YES' if listsep.count(i) > 1 else 'NO' for i in listsep]

print(resultlist1)
print(resultlist2)

