# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 5946 (Уровень: Средний)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if len(M) == len(set(M)):
        chet = len([x for x in M if x % 2 == 0])
        nechet = len([x for x in M if x % 2 != 0])
        if chet > nechet:
            cnt += 1
print(cnt)
'''


# № 8946 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if M[4] ** 2 > M[0] * M[1] * M[2] * M[3]:
        if (M[4] + M[3]) > (M[0] + M[1] + M[2]) * 2:
            cnt += 1
print(cnt)
'''

'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x)for x in s.split(',')])
    flag = 0
    if all(x == 18 for x in M):
        flag += 1
    if sum(M) % 18 == 0:
        flag += 1
    if flag >= 1:
        cnt +=1
print(cnt)
'''

'''
def F(a, b):
    if a <= b:
        return a == b
    return F(a - 2, b) + (a // 2, b)


print(F(38, 16) * F(16, 2))
'''

def F(a, b):
    if a <= b:
        return a == b
    return F(a - 2, b) + F(a // 2, b)

print(F(38, 16))

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
