# region Домашка: ******************************************************************
from pprint import pformat

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 17550 Основная волна 08.06.24 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    uncopied = [x for x in M if M.count(x) == 1]
    copied = [x for x in M if M.count(x) == 3]
    if len(copied) == 3 and len(uncopied) == 3:
        if sum(copied) ** 2 > sum(uncopied) ** 2:
            cnt += 1
print(cnt)
'''


# № 12463 (Уровень: Базовый)
'''
cnt =0
for s in open('0. files/9.csv'):
    M=[int(x) for x in s.split(',')]
    copied4 = [x for x in M if M.count(x) == 4]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied4)==4 and len(copied2) == 2 and len(uncopied)==3:
        if sum(uncopied) / 3 >= max(copied2 + copied4):
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
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 24, 26, 27
