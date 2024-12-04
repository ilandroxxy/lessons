# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038682/step/3?unit=1062773
'''
s = '1' + '0' * 55
while '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    else:
        s = s.replace('1', '00', 1)
print(s.count('0'))
'''


# https://stepik.org/lesson/1038682/step/4?unit=1062773
'''
for n in range(301, 1000):
    s = '5' * n
'''


# https://stepik.org/lesson/1038682/step/12?unit=1062773
'''
s = '3' * 70
while '333' in s or '77777' in s:
    if '333' in s:
        s = s.replace('333', '77', 1)
    else:
        s = s.replace('77777', '7', 1)
print(sum(map(int, s)))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 8 https://education.yandex.ru/ege/task/d9fba00a-a921-4c70-9597-0b458fbf17f0

# Вариант 1
'''
s = sorted('ФАВОРИТ')
cnt = 0
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            word = a + b + c + d + e + f + g
                            num += 1
                            if num % 2 != 0:
                                if 'ТРИО' in word:
                                    if word[:4] != 'ТРИО' and word[-4:] != 'ТРИО':
                                        cnt += 1
print(cnt)
'''


# Задание 8 https://education.yandex.ru/ege/task/86d21473-bf55-4b4d-99d9-d620244843ad

s = sorted('АВТОБУС')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    word = a + b + c + d + e
                    n += 1
                    if 'А' not in word and 'О' not in word:
                        if len(word) == len(set(word)):
                            if word[-2:] == 'СБ':
                                print(n, word)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
