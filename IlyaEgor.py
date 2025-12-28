# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
def F(a,b):
    if a < b or a == 36:
        return 0
    if a == b:
        return 1
    if a > b:
        return F(a-3,b) + F(a-6,b) + F(a//2,b)

print(F(86,53) * F(53,12))
'''


# 25
'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

cnt = 0
for x in range(1_350_050+1, 10**10):
    d = [j for j in divisors(x) if j != x and j != 11 and j % 100 == 11]
    if len(d) > 0:
        print(x, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# len(str(2939)) == 4
# len(str(-2939)) == 5
# len(str(abs(-2939))) == 4

# print(123 % 100)  # 23
# print(-123 % 100)  # 77
# print(abs(-123) % 100)  # 23

# 17
'''
M = [int(s) for s in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30 or str(x)[-2:] == '30']
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    if M.count(max(M)) == 1:
        copied3 = [x for x in M if M.count(x) == 3]
        copied1 = [x for x in M if M.count(x) == 1]
        if len(copied3) == 3 and len(copied1) == 4:
            cnt += 1
print(cnt)
'''


'''
def divisors(x):
    d = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

print([x for x in range(100) if len(divisors(x)) == 2])


def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))

print([x for x in range(100) if len(divisors(x)) == 0])
'''


# № 24896 (Уровень: Базовый)
def divisors(x):
    d = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            d.append(j)
            d.append(x // j)
    return sorted(set(d))


cnt = 0
for x in range(1_475_000-1, 0, -1):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        S = sum(d)
        if S != 0 and S < 42000 and S % 6 == 0:
            print(x, S)
            cnt += 1
            if cnt == 5:
                break







# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
