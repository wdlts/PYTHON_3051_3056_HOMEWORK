#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def trueorfalse(X, Y, Z):

    left = not(X or Y or Z)
    right = (not X) and (not Y) and (not Z)

    if (left == right) is True:
        print(True)
    else:
        print(False)


trueorfalse(bool(input('Input X ')), bool(input('Input Y ')), bool(input('Input Z ')))