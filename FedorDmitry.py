# region Домашка: ******************************************************************

'''
from math import ceil, floor
def F(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3 , n-1), F(floor(s / 5) , n-1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(506, 20000) if F(s, n=2)])
print([s for s in range(506, 10000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(506, 10000) if F(s, n=4) and not F(s, n=2)])


# 19: 12649
# 20: 2533, 2534
# 21: 2536
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 19233 ЕГКР 21.12.24 (Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
graph = 'BD DB BE EB BC CB CH HC HE EH HF FH DE ED DG GD GA AG GF FG AF FA'
for p in permutations('ABCDEFGH'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # E H B D F A C G
'''



'''
# i 0    1    2    3    4    5    6    7
# ('H', 'G', 'F', 'E', 'D', 'C', 'B', 'A')
#   1    2    3    4    5    6    7    8

nt = '12 13 14 21 25 27 31 34 37 41 43 48 52 56 58 65 68 72 73 84 85 86'
nt = nt.replace('1', 'H')
nt = nt.replace('2', 'G')
nt = nt.replace('3', 'F')
nt = nt.replace('4', 'E')
nt = nt.replace('5', 'D')
nt = nt.replace('6', 'C')
nt = nt.replace('7', 'B')
nt = nt.replace('8', 'A')
print(nt)  # HG HF HE GH GD GB FH FE FB EH EF EA DG DC DA CD CA BG BF AE AD AC
'''


# https://education.yandex.ru/ege/inf/task/bffe4eae-4210-48ec-af0e-cfb78d3f89c1
'''
print('1 2 3 4 5 6 7')
from itertools import *
t = '12 13 14 21 23 26 31 32 41 45 47 54 56 57 62 65 74 75'
g = 'BD DB BF FB FG GF FD DF GE EG GC CG CE EC CA AC AD DA'
for p in permutations('ABCDEFG'):
    nt = t
    for i in range(1, 7+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(g.split()):
        print(*p)
        # 1 2 3 4 5 6 7
        # F D B G C A E
        # G C E F D A B
'''


# https://education.yandex.ru/ege/inf/task/54241e14-fb77-417d-8148-09aeb2ce78a4

print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 13 15 21 23 31 32 34 35 36 37 38 43 46 51 53 63 64 67 73 76 78 83 87'
graph = 'АБ БА АВ ВА АГ ГА БГ ГБ ВГ ГВ ГЕ ЕГ ГЗ ЗГ ГЖ ЖГ ГД ДГ ЕЗ ЗЕ ДЖ ЖД ЗЖ ЖЗ'
for p in permutations('АБВГДЕЖЗ'):
    nt = table
    for i in range(1, 8+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)


print('1 2 3 4 5 6 7 8 9')
from itertools import permutations
table = '13 31 16 61 17 71 25 52 28 82 36 63 37 73 46 64 49 94 57 75 68 86 78 87 79 97  89 98'
graph = 'DA AD AE EA DF FD FE EF EB BE EG GE EI IE BG GB CG GC BC CB FC CF CH HC HI IH  FI IF'
for p in permutations('ABCDEFGHI'):
    nt = table
    for i in range(1, 9+1):
        nt = nt.replace(str(i), p[i-1])
    if set(nt.split()) == set(graph.split()):
        print(*p)



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 5, 8, 9, 14, 15, 16, 17, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке: Из пробника глянуть 8, 17 номера
