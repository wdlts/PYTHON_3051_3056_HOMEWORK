# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math


def distance2d(Xa, Ya, Xb, Yb):

    distance = int(math.sqrt(((Xb-Xa)**2) + ((Yb - Ya)**2)) * 100) / 100
    print(distance)


distance2d(int(input('Xa ')), int(input('Ya ')), int(input('Xb ')), int(input('Yb ')))