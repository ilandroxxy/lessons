# region Домашка: ************************************************************


# № 8602 (Уровень: Базовый)
'''
s = sorted('АЕКНС')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        n += 1
                        if slovo == 'СЕНЕКА':
                            print(n)

'''


# set() - создает множество и убирает копии элементов
# № 8417 (Уровень: Базовый)
'''
s = sorted('ЯРОСЛАВ')
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):  # буквы в коде не должны повторяться
                        sogl = [x for x in slovo if x in 'РСЛВ']
                        glas = [x for x in slovo if x in 'ЯОА']
                        if len(sogl) > len(glas):  # согласных в коде должно быть больше, чем гласных
                            slovo = slovo.replace('О', 'А').replace('Я', 'А')
                            if 'АА' not in slovo:
                                cnt += 1
print(cnt)
'''

'''
s = sorted('МАРКСЛ')
R = []
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        n += 1
                        if 'КС' not in slovo and 'СК' not in slovo:
                            copied = [x for x in slovo if slovo.count(x) == 3]
                            not_copied = [x for x in slovo if slovo.count(x) == 1]
                            if len(copied) == 3 and len(not_copied) == 3:
                                R.append(n)
print(max(R))
'''

'''
s = sorted('СОТОЧКА')
n = set()
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            slovo = a + b + c + d + e + f + g
                            if len(set(slovo)) == 6:
                                if slovo.count('О') == 2:
                                    if 'ОО' in slovo or 'АО' in slovo or 'ОА' in slovo:

                                        n.add(slovo)
print(len(n))
'''


# endregion Домашка: *********************************************************
#
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ = []
# на следующем уроке:
