# region Домашка: ******************************************************************
'''
def f(st, c, cnt):
    if c <= 3:
        if st % 2 == 0:
            cnt += 1
            return 0
    else:
        return cnt

    f(st + 1, c + 1, cnt)
    f(st + 2, c + 1, cnt)
    f(st * 3, c + 1, cnt)

f(4, 0, 0)
'''



# № 6093 /dev/inf 02.2023 (Уровень: Средний)
'''
def F(a, c):
    global cnt
    if c > 3:
        return 0
    else:
        if a % 2 == 0:
            cnt += 1
    return F(a+1, c+1) + F(a+2, c+1) + F(a*3, c+1)


cnt = 0
F(4, 0)
print(cnt)
'''

'''
def F(a, c):
    if c > 3:
        return 0
    return (a % 2 == 0) + (F(a+1, c+1) + F(a+2, c+1) + F(a*3, c+1))

cnt = F(4, 0)
print(cnt)
'''


# № 5838 (Уровень: Средний)
'''
def F(a, b, c):
    if a > b:
        return 0
    elif a == b:
        if len(c) % 2 != 0 and all(x == 'B' for x in c[1::2]):
            return 1
        else:
            return 0

    else:
        return F(a+3, b, c+'A') + F(a+2, b, c+'B') + F(a*2, b, c+'C')


print(F(1, 50, ''))

# Вариант 2
def F(a, b, c):
    if a >= b:
        return a == b and len(c) % 2 != 0 and all(x == 'B' for x in c[1::2])

    return F(a+3, b, c+'A') + F(a+2, b, c+'B') + F(a*2, b, c+'C')


print(F(1, 50, ''))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

print('x y z w f1 f2')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f1 = (w == x) and (y <= z)
                f2 = (w <= x) <= (y == z)

                print(w, y, x, z, int(f1), int(f2))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 14, 17, 22, 23, 24]
# на следующем уроке:


# Первый пробник 21.12.24:
# Yegor 21/27 -> 80 вторичных баллов +[1-5, 7, 9-12, 14-16, 18-24, 27] -[6, 8, 13, 25, 26]
