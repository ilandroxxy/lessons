# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
from itertools import *
table = '14 15 18 25 26 28 35 36 37 41 47 51 52 53 58 62 63 67 68 73 74 76 81 82 85 86'
graph = 'FG GF GE EG ED DE EH HE DA AD DB BD DH HD HB BH HC CH CA AC CF FC FA AF BC CB'
print('1 2 3 4 5 6 7 8')
for p in permutations('ADBCHEFG'):
    # i 0    1    2    3    4    5    6    7
    # ('G', 'F', 'E', 'H', 'C', 'D', 'A', 'B')
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''

# https://education.yandex.ru/ege/task/8251f419-7cb9-44fe-8f7e-c170f0fba7d2
'''
cnt = 0
for s in open('C:/9.txt'):
    M = [int(x) for x in s.split()]
    if (len(set(M)) < 4) != (len([x for x in M if x % 2 != 0]) == 3):
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/e35fe06d-0405-44b7-8976-4bd4bc4aaa7b
'''
from itertools import *

cnt = 0
for s in product(sorted('ПРОБНИК'), repeat=6):
    w = ''.join(s)
    cnt += 1
    if w.count('О') == 3 and len(set(w)) == 4:
        print(cnt)
'''

'''
pixels = 1024 * 768
V_27 = 1_638_400 * 220
V_1 = V_27 / 27
i = V_1 / pixels
print(i)  # 16.97530864
i = 16
print(2**i)  # colors = 2 ** i
'''
# 65536

'''
symbols = 197
# alphabet = ?

byte = 25 * 2 ** 20 / 178_080
print(byte)  # 147.20575

byte = 148
bit = byte * 8
i = bit / symbols
print(i)  # 6.010
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
