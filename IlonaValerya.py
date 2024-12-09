# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://stepik.org/lesson/1038667/step/3?unit=1062772

'''
print('ОА АО ЯО ОЯ АЯ ЯА'.split())
# ['ОА', 'АО', 'ЯО', 'ОЯ', 'АЯ', 'ЯА']
for x in ['ОА', 'АО', 'ЯО', 'ОЯ', 'АЯ', 'ЯА']
all(p not in word for p in ['ОА', 'АО', 'ЯО', 'ОЯ', 'АЯ', 'ЯА'])
all(p not in word for p in 'ОА АО ЯО ОЯ АЯ ЯА'.split())
'''

'''
s = 'ЯРОСЛАВ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    if len(word) == len(set(word)):  # буквы в коде не должны повторяться
                        sogl = [x for x in word if x in 'РСЛВ']
                        glas = [x for x in word if x in 'ЯОА']
                        if len(sogl) > len(glas):  # согласных в коде должно быть больше, чем гласных
                            if all(p not in word for p in 'ОА АО ЯО ОЯ АЯ ЯА'.split()):  # две гласные буквы нельзя ставить рядом
                                cnt += 1
print(cnt)
'''


# https://stepik.org/lesson/1038667/step/7?unit=1062772
'''
s = sorted('ПЯТЬДНЕЙ')
R = []
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                n += 1
                if all(p not in word for p in 'ЯЕ'):
                    if len(word) == len(set(word)):
                        R.append(n)
print(max(R))
'''

# https://stepik.org/lesson/1038667/step/5?unit=1062772

s = '0123456789ABCDE'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for e in s:
                for d in s:
                    num = a + b + c + d + e
                    if num[0] != '0' and num.count('8') == 1:
                        N = [x for x in num if x > '9']
                        if len(N) >= 2:
                            cnt += 1
print(cnt)





# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
