# region Домашка: ******************************************************************

# № 5627 (Уровень: Средний) 🌶
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    # if len(M) != len(set(M)):
    copied = [x for x in M if M.count(x) > 1]
    if len(copied) > 0:
        flag += 1
    M = sorted(M)
    # 0 1 2 3 4 5
    x = M[1] - M[0]
    if M[2] - M[1] == x and M[3] - M[2] == x and M[4] - M[3] == x and M[5] - M[4] == x:
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''


# № 6999 (Уровень: Базовый)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    A = [x for x in M if x % 3 == 0]
    if len(A) == 3:
        if max(M) - min(M) <= sum(A):
            cnt += 1
print(cnt)
'''


# № 23747 Демоверсия 2026 (Уровень: Базовый)
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 4:
        if sum(copied1) / 4 <= copied3[0]:
            print(n, sum(M))
'''


# № 12795 (Уровень: Средний)
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    avg = sum(M) / len(M)
    if int(avg) in M:
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 25364 (Уровень: Базовый)

clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 10:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if x > 20:
        clustersB[0].append([x, y])
    if x < 20 and y > 22:
        clustersB[1].append([x, y])
    if x < 20 and y < 22:
        clustersB[2].append([x, y])







# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 27
