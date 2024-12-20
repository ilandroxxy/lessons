# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Тип 24 №33526
'''
s = open('files/24.txt').readline()
M = []
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
R = []
for x in alphabet:
    R.append([M.count(x), x])

print(max(R))  # [1517, 'D']
'''


# Определите максимальное количество идущих подряд
# символов среди которых символ T встречается ровно 3 раза.
'''
s = '*****T***T******T*****T********T***T******T*******T****'
# ['*****', '***', '******', '*****', '********', '***', '******', '*******', '****']
# 22 *****T***T******T*****
# 25 ***T******T*****T********
# 25 ******T*****T********T***
# 25 *****T********T***T******
# 27 ********T***T******T*******
# 23 ***T******T*******T****
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # print(s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3])
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
#
# Определите в прилагаемом файле максимальное количество
# идущих подряд символов (длину непрерывной
# подпоследовательности), среди которых символ
# T встречается ровно 100 раз.
'''
s = open('files/24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''


# Определите минимальную подстроку, содержащую
# не менее 3 символов T
'''
s = '*****T***T******T*****T********T***T******T*******T****'
# ['*****', '***', '******', '*****', '********', '***', '******', '*******', '****']
# 12 T***T******T
# 14 T******T*****T
# 16 T*****T********T
# 14 T********T***T
# 12 T***T******T
s = s.split('T')[1:-1]
mini = 10**10
for i in range(len(s)-2):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''


# Тип 24 №59791
# Текстовый файл состоит не более чем из 106 символов
# латинского алфавита. Определите минимальную подстроку,
# содержащую не менее 130 символов W.
'''
s = open('files/24.txt').readline()
s = s.split('W')[1:-1]
mini = 10**10
for i in range(len(s)-129):
    r = 'W' + 'W'.join(s[i:i+129]) + 'W'
    mini = min(mini, len(r))
print(mini)
'''

# Тип 24 №63040
'''
s = open('files/24.txt').readline()
s = s.replace('A', 'A ').replace('B', 'B ')
s = s.split()
maxi = 0
for i in range(len(s)-4):
    r = ''.join(s[i:i+5])[:-1]
    if r.count('A') == 2 and r.count('B') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №68286
'''
import string
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
maxi = 0
s = open('files/24.txt').readline()
for x in 'NOPQRSTUVWXYZ':
    s = s.replace(x, '* *')
    maxi = max(max([len(i) for i in s.split()]), maxi)
    s = s.replace('* *', x)
print(maxi)
'''

s = open('files/24.txt').readline()

s = s.replace('A', 'A ').replace('B', 'B ')
s = s.split()
maxi = 0
for i in range(len(s) - 2):
    r = ''.join(s[i:i+3])[:-1]
    print(r)
    if r.count('A') == 1 and r.count('B') == 1:
        maxi = max(maxi, len(r))
print(maxi)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3?, 4, 5, 6, 7?, 8, 9, 10?, 11?, 12, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:
