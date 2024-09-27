# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from fnmatch import fnmatch
# 0 + 237 + 237 + 237 + 237
for x in range(0, 10**8, 237):
    if fnmatch(str(x), '81?2*80'):
        if not fnmatch(str(x), '*9*'):
            print(x, x//237)
'''


# № 7897 (Уровень: Базовый) 🌶
'''
from fnmatch import *
R = []
for x in range(0, 10**10, 11071):
    if fnmatch(str(x), '?136*1'):
        if str(x)[0] in '13579':
            if str(x)[-2] in '02468':
                R.append(x)

print(R[-5], R[-5] // 11071)
print(R[-4], R[-4] // 11071)
print(R[-3], R[-3] // 11071)
print(R[-2], R[-2] // 11071)
print(R[-1], R[-1] // 11071)
'''


# № 3901 (Уровень: Базовый) 🌶
'''
from fnmatch import *
cnt = 0
# 700011 % 13 == 0
for x in range(700011, 10**8, 13):
    if (not fnmatch(str(x), '*0??3*')) and (not fnmatch(str(x), '*4??2')) and (not fnmatch(str(x), '*1*')):
        print(x, sum([int(i) for i in str(x) if i.isdigit()]))
        cnt += 1
        if cnt == 5:
            break
'''


# Тип 25 №27854
'''
def Divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(110203, 110245+1):
    chet = [j for j in Divisors(x) if j % 2 == 0]
    if len(chet) == 4:
        print(*chet)
'''


# Тип 25 №35483
'''
def Divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            if j % 2 != 0:
                div += [j]
            if (x // j) % 2 != 0:
                div += [x // j]
        if len(div) > 5:
            return div
    return sorted(set(div))


for x in range(35000000, 40000000+1):
    if len(Divisors(x)) == 5:
        print(x)
'''

'''
def Divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(800000+1, 10**10):
    d = Divisors(x)
    if len(d) >= 2:
        M = d[0] + d[-1]
        if M % 10 == 4:
            print(x, M)
            cnt += 1
            if cnt == 5:
                break
'''

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
