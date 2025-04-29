# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21895 Открытый вариант 2025 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    M = sorted(M)
    if len(set(M)) == len(M):
        if (M[-1] + M[-2]) <= (M[0] + M[1] + M[2]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/9a4ed264-8f61-4713-91c3-37fceb735e15
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    
    flag = 0
    
    if len(set(M)) == len(M):
        flag += 1

    M = sorted(M)
    if (M[-1]) <= (M[0] + M[1] + M[2] + M[3] + M[4]):
         flag += 1
        
    if flag == 0:
        cnt += 1
        
print(cnt)
'''


# https://education.yandex.ru/ege/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 3]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 3 and len(uncopied) == 3:
        if sum(copied) ** 2 > sum(uncopied) ** 2:
            cnt += 1
print(cnt)
'''

# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 10 == 6 and 1000 <= abs(x) <= 9999]
B = [x for x in M if str(x)[-1] == '6' and len(str(abs(x))) == 4 and x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''
# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Матвей 10/14 -> 51 вторичных баллов +[1, 3, 4, 6, 7, 10, 11, 14, 18, 25] -[2, 5, 8, 12]

# Второй пробник 28.02.25:
# Матвей 14/29 -> 62 вторичных баллов +[1-4, 6, 7, 10, 11, 14, 15, 16, 18, 23, 25] -[5, 8, 12, 13]
