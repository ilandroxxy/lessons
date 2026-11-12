# region Домашка: ******************************************************************


# https://stepik.org/lesson/2354753/step/4?unit=2390077
'''
alp = sorted('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
def convert(n,b):
    r = ''
    while n> 0:
        r = alp[n % b]+r
        n //=b
    return r


n = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
n36 = convert(n, 36)

print(len([x for x in n36 if int(x, 36) % 2 == 0]))
print(len([x for x in n36 if x in alp[0::2]]))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 22419 (Уровень: Базовый)
# (Л. Шастин) Сколько существует тринадцатеричных семизначных чисел,
# в которых все цифры различны и никакая нечётная цифра не стоит
# рядом с цифрой B?
'''
cnt = 0
from itertools import permutations
alp = sorted('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
for p in permutations(alp[:13], r=7):

    num = ''.join(p)
    print(num, p)
    if num[0] != '0':
        for x in '13579':
            num = num.replace(x, '*')
        if '*B' not in num and 'B*' not in num:
            cnt += 1
print(cnt)
'''


# № 21975 (Уровень: Базовый)
# (Л. Шастин) Сколько существует шестизначных чисел,
# записанных в семнадцатеричной системе счисления,
# в которых все цифры различны и никакие три чётные
# или три нечётные цифры не стоят рядом?
'''
cnt = 0
from itertools import permutations
alp = sorted('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
for p in permutations(alp[:17], r=6):
    num = ''.join(p)
    if num[0] != '0':
        for x in alp[0::2]:
            num = num.replace(x, '2')
        for x in alp[1::2]:
            num = num.replace(x, '1')
        if '222' not in num and '111' not in num:
            cnt += 1
print(cnt)
'''


# № 20898 Апробация 05.03.25(Уровень: Базовый)
# Определите количество девятеричных пятизначных чисел,
# в записи которых ровно одна цифра 0, при этом никакая
# нечётная цифра не стоит рядом с цифрой 0.
'''
cnt = 0
from itertools import product
alp = sorted('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
for p in product(alp[:9], repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 1:
            for x in alp[1::2]:
                num = num.replace(x, '1')
            if '10' not in num and '01' not in num:
                cnt += 1
print(cnt)
'''


# № 18260 (Уровень: Базовый)
# (Л. Шастин) Определите количество 12-ричных шестизначных
# чисел, в записи которых содержится ровно одна цифра «B»
# и равное количество чётных и нечётных цифр.

cnt = 0
from itertools import product
alp = sorted('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
for p in product(alp[:12], repeat=6):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('B') == 1:
            chet = [x for x in num if x in alp[0::2]]
            nechet = [x for x in num if x in alp[1::2]]
            if len(chet) == len(nechet):
                cnt += 1
print(cnt)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 13, 14, 15, 16, 18, 19-21, 22]
# КЕГЭ = []
# todo на следующем уроке:
