# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for y in alphabet[:17]:
    for x in alphabet[:15]:
        A = int(f'123{x}5', 15)
        B = int(f'67{y}9', 17)
        if (A + B) % 131 == 0:
            print((A + B) // 131)
            exit()
'''

'''
for x in range(9999999):
    if str(bin(4**2015+2**x-2**2015+15)).count('1')==500:
        print(x)
        break
'''

'''
x = 4
print(f'123{x}56')  # 123456

print(f'{8:b}')

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for p in range(8, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'1{x}77', p) + int(f'{x}{x}77', p) == int(f'{y}0{y}{y}', p):
                print(int(y+x+y+x, p))
'''


# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
'''
x = 4*3125**2019 + 3* 625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
M = []
while x > 0:
    M.append(x % 25)
    x //= 25
M.reverse()
print(len([x for x in M if x > 10]))
'''

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    n = 7**91 + 7 ** 160 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    M.reverse()
    if M.count(0) == 70:
        print(x)
'''
# Ответ: 2029

'''
s = 'abcde'

print(f'Первый элемент строки s: {s[0]}')
print(f'Второй элемент строки s: {s[1]}')
print(f'Последний элемент строки s: {s[-1]}')
# Первый элемент строки s: a
# Второй элемент строки s: b
# Последний элемент строки s: e


# Срезы строк:

s = 'abcde'

print(s[2:4])  # cd
print(s[::2])  # ace
print(s[1::2])  # bd
print(s[::-1])  # edcba
'''

# Методы строк:
'''
s = '213213412312'
s = s.replace('2', '*')
print(s)  # *13*1341*31*

s = s.replace('*', '2', 2)
print(s)  # 21321341*31*


s = s.replace('2', '*', 1)
print(s)  # *1321341*31*


print(s.count('*'))  #

print(s.index('*'))  # 0
print(s.rindex('*'))  # 11

id = '192.213.12.9'
print(id.split('.'))  # ['192', '213', '12', '9']
print([int(x) for x in id.split('.')])  # [192, 213, 12, 9]
ID = id.split('.')

new_id = '**'.join(ID)
print(new_id)  # 192**213**12**9
'''

# № 17553 Основная волна 08.06.24 (Уровень: Базовый)
'''
s = '8' * 83
while '111' in s or '88888' in s:
    if '111' in s:
        s = s.replace('111', '88', 1)
    else:
        s = s.replace('88888', '8', 1)
print(s)  # 888
'''


# № 16378 ЕГКР 27.04.24 (Уровень: Базовый)
'''
R = []
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum([int(x) for x in s])
    R.append(summa)
    print(max(R))
'''

# № 17557 Основная волна 08.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n-1)

print((F(2024) // 16 - F(2023)) / F(2022))
'''
# 253886.5

# OverflowError: integer division result too large for a float


# № 17562 Основная волна 08.06.24 (Уровень: Базовый)
# A. Прибавить 1
# B. Прибавить 2
# C. Прибавить 3
# Сколько существует программ, которые преобразуют число 5 в число 11,
# и при этом траектория вычислений содержит число 7?
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))


def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a+3, b)

print(F(5, 7) * F(7, 11))
'''

# № 17534 Основная волна 07.06.24 (Уровень: Базовый)
'''
def F(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-1, b) + F(a//2, b)

print(F(30, 8) * F(8, 1))
'''


# № 16387 ЕГКР 27.04.24 (Уровень: Базовый)
'''
def F(a, b):
    if a > b or a == 16:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(2, 9) * F(9, 18))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2*, 3, 4, 6, 7, 9*, 10, 11, 18, 19-21]
# КЕГЭ  = [2, 12, 14, 16, 23]
# на следующем уроке:
