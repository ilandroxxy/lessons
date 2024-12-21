# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
def F(x, y, A):
    return (3 * x + y > A) and (y < x) and (x < 30)


for A in range(1, 120):
    if all(F(x, y, A) == False for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''
'''
def f(x, y, A):
    return (3 * x + y > A) and (y < x) and (x < 30)


R = []
for A in range(1000):
    if all(f(x, y, A) == 0 for x in range(100) for y in range(100)):
        R.append(A)
print(min(R))
'''


# 17 https://education.yandex.ru/ege/task/6488e44b-c19d-41be-a53f-3877c2d12728
'''
M = [int(s) for s in open('files/17.txt')]
R = []
for i in range(len(M)-5):
    x, y, z, w, r, t = M[i:i+6]
    if (z + w) > (x + y) and (z + w) > (r + t):
        if z + w > 0 and x + y > 0 and r + t > 0:
            R.append(z * w)
print(len(R), min(R))
'''

# https://education.yandex.ru/ege/task/062a4793-f5f9-4b96-be39-1a81c87197f3
'''
x = abs(18*7**108 - 5*49**76 + 343**35 - 50)
S = []
while x > 0:
    S.append(x % 49)
    x //= 49
S = S[::-1]
print(S)
print(sum(S))
'''

# 23 https://education.yandex.ru/ege/task/2cbe56c0-d995-4135-8f25-f3423059b3d3
'''
def F(a, b):
    if a >= b or a == 81:
        return a == b
    return F(a + int(str(a)[0]), b) + F(a + 3, b) + F(2 * a - 1, b)

print(F(42, 73) * F(73, 89))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Разобрать как быть с гласными https://education.yandex.ru/ege/task/bdfb8f12-2b10-4f4b-99b0-6d2e045552e2
'''
s = open('files/24.txt').readline()
for x in 'AEIOUY':
    s = s.replace(x, ' ')
s = s.split()
print(s)
maxi = 0
for i in range(len(s)-1):
    r = s[i] + s[i+1]
    if list(r) == sorted(r):
        if len(r) + 1 > maxi:
            maxi = len(r) + 1
print(maxi)
'''

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
