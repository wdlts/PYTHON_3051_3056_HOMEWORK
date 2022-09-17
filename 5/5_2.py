# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# # Variant1
#
# import random
#
# candies = 101
# candiesplayer1 = 0
# candiesplayer2 = 0
# countmoves = 0
#
#
# draft = random.randint(1, 2)
# print('Начинает игрок ' + str(draft))
#
# while True:
#         if candies > 0 and draft != 2:
#             moveplayer1 = int(input('Player 1 Введите число конфет '))
#             while moveplayer1 > 28:
#                 moveplayer1 = int(input('Too much! Введите число конфет '))
#             candiesplayer1 += moveplayer1
#             candies -= moveplayer1
#             print('Player 1 candies: ' + f'{candiesplayer1}')
#             print('Осталось конфет: ' + f'{candies}')
#             if candies == 0:
#                 print('Player 1 wins!')
#                 exit()
#             draft = 2
#         elif candies > 0 and draft != 1:
#             moveplayer2 = int(input('Player 2 Введите число конфет '))
#             while moveplayer2 > 28:
#                 moveplayer2 = int(input('Too much! Введите число конфет '))
#             candiesplayer2 += moveplayer2
#             candies -= moveplayer2
#             print('Player 2 candies: ' + f'{candiesplayer2}')
#             print('Осталось конфет: ' + f'{candies}')
#             if candies == 0:
#                 print('Player 2 wins!')
#                 exit()
#             draft = 0


# # Variant2

# import random
#
# candies = 101
# candiesplayer1 = 0
# candiesplayer2 = 0
# countmoves = 0
#
#
# draft = random.randint(1, 2)
# if draft == 2:
#     print('Начинает игрок Bot')
# else:
#     print('Начинает Human')
#
# while True:
#         if candies > 0 and draft != 2:
#             moveplayer1 = int(input('Human Введите число конфет '))
#             while moveplayer1 > 28:
#                 moveplayer1 = int(input('Too much! Введите число конфет '))
#             candiesplayer1 += moveplayer1
#             candies -= moveplayer1
#             print('Human candies: ' + f'{candiesplayer1}')
#             print('Осталось конфет: ' + f'{candies}')
#             if candies == 0:
#                 print('Human wins!')
#                 exit()
#             draft = 2
#         elif candies > 0 and draft != 1:
#             if candies < 29:
#                 moveplayer2 = random.randint(1, candies)
#             else:
#                 moveplayer2 = random.randint(1, 29)
#             # while moveplayer2 > 28:
#             #     moveplayer2 = int(input('Too much! Введите число конфет '))
#             candiesplayer2 += moveplayer2
#             candies -= moveplayer2
#             print('Bot candies: ' + f'{candiesplayer2}')
#             print('Осталось конфет: ' + f'{candies}')
#             if candies == 0:
#                 print('Bot wins!')
#                 exit()
#             draft = 0


# Variant3

import random

candies = 101
candiesplayer1 = 0
candiesplayer2 = 0
countmoves = 0
moveplayer1 = 0
moveplayer2 = 0

draft = random.randint(1, 2)
if draft == 2:
    print('Начинает игрок Bot')
else:
    print('Начинает Human')

while True:
        if candies > 0 and draft != 2:
            moveplayer1 = int(input('Human Введите число конфет '))
            while moveplayer1 > 28:
                moveplayer1 = int(input('Too much! Введите число конфет '))
            candiesplayer1 += moveplayer1
            candies -= moveplayer1
            print('Human candies: ' + f'{candiesplayer1}')
            print('Осталось конфет: ' + f'{candies}')
            if candies == 0:
                print('Human wins!')
                exit()
            draft = 2
        elif candies > 0 and draft != 1:
            if candies < 29:
                moveplayer2 = candies
            elif candies < 100:
                for i in range(1, 29):
                    if (candies - i) % (i+1) == 0:
                        moveplayer2 = i
                # moveplayer2 = 29 - moveplayer1
            else:
                moveplayer2 = 28
            candiesplayer2 += moveplayer2
            candies -= moveplayer2
            print('Bot candies: ' + f'{candiesplayer2}')
            print('Осталось конфет: ' + f'{candies}')
            if candies == 0:
                print('Bot wins!')
                exit()
            draft = 0

