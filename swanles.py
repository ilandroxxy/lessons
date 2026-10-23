

# № 31499 Демоверсия 2027(Уровень: Базовый)

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x == (not y)) <= (not(w <= x))) or (not z)
                if F == 0:
                    print(x, y, z, w)