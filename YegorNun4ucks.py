# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 5 Номер 17668
'''
mx = 10000000000000
for n in range(28, 10000):
    n = f'{n:b}'
    if n.count('1') % 2 == 0:
        n += '0'
        res = []
        for i in n:
            res.append(i)
        res[0] = '1'
        res[1] = '0'

        r = ''.join(res)
    else:
        n += '1'
        res = []
        for i in n:
            res.append(i)
        res[0] = '1'
        res[1] = '1'
        r = ''.join(res)

    r = int(r, 2)
    mx = min(mx, r)
print(mx)
'''

'''
R = []
for n in range(28, 10000):
    b = f'{n:b}'
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '10' + b[2:] + '1'
    r = int(b, 2)
    R.append(r)

print(min(R))
'''


# Тип 8 Номер 17671
'''
from itertools import *
for num, i in enumerate(product(sorted('ЛАЙМ'), repeat=5), 1):
    s = ''.join(i)
    print(num, s)
    if s.count('М') == 0 and s.count('Л') == 0 and 'ЙЙ' not in s:
        last = num
print(last)
'''


# Тип 9 Номер 17672
'''
cnt = 0
for s in open('9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    # if max(M) + min(M) < sum(M) - max(M) - min(M):
    if M[0] + M[3] < M[1] + M[2]:
        cnt += 1
print(cnt)
'''


# Тип 17 Номер 17680
'''
a = [int(x) for x in open('17.txt')]
cnt = 0
mx = 0
mm = 1000000000
for i in range(len(a)):
    if a[i] > 0 and a[i] % 41 == 0:
        mm = min(mm, a[i])
for i in range(len(a) - 1):
    val = abs(a[i] - a[i+1])
    if a[i] != a[i+1] and val % mm == 0:
        cnt += 1
        mx = max(mx, a[i] + a[i+1])
print(cnt, mx)


a = [int(x) for x in open('17.txt')]
m = min([x for x in a if abs(x) % 41 == 0 and x > 0])
R = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if x != y and abs(x - y) % m == 0:
        R.append(x + y)
print(len(R), max(R))
'''


# Тип 23 Номер 17680
'''
def f(st, end):
    if st < end:
        return 0
    elif st == end:
        return 1
    else:
        return f(st - 2, end) + f(st // 2, end)


print(f(38, 10) * f(10, 2))


def f(st, end):
    if st <= end:
        return st == end
    return f(st - 2, end) + f(st // 2, end)


print(f(38, 10) * f(10, 2))
'''


'''
import time
start = time.time()

# def divisors(n):
#     div = []
#     for j in range(1, n+1):
#         if n % j == 0:
#             div.append(j)
#     return div


def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div += [j, n // j]
            # div.append(j)
            # div.append(n // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))


print(time.time() - start)  # 3.2987 -> 0.000351905
print(3.2987 / 0.000351905)  # 9373.836
'''


'''
def f(n):
    for i in range(2, n):
        if n % i == 0 and i % 10 == 7 and i != 7:
            return i

for i in range(700_001, 800_000):
    if f(i):
        print(i, f(i))
'''


def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div += [j, n // j]
    return sorted(set(div))


cnt = 0
for n in range(700_001, 800_000):
    d = [j for j in divisors(n) if j % 10 == 7 and j != 7]
    if len(d) > 0:
        print(n, min(d))
        cnt += 1
        if cnt == 5:
            break


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
