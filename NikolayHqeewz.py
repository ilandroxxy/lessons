# region Домашка: ******************************************************************

# № 3901 (Уровень: Базовый) 🌶
'''
for x in range(700000+1,700100):
    print(x, x % 13)
    # 700009 11
    # 700010 12
    # 700011 0
    # 700012 1
    # 700013 2
'''


'''
from fnmatch import *
cnt = 0
for x in range(700011, 10**10, 13):
    if (not fnmatch(str(x), '*0??3*')) and (not fnmatch(str(x), '*4??2')) and (not fnmatch(str(x), '*1*')):
        print(x, sum(map(int, str(x))))
        cnt += 1
        if cnt == 5:
            break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
