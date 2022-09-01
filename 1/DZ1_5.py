# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def distance2d(a, b):

    for i in a:
        Xa = a[0]
        Ya = a[1]
    for i in b:
        Xb = b[0]
        Yb = b[1]

    distance = int(math.sqrt(((Xb-Xa)**2) + ((Yb - Ya)**2)) * 100) / 100

    print(distance)


distance2d([int(input('Input Xa')), int(input('Input Ya'))], [int(input('Input Xb')), int(input('Input Yb'))])