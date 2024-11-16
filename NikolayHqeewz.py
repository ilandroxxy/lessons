# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 24 №27687
'''
# Вариант 1
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'Y' and s[i+1] == 'Y':
    if s[i:i+2] == 'YY':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)


# Вариант 2
s = open('files/24.txt').readline()
s = s.replace('X', ' ').replace('Z', ' ')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27689

# XYZXYZXYZ
'''
s = open('files/24.txt').readline()
count = 2
maxi = 0
for i in range(len(s)-2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''

# Тип 24 №59817

# ertAAijklAAlkoko
# ertA AijklA Alkoko
# ert  ijkl  lkoko
'''
s = open('files/24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
