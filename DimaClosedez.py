# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
s = open('0. files/24.txt').readline()
while 'ABA' in s or 'BAB' in s:
    if 'ABA' in s:
        s = s.replace('ABA', '*', 1)
    if 'BAB' in s:
        s = s.replace('BAB', '+', 1)

for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''

# s = 'CABCABABABABCBA'
'''
s = open('0. files/24.txt').readline()
cnt = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('ABA', 'BAB'):
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 2
print(maxi)
'''

'''
s = open('0. files/24.txt').readline()
s = s.replace('O', 'A').replace('F', 'D').replace('C', 'D')
s = s.replace('AAD', '*')
s = s.replace('A', ' ').replace('D', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №45258
'''
s = open('0. files/24.txt').readline()
s = s.replace('AB', '*').replace('CB', '+')
for x in 'ABC':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
'''


# s = 'xxxAAxxxxAAxxx'
# s = 'xxxA AxxxxA Axxx'
# s = 'xxx xxxx xxx'
'''
s = open('0. files/24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
R = [len(x) for x in s.split()]
print(max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке: 14

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


