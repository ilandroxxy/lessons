# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
a = [3, 3, 3, 3]
e = [5, 5]
print(a + e)  # [3, 3, 3, 3, 5, 5]
print(max(a + e))  # 5


# todo Почему не срабатывает условие 25 строка
k = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    a = [x for x in M if M.count(x) == 4]
    e = [x for x in M if M.count(x) == 2]
    n = [x for x in M if M.count(x) == 1]
    if len(a) == 4 and len(e) == 2 and len(n) == 3:
        if sum(n)/3 >= max(a + e):
        # if (sum(n)/3 >= max(M)) and (max(M) in (a + e)):  #
            k += 1
print(k)
'''
from os import confstr_names

# print('*'.join(['a', 'b', 'c']))  # a*b*c

'''
cnt = 0
from itertools import *  # * - это подключение всего содержимого
# from itertools import product

for p in product(sorted('КОДИМ'), repeat=5):
    word = ''.join(p)
    cnt += 1
print(cnt)  # 3125
'''


# № 18133 (Уровень: Базовый)
'''
from itertools import *
n = 0
for p in product(sorted('КОДИМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('М') == 2 and 'ММ' not in word:
        print(n)
'''

'''
print(all(x % 2 == 0 for x in [2, 4, 6, 8]))  #  True
print(all(x % 2 == 0 for x in [2, 4, 7, 8]))  #  False
print(any(x % 2 == 0 for x in [2, 3, 7, 9]))  #  True
'''


# № 8417 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in permutations('ЯРОСЛАВ', r=5):
    word = ''.join(p)
    sogl = [x for x in word if x in 'РСЛВ']
    glas = [x for x in word if x in 'ЯОА']
    if len(sogl) > len(glas):  # согласных в коде должно быть больше, чем гласных
        # if all(x not in word for x in 'ЯО ОЯ ОА АО ЯА АЯ'.split()): # две гласные буквы нельзя ставить рядом
        word = word.replace('О', 'Я').replace('Я', 'А')
        if 'АА' not in word:
            cnt += 1
print(cnt)
'''


# № 18120 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
n = 0
for p in product(sorted('ПРЕСТОЛ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 != 0:
        if word[-1] in 'ЕО':  # оканчиваются на гласную букву
        # if word[-1] not in 'ПРСТЛ':  # оканчиваются на гласную букву
            sogl = [x for x in word if x in 'ПРСТЛ']
            if len(sogl) <= 3:
                cnt += 1
print(cnt)
'''

# № 17862 Демоверсия 2025 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('7') == 1:
            D = [x for x in num if x > '8']  # 9 A B
            if len(D) <= 3:
                cnt += 1
print(cnt)
'''


# № 17695 (Уровень: Средний)
'''
from itertools import *
cnt = 0
for p in product('0123456', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        # if num.count('3') + num.count('4') + num.count('5') == 2:
        # if len([x for x in num if '3' <= x <= '5']) == 2:
        if len([x for x in num if x in '345']) == 2:
            # if all(x not in num for x in '00 11 22 33 44 55 66'.split()):
            if all(num[i] != num[i+1] for i in range(len(num)-1)):
                cnt += 1
print(cnt)
'''

'''
M = [int(x) for x in open('0. files/17.txt')]
print(M)
R = []
for i in range(len(M)-2):
    # x, y, z = M[i], M[i+1], M[i+2]
    x, y, z = M[i:i+3]
    print(f'{x}, {y}, {z}')
'''


# № 20855 (Уровень: Средний)
'''
from itertools import *
n = -1
cnt = 0
for p in product('0123456789ABC', repeat=3):
    num = ''.join(p)
    if num[0] != '0':
        n += 1
        if n % 10 == 7:
            for x in '0123456789ABC'[1::2]:
                num = num.replace(x, '1')
            if '11' not in num:
                cnt += 1
print(cnt)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ = []
# на следующем уроке: 19-21 код, 22, 24.1 повторять

# Второй пробник 28.02.25:
# Дарья 10/29 -> 51 вторичных баллов +[1, 2, 4, 7, 10, 11, 13, 15, 16, 18] -[3, 6, 12, 22]

