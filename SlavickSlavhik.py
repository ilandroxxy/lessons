# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Номер 15
'''
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# Номер 23
'''
def F(a, b):
    if a >= b or a == 13:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(3, 8) * F(8, 18))
'''


# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x//2023)
'''


# минимальное кол-во идущих подряд символов среди которых
# символ Т встречается ровно 3 раза

s = 'TxxxTxxxxxTxxxxxxxTxxxTxxxxxTxxxxTxxxxxxT'
# ['', 'xxx', 'xxxxx', 'xxxxxxx', 'xxx', 'xxxxx', 'xxxx', 'xxxxxx', '']
# 6 TTxxxT
# 11 TxxxTxxxxxT
# 15 TxxxxxTxxxxxxxT
# 13 TxxxxxxxTxxxT
# 11 TxxxTxxxxxT
# 12 TxxxxxTxxxxT
# 13 TxxxxTxxxxxxT
# 9 TxxxxxxTT
'''
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
    print(len(r), r)
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


s = open('0. files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-210):
    r = 'T'.join(s[i:i+211])
    maxi = max(maxi, len(r))
print(maxi)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 24, 25]
# КЕГЭ  = [22, 25]
# на следующем уроке: повторить 22, 19-21, разобрать 3 с пробника

# Второй пробник 28.02.25:
# Славик 16/25 -> 67 вторичных баллов +[1, 2, 4-14, 16, 17, 18] -[3, 15, 19-21, 22-25]