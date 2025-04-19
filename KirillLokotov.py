# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# https://education.yandex.ru/ege/task/9aeb7cc2-2c1f-40b3-80b5-142a14f3969f
'''
from itertools import permutations

print('1 2 3 4 5 6 7 8')
table = '14 16 17 18 23 24 27 28 32 37 41 42 45 48 54 56 58 61 65 68 71 72 73 78 81 82 84 85 86 87'
graph = 'ВЕ ЕВ ВА АВ ВД ДВ ВЖ ЖВ ЖД ДЖ ЖЗ ЗЖ ЖГ ГЖ ГЗ ЗГ ЗЕ ЕЗ ЗД ДЗ ДА АД ДБ БД ДЕ ЕД АБ БА БЕ ЕБ'

for per in permutations('АБВГДЖЗЕ'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*per)
'''

# 1 2 3 4 5 6 7 8
# В З Г Е Б А Ж Д
# Е Ж Г В А Б З Д


# https://education.yandex.ru/ege/task/6fbcf8cd-d727-4ea5-86b2-12193523ab8b
'''
from itertools import *
cnt = 0
for p in product('ВОЗДУХ', repeat=5):
    word = ''.join(p)
    word = word.replace('У', 'О')
    if word.count('О')  == 1:
        word = word.replace('В', 'Х')
        if 'ОХ' not in word and 'ХО' not in word:
            cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/task/f5dc5b2a-ddaf-41fb-93d4-7a698e31cda8
'''
def F(x, y, A):
    return ((x >= A) or (121 >= x**2)) and ((y**2 < 49) or (A < y))

for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
'''

'''
print('x y u w F')
for x in 0, 1:
    for y in 0, 1:
        for u in 0, 1:
            for w in 0, 1:
                F = (not((y <= w) == x)) and u
                print(x, y, u, w, int(F))
'''
# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 17, 23, 9, 8
