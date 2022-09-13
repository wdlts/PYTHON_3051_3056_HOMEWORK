# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')
output1 = f1.read()
print(output1)
output2 = f2.read()
print(output2)

output3 = output1.split(' ')
output4 = output2.split(' ')
print(output3)
print(output4)

def outstr(strng):

    outsplit = strng.split('*')
    return outsplit[0]


output5 = [outstr(i) if i[0].isdigit() else outstr(i) if i[0] == '-' or i[0] == '+' else '1' for i in output3]
print(output5)
output6 = [outstr(i) if i[0].isdigit() else outstr(i) if i[0] == '-' or i[0] == '+' else '1' for i in output4]
print(output6)

output7 = [output5[i-1] + output5[i] for i in range(len(output5))[2:] if (output6[i-1] == '-' or output6[i-1] == '+')]
output8 = [output6[i-1] + output6[i] for i in range(len(output6))[2:] if (output6[i-1] == '-' or output6[i-1] == '+')]

output9 = output5[:1] + output7
print(output9)
output10 = output6[:1] + output8
print(output10)

sumlist = [int(output9[i])+int(output10[i]) for i in range(len(output10))]
print(f'{sumlist[0]}*x^2 + {sumlist[1]}*x + {sumlist[2]}')












