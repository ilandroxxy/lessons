# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 9364
'''
cnt = 0
for s in open('0. files/9.csv'):
    k = 0
    M = [int(x) for x in s.split(';')]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if sum(nechet) > sum(chet):
        k = k + 1
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(uncopied) == 3:
        k = k + 1
    if k == 1:
        cnt += 1
print(cnt)
'''

# 18116
'''
summa = 0
n = 0
for s in open('0. files/9.csv'):
    n += 1
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3 and x % 2 == 0]
    uncopied = [x for x in M if M.count(x) == 1 and x % 2 != 0]
    if len(copied) == 3 and len(uncopied) == 3:
         if sum(copied) ** 2 > sum(uncopied) ** 2:
             summa += n
print(summa)
'''

# 8554

cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    tri = [x for x in M if str(x)[-1] == '3']
    pol = [x for x in M if x > 0]
    otr = [x for x in M if x < 0]
    if len(tri) == 3 and sum(pol) ** 2 < sum(otr) ** 2:
        print(M)
        cnt += 1
print(cnt)

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
