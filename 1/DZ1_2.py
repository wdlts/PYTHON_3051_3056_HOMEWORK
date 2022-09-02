#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def trueorfalse(X, Y, Z):

    left = not(X or Y or Z)
    right = (not X) and (not Y) and (not Z)

    if (left == right) is True:
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')


trueorfalse(bool(input('Введите значение для X ')), bool(input('Введите значение для Y ')), bool(input('Введите значение для Z ')))