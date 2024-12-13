# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = '289734'
summa = sum(map(int, s))
print(map(int, s))  # <map object at 0x104e26b60>
print(list(map(int, s)))  # [2, 8, 9, 7, 3, 4]
print(summa)  # 33


print(map(str, [1, 2, 3, 4, 5]))
print(list(map(str, [1, 2, 3, 4, 5])))
# ['1', '2', '3', '4', '5']

print([int(x) for x in s])  # [2, 8, 9, 7, 3, 4]
summa = sum([int(x) for x in s])
print(summa)  # 33


s = '432897ewklo'
summa = sum([int(x) for x in s if x.isdigit()])
print(summa)  # 33
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# № 18120 (Уровень: Базовый)
'''
# Вариант 1

s = sorted('ПРЕСТОЛ')
n = 0
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if n % 2 != 0 and word[-1] in 'ЕО':
                        sogl = [x for x in word if x in 'ПРСТЛ']
                        if len(sogl) <= 3:
                            cnt += 1

print(cnt)

# Вариант 2

from itertools import *
n = 0
cnt = 0
for p in product(sorted('ПРЕСТОЛ'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 != 0 and word[-1] in 'ЕО':
        sogl = [x for x in word if x in 'ПРСТЛ']
        if len(sogl) <= 3:
            cnt += 1
print(cnt)

# Вариант 3

from itertools import *
cnt = 0
for n, p in enumerate(product(sorted('ПРЕСТОЛ'), repeat=5), 1):
    word = ''.join(p)
    if n % 2 != 0 and word[-1] in 'ЕО':
        sogl = [x for x in word if x in 'ПРСТЛ']
        if len(sogl) <= 3:
            cnt += 1
print(cnt)


for i, x in enumerate(['a', 'b', 'c', 'd', 'e'], 1):
    print(i, x)
'''


# № 18133 (Уровень: Базовый)
'''
from itertools import *
n = 0
R = []
for p in product(sorted('КОДИМ'), repeat=5):
    word = ''.join(p)
    n += 1
    if word.count('М') == 2 and 'ММ' not in word:
        print(n, word)
        R.append(n)
print(max(R))
'''

'''
from itertools import *
n = 0
for p in product(sorted('ЩЭДСР'), repeat=4):
    word = ''.join(p)
    n += 1
    if word == 'ЩДЩД':
        print(n)
    if n == 391:
        print(word)
'''


# № 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
'''
from itertools import *
R = []
for p in permutations('ПРОСТО'):
    word = ''.join(p)
    if 'ОО' not in word:
        print(word)
        R.append(word)
print(len(set(R)))
'''


# № 13251 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in permutations('КАЙФ'):
    word = ''.join(p)
    if word[-1] != 'Й' and 'КФ' not in word:
        cnt += 1
print(cnt)
'''


# № 13252 Открытый курс "Слово пацана" (Уровень: Средний)
'''
from itertools import *
R = []
for p in permutations('КИДАЛА', r=5):
    word = ''.join(p)
    if 'АА' not in word:
        R.append(word)
print(len(set(R)))
'''


# № 13870 (Уровень: Средний)
'''
from itertools import *
cnt = 0
for p in product('01234567', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if any(group in num for group in '000 111 222 333 444 555 666 777'.split()):
            if any(num.count(x) == 3 for x in num):
                if len(set(num)) == 3:
                    cnt += 1
                    print(num)
print(cnt)
'''


# № 15012 (Уровень: Базовый)
'''
from itertools import *
cnt = 0
for p in product('0123456789ABCD', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if len(set(num)) == 2:
            if num[-1] in '03':
                cnt += 1
print(cnt)
'''
# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
