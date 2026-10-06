
# region Домашка: ******************************************************************


# 📎  https://stepik.org/lesson/1309452/step/12?unit=1324568
#
# Дано натуральное число. Напишите программу, которая вычисляет:
# количество цифр 2 в нем;
# сколько раз в нем встречается последняя цифра;
# количество нечетных цифр;
# сумму его цифр, больших семи;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 11, если такая цифра одна, то вывести ее);
# сколько раз в нем встречаются цифры 0 и 4 (всего суммарно).
'''
from math import prod
n = int(input())
s = str(n)
print(s.count('2'))
print(s.count(s[-1]))
print(len([x for x in s if int(x) % 2 != 0]))
print(sum([int(x) for x in s if int(x) > 7]))
M = [int(x) for x in s if int(x) > 7]
if len(M) == 0:
    print(11)
elif len(M) == 1:
    print(M[0])
else:
    print(prod(M))
print(s.count('0') + s.count('4'))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
n = 10**8

print(bin(n)[2:])  # 101111101011110000100000000
print(int('101111101011110000100000000', 2))  # 10**8

print(oct(n)[2:])  # 575360400
print(int('575360400', 8))  # 10**8

print(hex(n)[2:])  # 5f5e100
print(int('5f5e100', 16))  # 10**8
'''


# Создание 36-ого алфавита
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']
print(alp[:16])  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


import string
alp = string.digits + string.ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''



# № 31511 Демоверсия 2027(Уровень: Базовый)
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:22]:
    A = int(f'27{x}98876', 22)
    B = int(f'26{x}51', 22)
    C = int(f'711{x}5', 22)
    if (A + B + C) % 21 == 0:
        RES.append((A + B + C) // 21)
print(min(RES))
'''


# № 31222 Резерв 22.06.26(Уровень: Базовый)
'''
res=[]
alp=sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM'.lower())
for x in alp[:19]:
    a=int(f'76{x}79645',19)
    b=int(f'35{x}42',19)
    c=int(f'332{x}6',19)
    if (a+b+c) % 18 ==0:
        res.append((a+b+c) // 18)
print(max(res))
'''



# № 29346 Открытый вариант 2026(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 5 * 1296 ** 2021 - 4 * 216 ** 2022 + 3 * 36 ** 2023 - 2 * 6 ** 2024 - 2025
n36 = convert(n, 36)
print(len([x for x in n36 if x in alp[0::2]]))  # количество цифр с чётным числовым значением
print(n36.count('0'))  # кол-во нулей
print(len(n) - n36.count('0'))  # кол-во не нулевых значений
print(len([x for x in n36 if x > '9']))  # Числа большие чем 9
print(len([x for x in n36 if x > alp[25]]))  # Числа большие чем 25
'''


# № 24629 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


n = 14**1402 + 28**501 - 14**51 -1400
n14 = convert(n, 14)
print(len([x for x in n14 if x == 'C']))
'''

# № 23754 Демоверсия 2026(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

res = []
for x in range(0, 3001):
    n = 9 * 11 ** 210 + 8 * 11 ** 150 - x
    n11 = convert(n, 11)
    if n11.count('0') == 60:
        res.append(x)
print(max(res))
'''

# № 22067 (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n=3 * 17**777 + 15 * 17**250 -6 * 17**100 + 2
n17= convert(n, 17)
print(len(set([x for x in n17 if int(x, 17) % 2 == 0])))
print(len(set([x for x in n17 if x in alp[0::2]])))
'''

# № 21900 Открытый вариант 2025(Уровень: Базовый)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

res = []
for x in range(1, 2301):
    n = 7 ** 350 + 7 ** 150 - x
    n7 = convert(n, 7)
    if n7.count('0') == 200:
        res.append(x)
print(max(res))




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [14]
# КЕГЭ = []
# на следующем уроке:









