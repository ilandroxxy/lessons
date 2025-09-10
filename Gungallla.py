# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Способ открытия файла для 9 номера
'''
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
'''

# № 23555 Пересдача 03.07.25 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3  and len(copied2) == 2 and len(copied1) == 2:
        if max(copied3 + copied2) > max(copied1):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/c255edb8-3ff7-4c2a-bf66-03487b499649
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) >= 3:
        if len(set(M)) == 5:
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/5c54e314-516a-44fb-b41f-b06ffe3345af
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
        if max(M) < sum(M) - max(M):
            if sum(M) % 2 == 0:
                cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe



# https://education.yandex.ru/ege/task/d73c5edf-63bd-47d8-87cb-7810e03725a0
#
#
# https://education.yandex.ru/ege/task/ebbc8b9f-d709-47ff-b8f4-2c2e99ccb13b
#
#
# https://education.yandex.ru/ege/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
