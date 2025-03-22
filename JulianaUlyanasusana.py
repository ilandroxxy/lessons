# region Домашка: ******************************************************************


# Номер 8
'''
s = sorted('СБОРНИК')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        world = a + b + c + d + e + f
                        n += 1
                        if world.count('Б') == 2 and world.count('К') <= 1:
                            if world[0] != 'Р':
                                print(n)
'''


# Номер 12
'''
for n in range(3,10000):
    s='5'+'2'*n
    while '52' in s or '1122' in s or '2222'in s:
        if '52'in s:
            s = s.replace('52','11',1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122'in s:
            s = s.replace('1122', '25', 1)

    # summa = 0
    # for i in s:
    #     summa += int(i)

    summa = sum([int(x) for x in s])

    summa = sum(map(int, s))

    if summa == 64:
        print(n)
        break
'''


# Номер 5
'''
def con(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


R = []
for n in range(1, 1000):
    s = con(n, 3)

    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + con(x, 3)
    r = int(s, 3)  # перевод из 3-й в 10-ю 
    if r > 150:
        R.append(n)
print(min(R))
'''


# Номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''

# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
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


# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 34 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]

# Второй пробник 28.02.25:
# Ульяна 10/29 -> 51 вторичных баллов +[1-4, 6, 10, 13, 15, 16, 23] -[5, 8, 9, 12, 14, 17, 25]
