


# № 31499 Демоверсия 2027(Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x == (not y)) <= (not (w <= x))) or (not z)
                if F == 0:
                    print(x, y, z, w)
'''

# № 29953 Апробация 14.05.26(Уровень: Базовый)
'''
print("x y z y")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not ((x <= w) <= (w == z))) and y
                if f == 1:
                    print(x,y,z,w)
'''


# № 28750 Досрочная волна 2026(Уровень: Базовый)

print("x y z y")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f= (w == z) or (not (y <= w)) or (not x)
                if f == 0:
                    print(x,y,z,w)




