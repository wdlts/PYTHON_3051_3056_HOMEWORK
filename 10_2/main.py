# 1. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и
# во второй список и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
#
# 2. Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось
#
# 3. Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
#
# Sample Input:
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#
# Sample Output:
# 19


# 1. Даны два списка чисел. Найдите все числа, которые входят как в первый, так и
# во второй список и выведите их в порядке возрастания.
# Примечание. И даже эту задачу на Питоне можно решить в одну строчку.

# list1 = [1, 6, 7, 6, 3, 2]
# list2 = [3, 4, 5, 1, 4, 8]
#
# print(set([i for i in list1 for i in list2 if i in list1 and i in list2]))

# 2. Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось

# listt = ['3 4 5 6 7 8 3 5 3 6 9 6 0']
#
# strsep = str(*listt)
# listsep = list(strsep.split(' '))
# print(listsep)
#
# resultlist = ['YES' if listsep.count(i) > 1 else 'NO' for i in listsep]
# print(resultlist)

# 3. Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
#
# Sample Input:
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#
# Sample Output:
# 19
#
import re
str1 = '4\n' \
       'She sells sea shells on the sea shore;\n'\
       'The shells that she sells are sea shells Im sure.\n'\
       'So if she sells sea shells on the sea shore,\n'\
       'Im sure that the shells are sea shore shells.\n'\

#
#
print(len(list(set(re.split('\n| |,|;', str1)))))

