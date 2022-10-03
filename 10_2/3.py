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
str1 = '4\n'\
       'She sells sea shells on the sea shore;\n'\
       'The shells that she sells are sea shells Im sure.\n'\
       'So if she sells sea shells on the sea shore,\n'\
       'Im sure that the shells are sea shore shells.\n'\

print(len(list(set(re.split('\n| ', str1.lower())))))