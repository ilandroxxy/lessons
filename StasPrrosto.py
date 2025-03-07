# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 12
'''
for n in range(4, 10000):
    s = '5' + '2'*n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if sum([int(x) for x in s]) == 64:
        print(n)
        break
'''


# Номер 6
'''
import turtle as t

t.screensize(3000, 3000)
t.tracer(0)
l = 30
t.left(90)
t.down()

for _ in range(4):
    t.forward(l*10)
    t.right(270)

t.up()
t.forward(l*3)
t.right(270)
t.forward(l*5)
t.right(90)
t.down()

for _ in range(2):
    t.forward(l*10)
    t.right(270)
    t.forward(l * 12)
    t.right(270)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(2, 'green')

t.done()
'''


# Номер 9
'''
cnt = 0
for s in open('0. files/9.txt'):
    M = [int(x) for x in s.split()]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''


# Номер 17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if abs(x) % 100 == 29]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''

# Номер 24

# минимальное количество идущих подряд символов, среди которых символ T
# встречается ровно 4 раз.
s = 'TxxxxxTxxTxxxxxTxxxTxxxxTxxxTxxxxT'
# ['', 'xxxxx', 'xx', 'xxxxx', 'xxx', 'xxxx', 'xxx', 'xxxx', '']
# 8 TTxxxxxT
# 10 TxxxxxTxxT
# 10 TxxTxxxxxT
# 11 TxxxxxTxxxT
# 10 TxxxTxxxxT
# 10 TxxxxTxxxT
# 10 TxxxTxxxxT
# 7 TxxxxTT
'''
s = 'TxxxxxTxxTxxxxxTxxxTxxxxTxxxTxxxxT'

s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(len(r), r)
    mini = min(mini, len(r))
print(mini)
'''

'''
s = open('0. files/24.txt').readline()
s = s.split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 9, 8, 11, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:  9, 17, 8, 7, 11, 22, 24

# Первый пробник 21.12.24:
# Стас 9/29 -> 48 вторичных баллов +[2, 3-5, 7, 10, 12, 16, 22] -[1, 6, 8, 9, 11, 13, 14, 15, 17-21, 24-25]

# Второй пробник 28.02.25:
# Стас 18/29 -> 72 вторичных баллов +[1-5, 7, 8, 10, 11, 13-16, 18-21, 23] -[6, 9, 12, 17, 22, 24, 25]
