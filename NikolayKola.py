# region Домашка: ******************************************************************

# КЕГЭ № 6985 (Уровень: Средний)
'''
s = sorted('марксл')
cnt = 0
r = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        w = a + b + c + d + e + f
                        cnt += 1
                        if (len(set(w)) == 4 and any(w.count(i) == 3 for i in w)):
                            if 'кс' not in w and 'ск' not in w:
                                r.append(cnt)
print(max(r))
'''

# КЕГЭ № 4320 (Уровень: Средний)
'''
s = sorted('01234567')
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        n = a + b + c + d + e + f
                        if a != '0':
                            if len(set(n)) == 6:
                                if '02' not in n and '20' not in n and '24' not in n and '42' not in n and '46' not in n and '64' not in n and '06' not in n and '60' not in n and '04' not in n and '40' not in n and '26' not in n and '62' not in n:
                                    if '13' not in n and '31' not in n and '15' not in n and '51' not in n and '17' not in n and '71' not in n and '35' not in n and '37' not in n and '57' not in n and '75' not in n and '73' not in n and '53' not in n:
                                        if int(n, 8) % 5 == 0:
                                            cnt += 1
print(cnt)


s = sorted('01234567')
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        n = a + b + c + d + e + f
                        if a != '0':
                            if len(set(n)) == 6:
                                if int(n, 8) % 5 == 0:
                                    n = n.replace('0', '2').replace('4', '2').replace('6', '2')
                                    n = n.replace('3', '1').replace('5', '1').replace('7', '1')
                                    if '11' not in n and '22' not in n:
                                        cnt += 1
print(cnt)
'''

'''
s = sorted('соточка')
cnt = set()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            w = a + b + c + d + e + f + g
                            if 'оо' in w or 'оа' in w or 'ао' in w:
                                if w.count('с') == 1:
                                    if w.count('о') == 2:
                                        if w.count('т') == 1:
                                            if w.count('ч') == 1:
                                                if w.count('к') == 1:
                                                    if w.count('а') == 1:
                                                        cnt.add(w)
print(len(cnt))

from itertools import *
cnt = set()
for per in permutations('СОТОЧКА'):
    w = ''.join(per)
    if 'ОО' in w or 'ОА' in w or 'АО' in w:
        cnt.add(w)
print(len(cnt))
'''
'''
s = sorted('барш')
cnt = 0
r = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    w = a + b + c + d + e
                    cnt += 1
                    sogl = [i for i in w if i in 'брш']
                    if len(set(w)) == 4 and any(w.count(i) == 2 for i in w):
                        if len(sogl) <= 3:
                            print(w)
                            r.append(cnt)
print(max(r))
'''
'''
s=sorted('амфбрхий')
cnt=0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for a1 in s:
                        for b1 in s:
                            for c1 in s:
                                for d1 in s:
                                    for e1 in s:
                                        w=a+b+c+d+e+a1+b1+c1+d1+e1
                                        if w.count('а') == 2:
                                            if w.count('м') == 1:
                                                if w.count('ф') == 1:
                                                    if w.count('и') == 2:
                                                        if w.count('б') == 1:
                                                            if w.count('р') == 1:
                                                                if w.count('х') == 1:
                                                                    if w.count('й') == 1:
                                                                        if w.count('иифаа') == 1 or w.count('аафии') == 1:
                                                                                print(w)
                                                                                cnt += 1

print(cnt)
'''
'''
from itertools import permutations
k = set()
for w in permutations('АМФИБРАХИЙ'):
    slovo = ''.join(w)
    if 'ИИФАА' in slovo or 'ААФИИ' in slovo:
        k.add(slovo)
print(len(k))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

R = []
for x in range(0, 2030+1):
    n = 6 ** 2030 + 6**100 - x
    M = []
    while n > 0:
        M.append(n % 6)
        n //= 6
    R.append(M.count(0))
print(max(R))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2*+, 3, 4+, 6+, 7, 9*+, 10+, 11, 18+, 19-21, 22+]
# КЕГЭ  = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23]
# на следующем уроке:
