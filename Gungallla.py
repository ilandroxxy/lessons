# region Домашка: ******************************************************************



'''
n = int(input())
maxi = 0
mini = 10
while n > 0:
    p = n % 10

    maxi = max(maxi, p)

    if p < mini:
        mini = p

    n //= 10
print(maxi)
print(mini)
'''
'''
n = int(input())
print(max(str(n)))
print(min(str(n)))
'''

'''
a = 5.2
print(type(a))
a = 5,2
print(type(a))
print(a)  # (5, 2)

a = int(input())
s, p, k = 0, 1, 0

while a > 0:
    b = a % 10
    s += b  # s = s + b
    p *= b  # p = p * b
    k += 1  # k = k + 1
    a //= 10  # a = a // 10
print(s)
print(k)
print(p)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 20567 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F=y∧(z≡(w→(x∨z)))
                F = y and (z == (w <= (x or z)))
                if F == 1:
                    print(x, y, z, w)
'''


# № 19234 ЕГКР 21.12.24 (Уровень: Базовый)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                # F= ¬((¬x ∨ y)∧¬w)∨¬(z∧¬(y∧ w))
                F = (not(((not x) or y) and (not w)) or (not(z and (not(y and w)))))
                if F == 0:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(w<=(x == (y or y))) and(z<=x))
                if F == 1:
                    print(x, y, z, w)
'''

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F=(x==(y<=(z or x))) and w
                if F == 1:
                    print(x, y, z, w)
'''



print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F=((z==x)<=w) and (w<=(y and x))
                if F == 1:
                    print(x, y, z, w)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2]
# КЕГЭ  = []
# на следующем уроке:
