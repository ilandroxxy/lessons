# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 12
'''
def f(n):
    s = '5' + '2' * n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    return s


for n in range(4, 10000):
    if sum(map(int, f(n))) == 64:
        print(n)
        break
'''


# Номер 9
'''
c = 0
for s in open('0. files/9.csv'):
    z = [int(i) for i in s.split(';')]

    p = [i for i in z if z.count(i) == 2]
    np = [i for i in z if z.count(i) == 1]

    if len(p) == 4 and len(np) == 3:
        if (sum(p) / len(p)) < (sum(np) / len(np)):
            c += 1
print(c)
'''


# Номер 24
'''
s = open('0. files/24.txt').readline()
s = s.split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''
# 4361 -> 4363


'''
# s[i:i+4]  len(s)-3
s = 'xxxxxTxxxTxxxxxxTxxxxx'
s = ['xxxxx', 'xxx', 'xxxxxx', 'xxxxx']  # maxi
s = ['xxx', 'xxxxxx']  # mini
# 'T' + 'xxxTxxxxxx' + 'T'
'''


# Номер 15
'''
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)


for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 300) for y in range(1, 300)):
        print(A)
        break
'''

'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r
'''

# Номер 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if str(x)[-2:] == '29']
R = []
for i in range(len(M)-2):
    x, y, z = M[i:i+3]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

from itertools import product, permutations
for p in permutations('12345', r=3):
    num = ''.join(p)
    print(num)

for p in product('12345', repeat=4):
    print(p)

# 1, 6, 8, 22, 19-21
# 3, 4, 7, 22

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 11, 13, 17, 18, 11, 22

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина 10/29 -> 51 вторичных баллов +[2, 3, 4, 7, 9, 10, 14, 18, 23, 25] -[1, 5, 6, 8, 12, 11, 13, 15, 17]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
