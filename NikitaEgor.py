# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: *************************************************************


'''
from itertools import permutations

for p in permutations('abc'):
    print(p)
    # ('a', 'b', 'c')
    # ('a', 'c', 'b')
    # ('b', 'a', 'c')
    # ('b', 'c', 'a')
    # ('c', 'a', 'b')
    # ('c', 'b', 'a')
'''


# № 31108 Основная волна 18.06.26(Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'DH HD DA AD HF FH HB BH FE EF EG GE GA GC CG AG AC CA CB BC'
for p in permutations('ABCDEFHG'):

    #         i     1    2    3    4    5    6    7    8
    #         p = ('G', 'H', 'F', 'E', 'D', 'B', 'C', 'A')
    # new_table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
    # new_table = 'GH GD GA HG HC ...'

    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    print(new_table)
    print(graph)
    print('--------------')
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7 8
# G E B D C H F A
# G E D B A H F C


graph = 'DH HD DA AD HF FH HB BH FE EF EG GE GA GC CG AG AC CA CB BC'
print(graph.split())
# ['DH', 'HD', 'DA', 'AD', 'HF', 'FH', 'HB', 'BH', 'FE', 'EF', 'EG', 'GE', 'GA', 'GC', 'CG', 'AG', 'AC', 'CA', 'CB', 'BC']

new_table = 'HD DA AD HF FH HB BH FE EF EG GE GA GC CG AG AC CA CB BC DH'


ip = '23.45.234.45'
print(ip.split('.'))  # ['23', '45', '234', '45']
print(set(ip.split('.')))  # {'45', '23', '234'}
'''


# № 31108 Основная волна 18.06.26(Уровень: Базовый)
'''
print('1 2 3 4 5 6 7 8')
from itertools import permutations
table = '12 15 18 21 27 35 36 46 48 51 53 58 63 64 67 72 76 81 84 85'
graph = 'DH HD DA AD HF FH HB BH FE EF EG GE GA GC CG AG AC CA CB BC'
for p in permutations('ABCDEFHG'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
        
# 1 2 3 4 5 6 7 8
# G E B D C H F A
# G E D B A H F C
'''
# 1 2 3 4 5 6 7 8
# G E B D C H F A
# G E D B A H F C


# № 29333 Открытый вариант 2026(Уровень: Базовый)

print('1 2 3 4 5 6 7')
from itertools import permutations
table = '12 17 21 25 26 27 36 37 45 52 54 56 62 63 65 67 71 72 73 76'
graph = 'АБ БА БД ДБ БВ ВБ ВД ДВ ДК КД ДЕ ЕД ЕК КЕ ЕВ ВЕ ЕГ ГЕ ГВ ВГ'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)

# 1 2 3 4 5 6 7
# Г В К А Б Д Е
# К Д Г А Б В Е



# endregion Урок: *************************************************************
# #
# #
# 2027
# ФИПИ = []
# КЕГЭ = []
#
# 2026
# ФИПИ = [1, 2, 3, 5, 8, 11, 10, 13, 14, 15, 16, 17, 18, 19-21, 22]
# КЕГЭ = [1, 2, 3, 12, 10]
# на следующем уроке:
