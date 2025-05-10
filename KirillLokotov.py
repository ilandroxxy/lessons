# region Домашка: ************************************************************

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

#
# № 21894 Открытый вариант 2025 (Уровень: Базовый)
'''
from itertools import *
cou = 0
for p in permutations('0123456789', 4):
    num = ''.join(p)
    if num[0] != '0':
        num = num.replace("0","ч").replace("2","ч").replace("4","ч").replace("6","ч").replace("8","ч")
        num = num.replace("1","н").replace("3","н").replace("5","н").replace("7","н").replace("9","н")
        print(num)
        if 'чч' not in num and 'нн' not in num:
            cou+=1
print(cou)
'''


# № 21703 ЕГКР 19.04.25 (Уровень: Базовый)
'''
from itertools import *
n = 0
for p in product(sorted('ПОБЕДА'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] == 'О':
            if len(set(word)) == 6:
                print(n)
'''



# № 20954 (Уровень: Базовый)
'''
from itertools import *
n = 0
for p in product(sorted('МАКС'), repeat=6):
    word = ''.join(p)
    n += 1
    if "С" not in word and "М" not in word and "КК" not in word:
        print(n, word)
'''


# ПАРИЖАНКА
# ПАРИЖАНКА
# ПАРИЖАНКА
# ПАРИЖАНКА
# ПАРИЖАНКА
# ПАРИЖАНКА

# № 19480 (Уровень: Средний)
'''
from itertools import *
cou = []
for p in permutations('ПАРИЖАНКА'):
    word = ''.join(p)
    if word == 'ПАРИЖАНКА':
        print(word)
    slovo = word
    slovo = slovo.replace('И', 'А')
    if 'ААА' not in slovo and slovo.count('АА') == 1:
        cou.append(word)
print(len(set(cou)))
'''



# № 18973 (Уровень: Средний)
'''
from itertools import *
cnt = 0
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in product(alp[:25], repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        chet = [x for x in num if x in alp[0:25:2]]
        if len(chet) >= 1:
            A = [x for x in num if x > 'F']
            if len(A) > 2:
                cnt += 1
print(cnt)
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: {24, 26, 27}
