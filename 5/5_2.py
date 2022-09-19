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

variant = input(' Игра против человека: 1.\n Игра против глупого бота: 2.\n Игра против умного бота: 3.\n Ваш выбор: ')

match variant:

    case '1':
        import random

        candies = 2021
        candiesplayer1 = 0
        candiesplayer2 = 0
        countmoves = 0
        draft = random.randint(1, 2)
        print('Начинает игрок ' + str(draft))
        while True:
            if candies > 0 and draft != 2:
                moveplayer1 = int(input('Игрок 1, введите число конфет '))
                while moveplayer1 > 28:
                    moveplayer1 = int(input('Слишком много взяли! Возьмите не больше 28 '))
                candiesplayer1 += moveplayer1
                candies -= moveplayer1
                print('Конфеты Игрока 1: ' + f'{candiesplayer1}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Игрок 1 выиграл!')
                    exit()
                draft = 2
            elif candies > 0 and draft != 1:
                moveplayer2 = int(input('Игрок 2, введите число конфет '))
                while moveplayer2 > 28:
                    moveplayer2 = int(input('Слишком много взяли! Возьмите не больше 28 '))
                candiesplayer2 += moveplayer2
                candies -= moveplayer2
                print('Конфеты Игрока 2: ' + f'{candiesplayer2}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Игрок 2 выиграл!')
                    exit()
                draft = 0
    case '2':
        import random

        candies = 2021
        candiesplayer1 = 0
        candiesplayer2 = 0
        countmoves = 0
        draft = random.randint(1, 2)
        if draft == 2:
            print('Начинает Бот')
        else:
            print('Начинает Человек')
        while True:
            if candies > 0 and draft != 2:
                moveplayer1 = int(input('Человек, возьмите конфеты '))
                while moveplayer1 > 28:
                    moveplayer1 = int(input('Слишком много взяли! Возьмите не больше 28 '))
                candiesplayer1 += moveplayer1
                candies -= moveplayer1
                print('Конфеты Человека: ' + f'{candiesplayer1}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Человек выиграл!')
                    exit()
                draft = 2
            elif candies > 0 and draft != 1:
                if candies < 29:
                    moveplayer2 = random.randint(1, candies)
                else:
                    moveplayer2 = random.randint(1, 29)
                candiesplayer2 += moveplayer2
                candies -= moveplayer2
                print('Конфеты Бота: ' + f'{candiesplayer2}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Бот выиграл!')
                    exit()
                draft = 0
    case '3':
        import random

        candies = 2021
        candiesplayer1 = 0
        candiesplayer2 = 0
        countmoves = 0
        moveplayer1 = 0
        moveplayer2 = 0
        draft = random.randint(1, 2)
        if draft == 2:
            print('Начинает Бот')
        else:
            print('Начинает Человек')
        while True:
            if candies > 0 and draft != 2:
                moveplayer1 = int(input('Человек, возьмите конфеты '))
                while moveplayer1 > 28:
                    moveplayer1 = int(input('Слишком много взяли! Возьмите не больше 28 '))
                candiesplayer1 += moveplayer1
                candies -= moveplayer1
                print('Конфеты человека: ' + f'{candiesplayer1}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Человек выиграл!')
                    exit()
                draft = 2
            elif candies > 0 and draft != 1:
                if candies < 29:
                    moveplayer2 = candies
                elif candies < 2021:
                    if candies % 29 == 0:
                        moveplayer2 = 1
                    else:
                        moveplayer2 = candies % 29
                else:
                    moveplayer2 = 28
                candiesplayer2 += moveplayer2
                candies -= moveplayer2
                print('Конфеты Бота: ' + f'{candiesplayer2}')
                print('Осталось конфет: ' + f'{candies}')
                if candies == 0:
                    print('Бот выиграл!')
                    exit()
                draft = 0
