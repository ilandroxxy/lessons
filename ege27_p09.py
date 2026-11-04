# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 1.  ¬x     |    (not x)
# 2. x ∧ y   |    x and y
# 3. x ∨ y   |    x or y
# 4. x → y   |    x <= y
# 5. x ≡ y   |    x == y


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



# № 23261 Основная волна 11.06.25(Уровень: Базовый)
# F=¬(w→(x≡y))∧(z→x)
# F = (not(w<=(x==y))) and (z<=x)
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F= (not(w<=(x==y))) and (z<=x)
                if F==1:
                    print(x,y,z,w)
'''


# № 23361 Резервный день 19.06.25(Уровень: Базовый)
# F=¬(y→(x≡z))∧(w→x)
# F = (not(y <= (x == z)))  and (w <= x)
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (not(y <= (x == z))) and (w <= x)
                if F == 1:
                    print(x, y, z, w)
'''


# № 31109 Основная волна 18.06.26(Уровень: Базовый)
# F=((w≡¬x)→¬(z→w))∨¬y
# F = ((w==(not x))<=(not(z<=w))) or (not y)



# № 29334 Открытый вариант 2026(Уровень: Базовый)
# F=((z→x)→(x≡y))∨¬w
# F = ((z<=x)<=(x==Y)) ro (not w)
'''
print('x,y,z,w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=((z<=x)<=(x==y)) or (not w)
                if F==0:
                    print(x,y,z,w)
'''

# № 29953 Апробация 14.05.26(Уровень: Базовый)
# F=¬((x→w)→(w≡z))∧y

'''
print('x,y,z,w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F= (not((x<=w)<=(w==z))) and y
                if F==1:
                    print(x,y,z,w)
'''


print('x,y,z,w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F=(w==z) or (not(y<=w)) or (not x)
                if F==0:
                    print(x,y,z,w)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14, 15]
# КЕГЭ = []
# todo на следующем уроке: 2, 10

