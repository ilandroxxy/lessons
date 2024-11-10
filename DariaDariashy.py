# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 9 https://education.yandex.ru/ege/task/2f370a43-39d3-4557-97a3-920195435a5d
'''
cnt = 0
for s in open('files/9.csv'):
    # print(s)  # 91;91;48;38;13
    M = sorted([int(x) for x in s.split(';')])
    if len(M) == len(set(M)):  # в строке все числа различны;
        if 3 * (M[0] + M[4]) >= 2 * (M[1] + M[2] + M[3]):
            cnt += 1

print(cnt)
'''


# Задание 9  https://education.yandex.ru/ege/task/59213ca9-5841-4d0e-90f4-d69569902d37
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    A = [x for x in M if x > 0]
    B = [x for x in M if x < 0]
    if len(B) > len(A):
        if len(A) != 0 and len(B) > 0:
            if abs(min(B)) > max(A):
                cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/9222d062-000f-4b29-80d0-86b20f9119d2
'''
num = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    num += 1
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    # if len(set(M)) == len(M) - 2:
    if len(copied) == 2:
        if copied[0] >= sum(not_copied) / len(not_copied):
            print(num)
            break
'''


# Задание 9 https://education.yandex.ru/ege/task/0afd47a3-ee9a-44f7-bbd3-22ff7b69d98d
'''
cnt = 0
for s in open('files/9.txt'):
    M = sorted([int(x) for x in s.split()])
    copied = [x for x in M if M.count(x) == 2]
    if len(copied) == 6:
        if (max(copied) + min(copied)) / 2 < sum(M) - sum(copied):
            cnt += 1
print(cnt)
'''


# Задание 9 https://education.yandex.ru/ege/task/2c9beda9-8bb0-497c-b6d3-d4fd322f0df0
'''
n = 0
summa = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    n += 1
    if len(M) == len(set(M)):
        if (M[0] + M[-1]) ** 2 > (M[1] * M[2] * M[3]):
            summa += n
print(summa)
'''


# Задание 9 https://education.yandex.ru/ege/task/d62dc568-941a-44da-870b-b8cc21faee9f
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if (sum(nechet) > sum(chet)) != (len(M) - 1 == len(set(M))):
        cnt += 1
print(cnt)
'''
# True != False
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
