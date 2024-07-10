# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 14 №15632
'''
print(bin(4**14+2**32-4)[2:].count('1'))

print(f'{4**14 + 2**32 - 4:b}'.count('1'))

x = 4**14 + 2**32 - 4
s = ''
while x > 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))

x = 4**14 + 2**32 - 4
L = []
while x > 0:
    L.append(x % 2)
    x //= 2
L.reverse()
print(L.count(1))
'''
# Ответ: 27


# Определите в 25-ричной записи числа количество цифр 0
'''
x = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4*5**2023 - 2024
base = 25
s = ''
while x > 0:
    s += str(x % base)
    x //= base
s = s[::-1]
print(s.count("0"))
print(s[:10])

x = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4*5**2023 - 2024
base = 25
L = []
while x > 0:
    L.append(x % base)
    x //= base
L.reverse()
print(L.count(0))
print(L[:10])
'''

# # № 16380 ЕГКР 27.04.24 (Уровень: Базовый)
# Определите в 25-ричной записи числа количество цифр с числовым значением, превышающим 10:
'''
x = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 + 25**2022 - 4*5**2023 - 2024
base = 25
L = []
while x > 0:
    L.append(x % base)
    x //= base
L.reverse()

# cnt = 0
# for elem in L:
#     if elem > 10:
#         cnt += 1
# print(cnt)

print(len([elem for elem in L if elem > 10]))
'''


# Тип 14 №33186
'''
x = 343**5 -7**9 + 48
base = 7
L = []
while x > 0:
    L.append(x % base)
    x //= base
L.reverse()
print(L.count(6))
'''

# № 17527 Основная волна 07.06.24 (Уровень: Базовый)
'''
R = []
for x in range(2030+1):
    n = 3**100 - x
    base = 3
    L = []
    while n > 0:
        L.append(n % base)
        n //= base
    L.reverse()
    if L.count(0) == 5:
        R.append(x)
print(max(R))
'''


# № 17633 Основная волна 19.06.24 (Уровень: Базовый)
'''
for x in range(2030+1):
    n = 6**260 + 6**160 + 6**60 - x
    base = 6
    L = []
    while n > 0:
        L.append(n % base)
        n //= base
    L.reverse()
    if L.count(0) == 202:
        print(x)
        break
'''
# Ответ: 216


# Тип 14 №55810
'''
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:15]:
    A = int(f'97968{x}13', 15)
    B = int(f'7{x}213', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
'''

# Тип 14 №48392
'''
from string import *
alphabet = digits + ascii_uppercase
print(alphabet)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:9]:
    for y in alphabet[:9]:
        A = int(f'2{y}66{x}', 9)
        B = int(f'{x}0{y}1', 12)
        if (A + B) % 170 == 0:
            print((A + B) // 170)
'''

# Тип 14 №64899
alphabet = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(9, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            for z in alphabet[:p]:
                for w in alphabet[:p]:
                    if int(z+x+y+x+'4', p) + int(f'{x}{y}658', p) == int(f'{w}{z}{x}73', p):
                        print(int(x+y+z+w, p))

print(f'{7*512**120-6*64**100+8**210-255:o}'.count('0'))

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
