# region Домашка: ******************************************************************

'''
def con(num: int, cen: int):
    alp = '01234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    res = ''
    while num > 0:
        res += alp[num % cen]
        num //= cen
    return res[::-1]


R = []
for n in range(11, 1000):
    s = con(n, 3)
    if s.count('0') + s.count('2') > s.count('1'):
        s = '22' + s
    else:
        s = '11' + s

    r = int(s, 3)
    if r > 100:
        R.append(r)
print(min(R))
'''

# № 12468 (Уровень: Базовый)
'''
R = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    a = int(f'78{x}79643', 19)
    b = int(f'25{x}43', 19)
    c = int(f'63{x}5', 19)
    if (a + b + c) % 18 == 0:
        R.append((a + b + c) // 18)
print(min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
def my_int(R, b):
    R = R[::-1]
    summa = 0
    for i, x in enumerate(R, 0):
        summa += x*b**i
    return summa

def my_int(R: list, b: int):
    return sum([x*b**i for i, x in enumerate(R[::-1], 0)])


print(int('1000', 2))  # 8
print(my_int([1, 0, 0, 0], 2))  # 8
'''


# № 13096 (Уровень: Средний)
'''
def my_int(R, b):
    return sum([x*b**i for i, x in enumerate(R[::-1], 0)])


for x in range(0, 39):
    for y in range(0, 39):
        A = my_int([5, 8, x, 7, 2, 3, y, 4, 9], 39)
        if A % 38 == 0:
            B = my_int([y, x], 39)
            if (B**0.5).is_integer() and B != 0:
                print(B)
'''

'''
def my_int(R, b):
    return sum([x*b**i for i, x in enumerate(R[::-1], 0)])


R = []
for x in range(10, 67):
    for y in range(0, x):
        A = my_int([7, 3, x, 1, y], 67)
        B = my_int([4, 9, y, 6], x)
        R.append(A + B)
print(len(set(R)))
'''


# Тип 23 №27551
# 1.Прибавить 1.
# 2.Умножить на 2.
# Сколько существует программ, которые преобразуют исходное число 1 в число 20,
# и при этом траектория вычислений содержит ровно одно из чисел 9 и 10?

'''
def F(a, b):
    if a >= b or a == 9:
        return a == b
    return F(a+1, b) + F(a*2, b)

def G(a, b):
    if a >= b or a == 10:
        return a == b
    return G(a+1, b) + G(a*2, b)


print(F(1, 10) * F(10, 20))
print(G(1, 9) * G(9, 20))
'''

# True  ['1', '2', '4', '8', '18', '19']
'''
def F(a, b, c):
    if a > b:
        return 0
    elif a == b:
        c = c.split()
        if ('9' in c) != ('10' in c):
            # print(a == b, c)
            return 1
        else:
            return 0
    else:
        return F(a+1, b, c+' '+str(a)) + F(a*2, b, c+' '+str(a))

print(F(1, 20, ''))


def F(a, b, c):
    if a >= b:
        c = c.split()
        return a == b and ('9' in c) != ('10' in c)
    return F(a+1, b, c+' '+str(a)) + F(a*2, b, c+' '+str(a))

print(F(1, 20, ''))
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 14, 23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Александр 19/25 -> 75 вторичных баллов +[1-5, 7, 9-10, 12, 14-16, 18-22, 24, 25] -[6, 8, 11, 13, 17, 23]
# Саша
