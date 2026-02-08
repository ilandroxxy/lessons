# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# ЕГКР 24 номер вариант 2
'''
s = open('files/24.txt').readline()
for x in '2468':
    s = s.replace(x, '*')
s = s.split('W')
maxi = 0
for i in range(len(s)-36):
    r = 'W'.join(s[i:i+37])
    if r.count('*') == 1:
        i = r.index('W')
        if r[i - 1] == '*':
            maxi = max(maxi, len(r))
print(maxi)
'''


# Задание 19-21
'''
from math import ceil, floor
def F(s, n):
    if s <= 20:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-2, n-1), F(s-4, n-1), F(floor(s/2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(21, 1000) if F(s, n=2)])
print([s for s in range(21, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(21, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# Задание 17 Вариант 2 ЕГКР
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 10]
R = []
for i in range(len(M) - 2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# Задание 9 Вариант 2 ЕГКР
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    print(M)
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]  # [5 5 7 7]
    if len(copied2) == 4 and len(copied1) == 3:
        # if M.count(max(M)) == 1:
        if max(M) in copied1:
            cnt += 1
print(cnt)
'''

'''
def F(a, b):
    if a < b or a == 26 or a == 76:
        return 0
    elif a == b:
        return 1
    else:
        return F(a-2, b) + F(a-4, b) + F(a//2, b)

print(F(86, 39) * F(39, 14))
'''


def divisors(x):
    d = []
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(13200000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        M = min(d) + max(d)
        if M % 100 == 55 and M > 30000:
            print(x, M)
            cnt += 1
            if cnt == 7:
                break

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [19-21]
# на следующем уроке: 10, (26)