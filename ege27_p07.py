# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 31499 Демоверсия 2027(Уровень: Базовый)
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


# № 31109 Основная волна 18.06.26(Уровень: Базовый)
# F=((w≡¬x) → ¬(z→w)) ∨ ¬y
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w==(not x))<=(not(z<=w)))or(not y)
                if F == 0:
                    print(x, y, z, w)
'''


# № 29953 Апробация 14.05.26(Уровень: Базовый)
# F=¬((x→w)→(w≡z))∧y
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((x<=w)<=(w==z))) and y
                if F == 1:
                    print(x, y, z, w)
'''


# № 22423 (Уровень: Базовый)
# F=((z→x)∧(x→y))∨(w≡(z∨x))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z<=x)and(x<=y))or(w==(z or x))
                if F == 0:
                    print(x, y, z, w)
'''

# № 22421 (Уровень: Базовый)
# F=¬(¬(z→y)∨(x≡w)∨x)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((not(z<=y))or(x==w)or x))
                if F == 1:
                    print(x, y, z, w)
'''

# № 20820 (Уровень: Базовый)
# F=(((y→¬x)∧y)≡w)∧z
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((( y <= (not x)) and y) == w) and z
                if F == 1:
                    print(x, y, z, w)
'''


# № 29334 Открытый вариант 2026(Уровень: Базовый)
# F=((z→x)→(x≡y))∨¬w

print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=((z<=x)<=(x==y))or(not w)
                if F==0:
                    print(x,y,z,w)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 14, 15, 16, 18]
# КЕГЭ = []
# todo на следующем уроке:
