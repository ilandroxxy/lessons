# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
R = []
for n in range(11, 1000):
    s = f'{n:b}'
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = f'{x:b}' + s
    r = int(s, 2)
    if r > 512:
        R.append(n)
print(min(R))
'''


R = []
for x in range(1, 1000):
    s = f'{x:b}'
    if x % 3 == 0:
        s = s + s[-3:]
    else:
        x = (x % 3) * 3
        s = s + f'{x:b}'
    r = int(s, 2)
    if r > 151:
        R.append(r)
print(min(R))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1+, 2+, 3, 4, 5*, 6, 7, 8*, 10+, 12*+, 14*, 16, 18, 19-21+]
# КЕГЭ  = [5, 8, 9, 12, 13, 14, 15, 16, 17, 23]
# на следующем уроке: 9, 11