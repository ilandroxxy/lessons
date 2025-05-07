# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
from itertools import *
cnt = 0
for p in permutations('ЯРОСЛАВ', r=5):
    word = ''.join(p)
    sogl = [x for x in word if x in 'РСЛВ']
    glas = [x for x in word if x in 'ЯОА']

    if len(sogl) > len(glas):
        if all(x not in word for x in 'ЯА АЯ АО ОА ОЯ ЯО'.split()):
            cnt += 1

print(cnt)
'''


from itertools import *
M = []
n = 0
for p in product(sorted('МАРКСЛ'), repeat = 6):
    word = ''.join(p)
    n += 1
    if 'КС' not in word and 'СК' not in word:
        copied = [x for x in word if word.count(x) == 3]
        not_copied = [x for x in word if word.count(x) == 1]
        if len(copied) == 3 and len(not_copied) == 3:
            M.append(n)

print(max(M))



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 8.1, 12]
# КЕГЭ  = []
# на следующем уроке:
