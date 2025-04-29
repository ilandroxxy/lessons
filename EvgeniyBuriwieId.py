# region Домашка: ************************************************************

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# 14 номер 21709
'''
R = []

for x in range(1, 3000+1):
    n = 4**210+4**110-x
    M = []
    while n>0:
        M.append(n%4)
        n //= 4
    M.reverse()

    R.append([M.count(0), x])

print(max(R))
for x in R:
    if x[0] == 105:
        print(x)
        # [105, 1024]
        # [105, 2048]
'''

'''
for n in range(4,10000):
    s = "4" + "2" * n
    while "42" in s or "8222" in s or "2222" in s:
        if "42" in s:
            s = s.replace("42","2",1)
        if "8222" in s:
            s = s.replace("8222","24",1)
        if "2222" in s:
            s = s.replace("2222","8",1)

    summa = sum([int(x) for x in s])
    if summa % 110 == 0:
        print(n)
        break
'''


'''
from itertools import *
print('1 2 3 4 5 6 7 8')
table = '12 13 21 26 28 31 35 38 45 47 48 53 54 57 62 67 74 75 76 82 83 84'
graph = 'AE EA AF FA FD DF FC CF CG GC GB BG GH HG BH HB BD DB DE ED EH HE'
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''
# 1 2 3 4 5 6 7 8
# A F E B H C G D


from itertools import *
print('1 2 3 4 5 6 7')
table = '12 13 14 21 23 26 31 32 41 45 47 54 56 57 62 65 74 75'
graph = 'FB BF FD DF FG GF BD DB DA AD AE EA EG GE EC CE CG GC'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)



# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1.1, 2, 3, 4, 5, 7, 8, 9, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25]
# КЕГЭ = [7, 11, 12, 17, 19-21, 22]
# на следующем уроке: 9, 10,


# Первый пробник 21.12.24:
# 4/8 -> 29 вторичных баллов +[1, 10, 16, 23] -[2, 4, 12, 15]

# Второй пробник 28.02.25:
# 10/29 -> 48 вторичных баллов +[1, 2, 4, 10, 12, 14, 15, 16, 23, 25] -[11]
