# region Домашка: ******************************************************************

'''
from itertools import *
num = 0
R = []
for p in product(sorted('МАРКСЛ'), repeat=6):
    s = ''.join(p)
    num += 1
    if 'КС' not in s and 'СК' not in s:
        if len(set(s)) == 4 and any(s.count(x) == 3 for x in s):
            R.append(num)
print(max(R))
'''
# 46605


'''
from itertools import *
cnt = 0
for p in permutations('ЯРОСЛАВ', 5):
    s = ''.join(p)
    sogl = [x for x in s if x in 'РСЛВ']
    glas = [x for x in s if x in 'ЯОА']
    if len(sogl) > len(glas):
        s = s.replace('Я', 'А').replace('О', 'А')
        if 'АА' not in s:
            cnt += 1
print(cnt)
'''

'''
from itertools import *
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
cnt = 0
print(alphabet[:15])
for p in product(alphabet[:15], repeat=5):
    n = ''.join(p)
    if n[0] != '0':
        if n.count('8') == 1:
            if len([x for x in n if int(x, 15) > 9]) >= 2:
                cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in range(2):
            for w in [0, 1]:
                F = (x or (not z)) and (x == (not w)) and (x <= y)
                if F == 1:
                    print(x, y, z, w)
'''

# Тип 2 №18578
# Логическая функция F задаётся выражением ((x ∧ ¬y) ∨ (w → z)) ≡ (z ≡ x).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x and (not y)) or (w <= z)) == (z == x)
                if F == 1:
                    print(x, y, z, w)
'''

# Тип 2 №56502
# Логическая функция F задаётся выражением:
# ((x→y)∨(z→w))∧((z≡y)→(w≡x)).
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) or (z <= w)) and ((z == y) <= (w == x))
                if F == 0:
                    print(x, y, z, w)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
