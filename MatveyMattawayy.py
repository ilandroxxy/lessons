# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Найти номер слова
# № 17549 Основная волна 08.06.24 (Уровень: Базовый)
'''
s = sorted('ФОКУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    num += 1
                    if 'Ф' not in word and word.count('У') == 2:
                        print(num, word)
'''

'''
s = sorted('ПАРУС')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    num += 1
                    if word.count('У') <= 1 and word.count('АА') == 0:
                        print(num, word)
'''

'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0' and a not in '1357':
                        if e not in '26' and num.count('7') <= 2:
                            cnt += 1
print(cnt)
'''
'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            num = a + b + c + d + e + f + g
                            if a != '0':
                                chet = [x for x in num if x in '0246']
                                if len(chet) == 2:
                                    cnt += 1
print(cnt)
'''

# № 12240 ЕГКР 16.12.23 (Уровень: Базовый)
'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if a != '0' and num.count('5') == 1:
                        if a != b and b != c and c != d and d != e:
                            cnt += 1
print(cnt)
'''

'''
s = '0123456'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        num = a + b + c + d + e + f
                        if a != '0' and int(f) >= 4:
                            chet = [x for x in num if x in '0246']
                            nechet = [x for x in num if x in '135']
                            if len(chet) == len(nechet):
                                cnt += 1
print(cnt)
'''

# № 17550 Основная волна 08.06.24 (Уровень: Базовый)
'''
cnt = 0
for s in open('9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(not_copied) == 3:
        if sum(copied) ** 2 > sum(not_copied) ** 2:
            print(M, copied, not_copied)
            cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    print(M)
    if max(M) < (sum(M) - max(M)):
        if len(set(M)) == 3:  # set([25, 30, 63, 25]) = {25, 30, 63}
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
# ФИПИ = [1+, 2+, 3, 4, 5*, 6, 7, 8*, 10+, 12*+, 14*, 16, 18, 19-21+]
# КЕГЭ  = [8, 9, 5, 12, 13, 14, 15, 16, 23]
# на следующем уроке: 9, 11, 25
