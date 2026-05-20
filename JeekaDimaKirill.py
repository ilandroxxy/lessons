# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# максимальное количество идущих подряд символов,
# среди которых пара символов BC встречается ровно 3 раза.
'''
s = 'xxxxBCxxxxBCxxxxxBCxxxxBCxxxxxxxxxxBCxxxxxBCxxxxxx'
# ['xxxx', 'xxxx', 'xxxxx', 'xxxx', 'xxxxxxxxxx', 'xxxxx', 'xxxxxx']
s = s.split('BC')
R = []
for i in range(len(s)-3):
    r = 'C' + 'BC'.join(s[i:i+4]) + 'B'
    R.append(len(r))
print(max(R))
'''

# минимальное количество идущих подряд символов,
# среди которых пара символов BC встречается ровно 3 раза.
'''
s = 'xxxxBCxxxxBCxxxxxBCxxxxBCxxxxxxxxxxBCxxxxxBCxxxxxx'
s = s.split('BC')
R = []
for i in range(len(s) - 1):
    r = 'BC' + 'BC'.join(s[i:i+2]) + 'BC'
    R.append(len(r))
print(max(R))
'''


# № 27634 Апробация 04.03.26 (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
s = s.split('Z')
mini = 10 ** 10
for i in range(len(s)-268):
    r = 'Z' + 'Z'.join(s[i:i + 269]) + 'Z'
    mini = min(mini, len(r))
print(mini)
'''


# № 28943 ЕГКР 18.04.26 (Уровень: Базовый)
'''
s = open('24_28943.txt').readline()
for x in 'AEYUIO':
    s = s.replace(x, '-')
mini = 10 ** 10
r = ''
for i in range(len(s)):
    r += s[i]
    if r.count('-') == 1 and r[-1] == '-':
        while r.count('20') >= 26:
            if r.count('20') == 26:
                mini = min(mini, len(r))
            r = r[1:]
        r = ''
print(mini)#Answer: 58
'''

'''
s = open('files/24.txt').readline()
for x in 'AEIOUY':
    s = s.replace(x, 'A')
s = s.split('20')
mini = 10**10
for i in range(len(s)-24):
    r = '20' + '20'.join(s[i:i+25]) + '20'
    if r.count('A') == 1 and r[-3] == 'A':
        mini = min(mini, len(r))
print(mini)


from re import *
s = open("files/24.txt").readline().replace("20", "##")
pat = "(((##)[0123456789BCDFGHJKLMNPQRSTVWXY]*){26}[AEIOUY])"
M = [x.group(1) for x in finditer(pat, s)]
print(min([len(x) for x in M]))
'''




# endregion Урок: *************************************************************
#
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке: 4, 22, 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Женя
# Дата: #Четверг #26Февраля2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17, 27
# ❔ Без ответа: 22, 24, 26
# Итог: 23/29 первичных балла ~ 85 вторичных

# Студент #Кирилл
# Дата: #Четверг #26Февраля2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 23
# ⛔️ Неверно: 17, 18, 22, 24, 25, 26, 27
# ❔ Без ответа: Нет
# Итог: 20/29 первичных балла ~ 78 вторичных

# Студент #Дима
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 15, 16, 19, 20, 21, 23
# ⛔️ Неверно:
# ❔ Без ответа: 8, 9, 14, 17, 18, 22, 24, 25, 26, 27
# Итог: 17/29 первичных балла ~ 70 вторичных

# endregion 📖 Пробник (Вариант 2)

