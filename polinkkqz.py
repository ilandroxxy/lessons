
# Команды математической логики на python
# ¬x         |    (not x)
# x ∧ y      |    x and y
# x ∨ y      |    x or y
# x → y      |    x <= y
# x ≡ y      |    x == y


# ¬(x ∧ y)                  |   (not(x and y))
# (w ≡ z) ∧ y               |   (w == z) and y
# ¬(x → w)                  |   (not(x <= w))
# ((z → x) → (x ≡ y)) ∨ ¬w  |  ((z <= x) <= (x == y)) or (not w)


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
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w == (not x)) <= (not(z <= w))) or (not y)
                if F == 0:
                    print(x, y, z, w)
'''
