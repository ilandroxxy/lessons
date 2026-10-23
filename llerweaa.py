



# № 31499 Демоверсия 2027(Уровень: Базовый)
# F = ((x≡¬y) → ¬(w→x)) ∨ ¬z
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x == (not y)) <= (not(w <= x))) or (not z)
                if F == 0:
                    print(x, y, z, w)
'''


# № 29953 Апробация 14.05.26(Уровень: Базовый)
# F=¬((x→w) → (w≡z)) ∧ y
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not ((x <= w) <= (w == z))) and y
                if F == 1:
                    print(x, y, z, w)
'''


# № 29334 Открытый вариант 2026(Уровень: Базовый)
# F=((z→x) → (x≡y)) ∨ ¬w
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= x) <= (x == y)) or (not w)
                if F == 0:
                    print(x, y, z, w)
'''


# № 28750 Досрочная волна 2026(Уровень: Базовый)
# F=(w≡z)∨¬(y→w)∨¬x
# F = (w == z) or (not (y <= w)) or (not x)



# № 22423 (Уровень: Базовый)
# F=((z→x)∧(x→y))∨(w≡(z∨x))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= x) and (x <= y)) or (w == (z or x))
                if F == 0:
                    print(x, y, z, w)
'''


# № 25341 ЕГКР 13.12.25(Уровень: Базовый)
# F=(w≡z)∨¬(y→w)∨¬x

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w == z) or (not(y <= w)) or (not x)
                if F == 0:
                    print(x, y, z, w)












# todo На следующем уроке:












