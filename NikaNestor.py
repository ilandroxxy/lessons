# region Домашка: ******************************************************************

# № 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        # if ((x + y) % 18 == 0) ^ ((x * y) % 18 == 0):
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************



# Методы строк .split() и ''.join()
'''
ip = '234.34.78.90'
new_ip = ip.split('.')
print(new_ip)  # ['234', '34', '78', '90']

new_ip = ['234', '34', '78', '90']
ip = '* *'.join(new_ip)
print(ip)  # 234.34.78.90
'''


# Способы открытия файла для 9 номера
'''
for s in open('0. files/9.txt'):
    print(s)  # '48	31	3	32'
    M = [int(x) for x in s.split()]
    print(M)

for s in open('0. files/9.csv'):
    # '28;197;100;54;54;152;34'
    M = [int(x) for x in s.split(';')]
    print(M)  # [118, 182, 35, 176, 171, 171, 171]
'''


# № 23555 Пересдача 03.07.25 (Уровень: Базовый)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied2) == 2 and len(copied1) == 2:
        if max(copied3 + copied2) > max(copied1):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/622b91cc-fe32-4b92-9127-6137aae32039
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if len(M) == len(set(M)):  # в строке все числа различны;
        M = sorted(M)
        if (M[-1] + M[-2]) <= (M[-3] + M[-4] + M[-5]):
            cnt += 1
print(cnt)
'''

# Как работает функция permutations
'''
from itertools import permutations
for p in permutations([6, 54, 53, 39]):
    print(p)
    # (6, 54, 53, 39)
    # (6, 54, 39, 53)
    # (6, 53, 54, 39)
    # (6, 53, 39, 54)
    # (6, 39, 54, 53)
    # (6, 39, 53, 54)
    # (54, 6, 53, 39)
    # (54, 6, 39, 53)
    # (54, 53, 6, 39)
    # (54, 53, 39, 6)
    # (54, 39, 6, 53)
    # (54, 39, 53, 6)
    # (53, 6, 54, 39)
    # (53, 6, 39, 54)
    # (53, 54, 6, 39)
    # (53, 54, 39, 6)
    # (53, 39, 6, 54)
    # (53, 39, 54, 6)
    # (39, 6, 54, 53)
    # (39, 6, 53, 54)
    # (39, 54, 6, 53)
    # (39, 54, 53, 6)
    # (39, 53, 6, 54)
    # (39, 53, 54, 6)
'''

# https://education.yandex.ru/ege/task/c51900be-b855-4ffb-97d5-8402bb52ffd8
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/f4fdf6fb-9ba6-4a16-b901-0b495310b132

# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа. Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# наибольшее из четырёх чисел меньше суммы трёх других;
# четыре числа нельзя разбить на две пары чисел с равными суммами.
# В ответе запишите только число.
'''
from itertools import permutations
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
            print(M)
            cnt += 1
print(cnt)
'''

'''
# четыре числа нельзя разбить на две пары чисел с равными суммами.
if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):

# четыре числа можно разбить на две пары чисел с равными суммами.
if any(p[0] + p[1] == p[2] + p[3] for p in permutations(M)):
'''

# https://education.yandex.ru/ege/task/3c10485a-aca0-427e-8464-c7669e3315f9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if sum(copied1) / 3 <= sum(M) / 7:
            cnt += 1
print(cnt)
'''


# № 19117 (Уровень: Средний)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    flag = 0
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied1) == 3:
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > 0 and len(nechet) > 0:
        if sum(chet) > sum(nechet):
            flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [9, 17]
# КЕГЭ = []
# на следующем уроке:
