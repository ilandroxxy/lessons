# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************
'''
s = '01'
k = 0
for x in s:
    for y in s:
        num = x + y
        k += 1
        print(k, num)

'''


# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
# A = [x for x in M if str(x)[-1] == '6' and len(str(abs(x))) == 4]
A = [x for x in M if abs(x) % 10 == 6 and 1000 <= abs(x) <= 9999]
B = [x for x in A if x > 0]
# B = [x for x in M if abs(x) % 10 == 6 and 1000 <= x <= 9999]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    # в которых ровно один элемент является четырёхзначным числом и оканчивается на 6
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''
# является четырёхзначным числом и оканчивается на 6,
# минимального положительного элемента последовательности, являющегося четырёхзначным числом, которое оканчивается на 6.

'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    k = 0
    M = sorted(M)
    if len(set(M)) == 6:
        k += 1
    if M[-1] > (M[0] + M[1] + M[2] + M[3] + M[4]):
        k += 1
    if k == 2:
        cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    M = sorted(M)
    if (M[-1] + M[0]) ** 2 > (M[1] ** 2 + M[2] ** 2 + M[3] ** 2):
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/7eeb5357-91a8-4e1a-b4ec-dafe92df2f09
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        if 3 * (copied[0] ** 2) > (uncopied[0] ** 2  + uncopied[1] ** 2 + uncopied[2] ** 2):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/cecbe39b-e6f6-479b-b23b-b0261ac504fe
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(uncopied) == 3:
        if sum(copied) / 4 < sum(M) / 7:
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/01a992ef-abe9-43e7-8dfe-5dd7e31159ff
'''
n = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(copied) == 3 and len(uncopied) == 4:
        if len(chet) > len(nechet):
            print(n)
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 18, 19-21]
# КЕГЭ = []
# на следующем уроке: 2, 8, 5


# Первый пробник 7.03.25:
# Арина 12/29 -> 56 вторичных баллов +[1, 2, 3, 4, 5, 8, 9, 11, 12, 14, 15, 23] -[7, 13, 17, 19-21, 18, 25]
