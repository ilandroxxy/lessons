# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Статград 23.10.25 вариант 1, номер 8
'''
cnt = 0
from itertools import *
alp = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in product(alp[:15], repeat = 4):
    k = 0
    if x[0] != '0':
        if x.count('8') == 1:
            for i in range(len(x) - 1):
                if x[i] != x[i + 1]:
                    k += 1
            if k == 3:
                cnt += 1
print(cnt)


cnt = 0
from itertools import *
alp = sorted('1234567890QWERTYUIOPASDFGHJKLZXCVBNM')
for x in product(alp[:15], repeat = 4):
    num = ''.join(x)
    if num[0] != '0':
        if num.count('8') == 1:
            if all(p*2 not in num for p in alp[:15]):
                cnt += 1
print(cnt)
'''


# Статград 23.10.25 вариант 1, номер 23
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return F(a * 3, b) + F(a * 2, b) + F(a + 1, b)

print(F(6, 14) *F(14,18) * F(18,48))  # 24
print(F(6, 14) * F(14,48))  # 45
print(F(6, 18) * F(18,48))  # 48
print((48 + 45) - 24)  # 69
'''



# Статград 23.10.25 вариант 1, номер 25
'''
def pdr(n):
    S = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            S.append(i)
            S.append(n // i)
    return sorted(set(S))


def sl(n):
    if len(pdr(n)) == 0:
        return 1
    else:
        return 0

cnt = 0
for n in range(1325000-1, 1, -1):
    p = pdr(n)
    b = [i for i in p if sl(i)]
    if len(b) > 0:
        if sum(b) <= 30000 and sum(b) % 5 == 0:
            print(n)
            cnt += 1
            if cnt == 5:
                break
'''

'''
def pdr(n):
    S = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            S.append(i)
            S.append(n // i)
    return sorted(set(S))

cnt = 0
for n in range(1325000-1, 1, -1):
    b = [i for i in pdr(n) if len(pdr(i)) == 0]
    if len(b) > 0:
        if sum(b) <= 30000 and sum(b) % 5 == 0:
            print(n)
            cnt += 1
            if cnt == 5:
                break
'''

# Статград 23.10.25 вариант 1, номер 9
'''
cnt = 0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    p = [x for x in M if x == min(M)]
    copy1 = [x for x in M if M.count(x) == 1]
    # if (2 <= len(p) <= 3) and (5 <= len(copy1) <= 6):
    # if (len(p) == 2 and len(copy1) == 6) or (len(p) == 3 and len(copy1) == 5):
    if len(p) in (2, 3) and len(copy1) in (5, 6):
        if (copy1[0] ** 2 + copy1[-1] ** 2) <= (sum(copy1) - min(copy1) - max(copy1)) ** 2:
            cnt += 1
print(cnt)
'''





# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25, 27]
# КЕГЭ = []
# на следующем уроке:
