# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import *
n = 0
for p in product(sorted('ОМЮТ'), repeat=5):
    slovo = ''.join(p)
    n += 1
    if slovo[0] == 'О':
        print(n)
'''  # 512


'''
from itertools import *
cnt = 0
for p in product('КОМПЕГЭ', repeat=6):
    slovo = ''.join(p)
    if slovo[0] in 'ОЕЭ' and slovo[-1] in 'ОЕЭ':
        glas = [x for x in slovo if x in 'ОЕЭ']
        if len(glas) == 2:
            print(slovo)
            cnt += 1
print(cnt)  # 2304
'''

'''
from itertools import *
cnt = 0
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('6') == 1:
            num = num.replace('3', '1').replace('5', '1').replace('7', '1')
            if '16' not in num and '61' not in num:
                cnt += 1
print(cnt)  # 2961
'''

'''
n = 49**13 + 7**33 - 49
M = []
while n > 0:
    M.append(n % 7)
    n //= 7
M = M[::-1]
print(M.count(6))
'''
# 24


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print((A + B) // 18)
'''
# 469034148 (наибольшее)


'''
M = []
for n in range(1, 10000):
    s = bin(n)[2:]

    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 108:
        M.append(r)
print(min(M))  # 114
'''

'''
def convert(n, b):
    r = []
    while n > 0:
        r.append(n % b)
        n //= b
    return r[::-1]


R = []
for x in range(1000, 10000):
    if x % 3 != 0 and x % 17 != 0 and x % 19 != 0:
        if len(convert(x, 4)) == 6:
            R.append(x)

print(min(R), max(R))
'''
# 1024 4094

'''
i = 12
k = 1024 * 768
bit = k * i
pack = bit * 256
print(pack / 2**23)
'''
# 288

'''
# bit = a * b * c * t
a = 2
b = 48000
c = 24
# t = ?
bit = 288 * 2**23
t = bit / (a * b * c)
print(t / 60)  # 17.47626
'''

symbols = 15
alphabet = 26 + 10  # 36
# alphabet = 2 ** i
i = 6  # бит на символ
bit = symbols * i
print(bit / 8)  # 11.25
byte = 12   # вес пароля

V = 255 / 17
print(V - byte)
print(3 * 8)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке: устанавливаем Pycharm


# Первый пробник 21.12.24:
# Роман 2/5 -> 14 вторичных баллов +[2, 12] -[5, 6, 8]
