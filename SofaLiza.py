# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Статград номер 8
'''
cnt = 0
from itertools import product
for p in product ('0123456789ABCDEF', repeat = 4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('D') == 1:
            if all(pair not in num for pair in '1D D1 3D D3 5D D5 7D D7 9D D9 BD DB FD DF'.split()):
                cnt += 1
print(cnt)


cnt = 0
from itertools import product
for p in product('0123456789ABCDEF', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('D') == 1:
            for x in '13579BF':
                num = num.replace(x, '*')
            if '*D' not in num and 'D*' not in num:
                cnt += 1
print(cnt)
'''


# Статград номер 9
'''
n = 0
R = []
for s in open('files/9.csv'):
    M = [int(x) for x in s.split()] 
    n += 1 
    copied4 = [x for x in M if M.count(x) == 4] 
    copied1 = [x for x in M if M.count(x) == 1] 
    if len(copied1) == 3 and len(copied4) == 4:
        if M == sorted(M, reverse=True):
            R.append(n)
print(sum(R))
'''


# Статград номер 19-21
'''
from math import ceil, floor
def F(s,n):
    if s <= 20007:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 2, n - 1), F(s - 7, n - 1), F(floor(s/3), n - 1)]
    return any(h) if (n - 1) % 2  == 0 else all(h)
print(19, [s for s in range(20007+1, 1000000) if F(s, n = 2)])
print(20, [s for s in range(20007+1, 1000000) if F(s, n = 3) and not F(s, n =1)])
print(21, [s for s in range(20007+1, 1000000) if F(s, n = 4) and not F(s, n =2)])
'''


# № 28760 Досрочная волна 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2*2187**567 + 729**566 - 2*243**565 + 81 ** 564 - 2*27**563 - 6561
n27 = convert(n, 27)
print(len([x for x in n27 if x in alp[0::2] and x > '9']))

# print(int('345', 40))
# ValueError: int() base must be >= 2 and <= 36, or 0


n = 2*2187**567 + 729**566 - 2*243**565 + 81 ** 564 - 2*27**563 - 6561
b = 27
cnt = 0
while n > 0:
    ostat = n % b

    if ostat % 2 == 0 and ostat > 9:
        cnt += 1

    n //= b
print(cnt)
'''


# № 27626 Апробация 04.03.26 (Уровень: Базовый)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

R = []
for x in range(1, 2030):
    n = 6**2030 + 6**100 - x
    n6 = convert(n, 6)
    R.append(n6.count('0'))
print(min(R))


b = 6
R = []
for x in range(1, 2030):
    n = 6**2030 + 6**100 - x
    cnt = 0
    while n > 0:
        ostat = n % b
        if ostat == 0:
            cnt += 1
        n //= b
    R.append(cnt)
print(min(R))



# № 28935 ЕГКР 18.04.26 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:23]:
    A = int(f'761{x}035', 23)
    B = int(f'338{x}932', 23)
    if (A + B) % 22 == 0:
        print((A + B) // 22)
'''




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [6, 7, 10, 11, 12, 17]
# на следующем уроке: 9 17 24 27 26


# region 📖 Пробник (Вариант 2)

# Студент #Софья
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# Студент #Лиза
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# endregion 📖 Пробник (Вариант 2)
