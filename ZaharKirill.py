# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 5627 (Уровень: Средний) 🌶
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    if all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M)-1)):
        flag += 1
    if flag >= 1:
        cnt += 1
print(cnt)
'''


# № 12797 (Уровень: Средний) 🌶
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    # if len(set(M)) == 3:
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2 and len(uncopied) == 2:
        if all(x % 2 != 0 for x in uncopied):
            if all(x % 2 == 0 for x in copied):
                cnt += 1
print(cnt)
'''

'''
from itertools import *
print('1 2 3 4 5 6 7')  # тут
table = '12 16 21'  # тут
graph = 'AE EA AC'  # тут
for p in permutations('ABCDEFG'):  # тут
    new_table = table
    for i in range(1, 7+1):  # тут
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)



from itertools import *
print('1 2 3 4 5 6 7 8 9')  # тут
table = '14 24 26 34 43 49 51 53 65 74 82 87 92 94'  # тут
graph = 'AK KA KC CK KB BK DB BD DC CD ED DH GD DG GH HG HD DH EF FE '  # тут
for p in permutations('ABCDEFG'):  # тут
    new_table = table
    for i in range(1, 8+1):  # тут
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)
'''


# Единицы измерения информации
# 1 бит - минимальная единица измерения информации
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит

# 64 Мбайт = 64 * 2**23 бит
# 3 Гбайт = 3 * 2**20 Кбайт
# 7 Кбайт = бит


# bit = pixels * i, где i - это кол-во бит на один пиксель
# colors = 2 ** i
'''
pixels = 1280 * 960
colors = 2048  # colors = 2 ** i
i = 11
bit = pixels * i
bit_all = 96_468_992 * 132  # бит на весь пакет
count = bit_all / bit
print(count)  # 942.08
'''


# № 19557 (Уровень: Базовый)
'''
pixels = 1920 * 1080
i = 11
bit = pixels * i
bit_313 = bit * 313
print(bit_313 / 2**23)  # 851.08337
'''


# № 9280 (Уровень: Базовый)
'''
pixels = 512 * 256
bit = 64 * 2 ** 13  # бит
bit = bit * 1.25
i = bit / pixels
print(2 ** i)
'''


# № 7883 (Уровень: Средний)

pixels = 1920 * 1080
print(2 ** 16)
i = 16
bit = pixels * i
byte = bit / 8
byte_100 = byte * 100
disk = 4 * 2**30
print(disk / byte_100)
print(disk - 10 * byte_100)  # 147767296
print((disk - 10 * byte_100) / 2 ** 10)  # 144304

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:

# Первый пробник 21.12.24:
# Захар 4/6 -> 27 вторичных баллов +[2, 8, 12, 14] -[5, 6]
# Kirill 3/6 -> 20 вторичных баллов +[8, 12, 14] -[2, 5, 6]

# Второй пробник 28.02.25:
# Захар 7/13 -> 43 вторичных баллов +[1, 2, 10, 12, 14, 15, 16] -[4, 5, 6, 8, 13, 17, 23, 25]
# Kirill 6/13 -> 40 вторичных баллов +[2, 10, 13, 14, 15, 16] -[5, 6, 8, 12, 17, 23, 25]