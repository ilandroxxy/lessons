# region Домашка: ******************************************************************

'''
from itertools import *

R = []
num = 0
for p in product(sorted("ФЕВРАЛЬ"), repeat=6):
    slovo = "".join(p)
    num += 1
    if "А" not in slovo and "Е" not in slovo:
        R.append(num)
print(min(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 14 №26959
# Значение арифметического выражения 16**18 * 4**10 - 4**6 - 16 записали в системе счисления с основанием 4.
# Сколько цифр 3 содержится в этой записи?
'''
n = 16**18 * 4**10 - 4**6 - 16
b = 4
M = []
while n > 0:
    M.append(n % b)
    n //= b
M = M[::-1]  # M.reverse()
print(M.count(3))


n = 16**18 * 4**10 - 4**6 - 16
M = []
while n > 0:
    M = [n % 4] + M
    n //= 4
print(M.count(3))
'''

# № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
'''
n = 4*3125 ** 2019 + 3*625**2020 -2 * 125**2021  +25**2022 -4*5**2023 - 2024
M = []
while n > 0:
    M.append(n % 25)
    n //= 25
M.reverse()
print(len([x for x in M if x > 10]))
'''

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    n = 7**91 + 7**160 - x
    M = []
    while n > 0:
        M.append(n % 7)
        n //= 7
    M.reverse()
    if M.count(0) == 70:
        print(x)
'''

'''
print(int('324', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0
'''


# Тип 14 №48385
'''
from string import *
alphbaet = digits + ascii_uppercase
print(alphbaet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:13]:
    for y in alphabet[:13]:
        A = int(f'8{x}78{y}', 13)
        B = int(f'79{x}{y}7', 18)
        if (A + B) % 9 == 0:
            print((A + B) // 9)
            exit()
'''

'''
from string import *
alphbaet = digits + ascii_uppercase

for p in range(7, 36+1):
    for x in alphbaet[:p]:
        for y in alphbaet[:p]:
            for z in alphbaet[:p]:
                if int(f'{y}4{y}', p) + int(f'{y}65', p) == int(f'{x}{z}33', p):
                    print(int(x + y + z, p))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
