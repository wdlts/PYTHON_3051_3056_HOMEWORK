#2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            result = ((not(X or Y or Z)) == (not (X) and not (Y) and not (Z)))
            print(result)





