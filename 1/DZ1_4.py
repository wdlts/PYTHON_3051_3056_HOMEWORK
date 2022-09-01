# 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

def coordrange (n):

    if n == 1:
        print('x and y')
    elif n == 2:
        print('-x and y')
    elif n == 3:
        print('-x and -y')
    elif n == 4:
        print('x and -y')


coordrange(2)