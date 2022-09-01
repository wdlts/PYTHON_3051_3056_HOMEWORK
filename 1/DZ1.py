#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# def dayofweek(n):
#
#     if 1 <= n >= 5:
#         print('YES')
#     else:
#         print('NO')
#
#
# dayofweek(int(input('Input day nr.')))


#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def trueorfalse(X, Y, Z):

    left = not(X or Y or Z)
    right = (not X) and (not Y) and (not Z)

    if (left == right) is True:
        print(True)
    else:
        print(False)


trueorfalse(False, False, False)

#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# def coordinates(x, y):
#
#     if x == 0 or y == 0:
#         print("X and/or Y should not equal 0, try again")
#     else:
#         if x > 0 and y > 0:
#             print('1')
#         elif x < 0 and y > 0:
#             print('2')
#         elif x < 0 and y < 0:
#             print('3')
#         elif x > 0 and y < 0:
#             print('4')
#
#
# coordinates(-1, -1)


#4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

# def coordrange (n):
#
#     if n == 1:
#         print('x and y')
#     elif n == 2:
#         print('-x and y')
#     elif n == 3:
#         print('-x and -y')
#     elif n == 4:
#         print('x and -y')
#
#
# coordrange(2)

#5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# import math
#
#
# def distance2d(a, b):
#
#     for i in a:
#         Xa = a[0]
#         Ya = a[1]
#     for i in b:
#         Xb = b[0]
#         Yb = b[1]
#
#     distance = int(math.sqrt(((Xb-Xa)**2) + ((Yb - Ya)**2)) * 100) / 100
#
#     print(distance)
#
#
# distance2d([int(input('Input Xa')), int(input('Input Ya'))], [int(input('Input Xb')), int(input('Input Yb'))])

