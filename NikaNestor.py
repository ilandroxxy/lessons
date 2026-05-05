# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 16333 Открытый вариант 2024 (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
for x in 'QRW':
    s = s.replace(x, 'a')
for x in '124':
    s = s.replace(x, 'b')
while 'aa' in s or 'bb' in s:
    s = s.replace('aa', 'a a').replace('bb', 'b b')
print(max([len(x) for x in s.split()]))

s = open('files/24.txt').readline()
s = s.replace('Q', 'a').replace('R', 'a').replace('W', 'a')
s = s.replace('1', 'b').replace('2', 'b').replace('4', 'b')
while 'aa' in s or 'bb' in s:
    s = s.replace('aa', 'a a').replace('bb', 'b b')
s = s.split()
m = [len(x) for x in s]
print(max(m))
'''



# № 15339 Досрочная волна 2024 (Уровень: Средний)
'''
s = open('files/24.txt').readline()
for x in 'ABC':
    s = s.replace(x, '*')
for x in '6789':
    s = s.replace(x, '+')

while '**' in s or '++' in s:
    s = s.replace('**', '* *').replace('++', '+ +')
print(max([len(x) for x in s.split()]))
'''


# № 2942 Апробация 19.02.2022 (Уровень: Базовый)
'''
from re import *
s = open('files/24.txt').readline()
pat = '((AB)|(AC))+'
# pat = '[(AC)|(AB)]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]) / 2)
'''

'''
s = open('files/24.txt').readline()
s = s.replace('AB', '*').replace('AC', '*')
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i:i+2] in ('AB', 'BA', 'AC', 'CA'):
        if cnt == 1:
            if s[i:i+2] in ('BA', 'CA'):
                continue
        cnt += 1
        maxi = max(cnt, maxi)
    else:
        cnt = 1
print(maxi / 2)
'''


# № 1302 Открытый вариант КЕГЭ (Уровень: Базовый)
'''
s = open('files/24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')
print(max([len(x) for x in s.split()]))


s = open('files/24.txt').readline()
cnt = 3
maxi = 0
for i in range(len(s)-3):
    if s[i:i+4] == 'XZZY':
        cnt = 3
    else:
        cnt += 1
        maxi = max(cnt, maxi)
print(maxi)
'''

# максимальное количество идущих подряд символов,
# среди которых пара символов BC встречается ровно 3 раза.

s = 'xxxxBCxxxxBCxxxxxBCxxxxBCxxxxxxxxxxBCxxxxxBCxxxxxx'
# ['xxxx', 'xxxx', 'xxxxx', 'xxxx', 'xxxxxxxxxx', 'xxxxx', 'xxxxxx']
s = s.split('BC')
R = []
for i in range(len(s)-3):
    r = 'C' + 'BC'.join(s[i:i+4]) + 'B'
    R.append(len(r))
print(max(R))

# минимальное количество идущих подряд символов,
# среди которых пара символов BC встречается ровно 3 раза.

s = 'xxxxBCxxxxBCxxxxxBCxxxxBCxxxxxxxxxxBCxxxxxBCxxxxxx'
s = s.split('BC')
R = []
for i in range(len(s) - 1):
    r = 'BC' + 'BC'.join(s[i:i+2]) + 'BC'
    R.append(len(r))
print(max(R))


# Пара содержится ровное кол-во раз

s = open('files/24.txt').readline()
s = s.split('BC')
maxi = 0
for i in range(len(s)-190):
    r = 'C' + 'BC'.join(s[i:i+191]) + 'B'
    maxi = max(maxi, len(r))
print(maxi)




# № 28710 (Уровень: Базовый)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [23]
# на следующем уроке:



# region Пробник 2

# Вероника
# Пробник №2
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17,
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных


# Нестор
# Пробник №2
# Дата: #Воскресенье #01Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17
# ❔ Без ответа: 22, 24, 26, 27
#
# Итог: 22/29 первичных балла ~ 83 вторичных

# endregion Пробник 2
