# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
from itertools import product
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    n += 1
    print(n, word)


from itertools import product
for n, p in enumerate(product(sorted('СТРОКА'), repeat=5), 1):
    word = ''.join(p)
    print(n, word)
'''

# Аналог функции int(s, b), но универсальный по размеру и через списки list()
'''
def my_int(L: list, b: int):
    return sum([x*b**i for i, x in enumerate(L[::-1], 0)])

print(my_int([1, 0, 0, 0], 2))  # 8
'''


#
# № 9918 (Уровень: Сложный)
'''
def my_int(L, b):
    return sum([x*b**i for i, x in enumerate(L[::-1], 0)])

RES = []
for x in range(10, 67):
    for y in range(0, x):
        A = my_int([7, 3, x, 1, y], 67)
        B = my_int([4, 9, y, 6, x], x)
        RES.append(A + B)
print(len(set(RES)))  # 2166
'''


# № 23746 Демоверсия 2026 (Уровень: Базовый)
'''
from itertools import product
RES = []
n = 0
for p in product(sorted('СТРОКА'), repeat=5):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word[0] not in 'АСТ':
            if word.count('О') == 2:
                RES.append(n)
print(max(RES))
'''


# № 21407 Досрочная волна 2025 (Уровень: Базовый)
'''
from itertools import product
cnt = 0
for p in product('ДГИАШЭ', repeat=5):
    word = ''.join(p)
    if word[0] not in 'ИАЭ':
        if word[-1] not in 'ДГШ':
            cnt += 1
print(cnt)
'''


# № 20898 Апробация 05.03.25 (Уровень: Базовый)
# Определите количество девятеричных пятизначных чисел,
# в записи которых ровно одна цифра 0,
# при этом никакая нечётная цифра не стоит рядом с цифрой 0.
'''
from itertools import product
cnt = 0
for p in product('012345678', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('0') == 1:
            for x in '13579':
                num = num.replace(x, '*')
            if '*0' not in num and '0*' not in num:
                cnt += 1
print(cnt)
'''

# № 18042 (Уровень: Базовый)
# (Л. Шастин) Ваня составляет 5-буквенные слова, в которых могут быть использованы только буквы Л, Ю, С, Т, Р, А,
# причём буква Ю используется не более двух раз. Также слово не должно оканчиваться согласными буквами.

'''
from itertools import * 
cnt = 0
for p in product("ЛЮСТРА", repeat = 5):
    p = "".join(p)
    if p.count("Ю") <= 2:
        if p[-1] not in "ЛСТР":
            cnt += 1
print(cnt)
'''

# № 14412 (Уровень: Базовый)
# (Л. Шастин) Вася составляет 6-буквенные слова, в которых могут быть
# использованы только буквы А, Л, Г, О, Р, И, Т, М, причём буква Л используется не более одного раза.
# Слово не должно начинаться с буквы Р и оканчиваться согласными буквами.
# Сколько существует таких слов, которые может написать Вася?


'''
from itertools import *
cnt = 0 
for p in product("АЛГОРИТМ", repeat = 6):
    p = "".join(p)
    if p.count("Л") <= 1:
        if p[0] != "Р" and p[-1] not in "ЛГРТМ":
            cnt += 1
print(cnt)
'''

# № 13870 (Уровень: Средний)
# (Л. Шастин) Сколько существует различных пятизначных чисел, записанных в восьмеричной системе счисления,
# в записи которых есть только три одинаковые цифры, причём стоящие рядом?
'''
from itertools import *
num = 0
for p in product("01234567", repeat = 5):
    p = "".join(p)
    if p[0] != '0':
        copied3 = [x for x in p if p.count(x) == 3]
        copied1 = [x for x in p if p.count(x) == 1]
        if len(copied3) == 3 and len(copied1) == 2:
            if copied3[0] * 3 in p:
                num += 1
print(num)
'''

# № 12783 Открытый курс "Слово пацана" (Уровень: Базовый)

# (М. Попков) Какое количество 7-значных чисел в десятичной системе
# счисления вы можете составить? Число можно составить согласно данным правилам:
# 1) Все цифры различны;
# 2) Никакие две четные и две нечетные цифры не стоят рядом.

'''
from itertools import *
cnt = 0
for p in permutations("0123456789", r = 7):
    p = "".join(p)
    if p[0] != "0":
        for x in "02468":
            p = p.replace(x, "*")
        for x in "13579":
            p = p.replace(x, "-")
        if "**" not in p and "--" not in p:
            cnt += 1
print(cnt)
'''



print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(x <= y)) or (z == w) or z
                if F == 0:
                    print(x, y, z, w)




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 8, 9, 14, 17]
# КЕГЭ = []
# на следующем уроке: