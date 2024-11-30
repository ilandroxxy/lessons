# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://stepik.org/lesson/1038834/step/8?unit=1062779
# Определите максимальную длину подстроки, которая ограничена с одной стороны
# буквой A, а с другой - D и не содержит других букв A и D внутри.
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'A A').replace('D', 'D D')
print(max([len(x) for x in s.split() if x.count('A') == 1 and x.count('D') == 1]))
'''


# https://inf-ege.sdamgia.ru/problem?id=38958
# Определите максимальное количество идущих подряд символов, среди которых
# не более одной буквы A.
'''
s = open('files/24.txt').readline()
s = s.split('A')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'A' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)

s = open('files/24.txt').readline()
maxi = 0
s = s.replace('A', 'A ').split()
for i in range(len(s)-1):
    r = ''.join(s[i:i+2])[:-1]
    maxi = max(maxi, len(r))
print(maxi)
'''


# Определите максимальное количество идущих подряд символов,
# среди которых каждая из букв A и B встречается не более двух раз.
'''
s = open('files/24.txt').readline()
maxi = 0
s = s.replace('A', 'A ').replace('B', 'B ').split()
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('A') == 2 and r.count('B') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''

'''
s = open('files/24.txt').readline().split('D')
print(s)
count = 1
maxi = 0
for i in range(len(s)):
    if s[i].count('O') <= 2:
        count += len(s[i]) + 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''


s = open('files/24.txt').readline()
count = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('LDR', 'DRL', 'RLD'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
