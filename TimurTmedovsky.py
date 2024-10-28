# region Домашка: ******************************************************************

'''
for n in range(1, 1000):
    s = f'{n:b}'
    s = s.replace('1', '*').replace('0', '1').replace('*', '0')
    s = '1' + s
    if s.count('1') % 2 != 0:
        s += '1'
    else:
        s += '0'
    r = int(s, 2)
    if r > 180:
        print(n)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 14 №15856
'''
n = 4**12 + 2**32 - 17
print(bin(n)[2:].count('1'))
'''


# Тип 14 №27015
'''
n = 49**7 + 7**20 - 28
b = 7
R = []
while n > 0:
    R.append(n % b)
    n //= b
R.reverse()
print(R.count(0))
'''


# № 17768 (Уровень: Базовый)
'''
n = 4**644 + 4**322 + 16**35 - 64**3
b = 4
R = []
while n > 0:
    R.append(n % b)
    n //= b
R.reverse()
print(R.count(3))
'''

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
M = []
for x in range(2030+1):
    n = 7**91 + 7 ** 160 - x
    b = 7
    R = []
    while n > 0:
        R.append(n % b)
        n //= b
    R.reverse()
    if R.count(0) == 70:
        M.append(x)
print(max(M))
'''

# № 18169 (Уровень: Сложный)
'''
for x in range(50000, 100000):
    n = 3**2000 + 3**10 - x
    b = 3
    R = []
    while n > 0:
        R.append(n % b)
        n //= b
    if R.count(2) == 2000:
        print(x)
        break
'''


# № 17868 Демоверсия 2025 (Уровень: Базовый)
'''
alphbaet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphbaet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print((A + B) // 18)
'''
# 469034148

# Тип 14 №48389
'''
alphbaet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphbaet[:7]:
    for y in alphbaet[:7]:
        A = int(f'{y}{x}320', 7)
        B = int(f'1{x}3{y}3', 9)
        if (A + B) % 181 == 0:
            print((A + B) // 181)
'''


# № 8418 (Уровень: Средний)
'''
alphbaet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for p in range(7, 36+1):
    for x in alphbaet[:p]:
        for y in alphbaet[:p]:
            for z in alphbaet[:p]:
                if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}33', p):
                    print(int(f'{x}{y}{z}', p))
'''

'''
from string import *
alphabet = digits + ascii_uppercase
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for p in range(10, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                if int(f'5{x}83', p) + int(f'{x}9{x}9', p) == int(f'{y}20{y}', p):
                    print(int(f'{x}{y}{y}{x}', p))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ  = []
# на следующем уроке:
