# region Домашка: ******************************************************************

'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a != b != c != a:
    print('Разносторонний')
else:
    print('Равнобедренный')
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 22423 (Уровень: Базовый)
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


# № 22421 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not((not(z <= y)) or (x == w) or x))
                if F == 1:
                    print(x, y, z, w)
'''


# № 22073 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z <= y) or ((w <= x) <= y)
                if F == 0:
                    print(x, y, z, w)
'''


# ¬(x) - (not x)
# ∧ - and
# ∨ - or
# → - <=
# ≡ - ==
# ¬(x→y) - (not(x <= y))

'''
# F=¬(x→y)∨(z≡w)∨z
F= (not(x <= y)) or (z == w) or z

# F=z ∨ (z≡w) ∨ ¬(y→x)
F = z or (z==w) or (not(y<=x))

# F=((x → z) → w) ∨ ¬y
F = ((x<=z)<=w ) or (not x)


# F = ¬(w → (x ≡ y ∨ y)) ∧ (z → x)
F = (not (w <= (x == (y or y))) or (z <= x))


# F = (x ≡ (y → (z ∨ x))) ∧ w
F = (x == (y <= (z or x))) or w


# F = ((z ≡ x) → w) ∧ (w → (y ∧ x))
F =((z == x) <= w) and (w <= (y and x))

# F=(¬((¬y→x)→w))∨(z→x)
F = ((not(((not y) <= x) <= w )) or (z <= x))


# F=x∧(z→w)∧¬y
F=x and (z<=w) and (not y)
x y z w
1 0 0 0
1 0 0 1
1 0 1 1
# F=(((y→¬x)∧y)≡w)∧z
F=(((y<=(not x) and y)==w) and z
# F=((w→z)≡(x→¬y))∧(x∨z)
F=((w<=z)==(x<=(not y))and(x or z)


# F=x∧((w→y)≡z)
F=x and (w<=y)==z)

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (z <= y) or ((w <= x) <= y)
                if F == 0:
                    print(x, y, z, w)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, ]
# КЕГЭ = []
# на следующем уроке:
