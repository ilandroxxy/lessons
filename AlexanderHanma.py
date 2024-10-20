# region Домашка: ******************************************************************

# № 18045 (Уровень: Базовый)
# (Л. Шастин) В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000
# включительно. Определите количество пар последовательности, в которых
# сумма последних цифр элементов равна количеству двузначных чисел в
# последовательности. В ответе запишите количество найденных пар, затем
# минимальную из сумм элементов таких пар. В данной задаче под парой
# подразумевается два идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x % 10) + (y % 10) == len(D):
        R.append(x + y)
print(len(R), min(R))
'''


# № 17968 (Уровень: Средний)
# (Л. Шастин) Откройте файл электронной таблицы, содержащей в
# каждой строке четыре натуральных числа. Определите количество строк таблицы,
# содержащих числа, для которых выполнены оба условия:
# – наибольшее из четырёх чисел меньше суммы трёх других;
# – сумма чётных чисел равна сумме нечётных.
# В ответе запишите только число.
'''
cnt = 0
for s in open('files/9.txt'):
    M = [int(x) for x in s.split()]
    if max(M) < sum(M) - max(M):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if sum(chet) == sum(nechet):
            cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 24 №27696
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов L.
# Хотя бы один символ L находится в последовательности.

# Вариант 1
'''
s = open('files/24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    # if s[i] == 'L' and s[i+1] == 'L':
    if s[i:i+2] == 'LL':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# Вариант 1
'''
s = open('files/24.txt').readline()
s = s.replace('R', ' ').replace('D', ' ')
print(max([len(x) for x in s.split()]))
# ['LLL', 'LLLLL', 'LLLLL', 'LLLLLLL', 'LLLLLLLLLL', 'LLLL', 'LLLLLLL', 'LLLL']
# [3, 5, 5, 7, 10, 4, 7, 4]
'''


# Тип 24 №27695
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)


s = open('files/24.txt').readline()
s = s.replace('LL', 'L L').replace('DD', 'D D').replace('RR', 'R R')
print(max([len(x) for x in s.split()]))
'''


# Тип 24 №27689
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ...
# (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
'''
s = open('files/24.txt').readline()
count = 2
maxi = 0
for i in range(len(s) - 2):
    if s[i:i+3] in ('XYZ', 'YZX', 'ZXY'):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''


# Тип 24 №47228
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида:
# согласная  + гласная.
'''
s = open('files/24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D').replace('F', 'D')
while 'DD' in s or 'AA' in s:
    s = s.replace('AA', 'A A').replace('DD', 'D D')
R = []
for x in s.split():
    if x[0] == 'A':
        R.append(x[1:])
    else:
        R.append(x)

print(max([len(x) / 2 for x in R]))
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
