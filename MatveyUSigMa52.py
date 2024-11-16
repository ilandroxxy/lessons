# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038667/step/10?unit=1062772
'''
from itertools import *

r = []
num = 0
for i in product(sorted('ФОКУС'), repeat=5):
    w = ''.join(i)
    num = num + 1
    if 'Ф' not in w and w.count('У') == 2:
        r.append(num)

print(max(r))
'''

# 1. Есть условие про алфавитный порядок, то бишь: sorted('ФОКУС')
# 2. Если буквы повторяются в "слове", то используем: product(s, repeat=5)


# https://stepik.org/lesson/1038667/step/13?unit=1062772
'''
from itertools import *

k = []
for i in permutations('КЛАБХАУС'):
    w = ''.join(i)
    if 'АА' not in w:
        k.append(w)
print(len(set(k)))
'''

'''
from itertools import *

k = 0
for i in product('01234567', repeat=5):
    num = ''.join(i)
    if num[0] not in '013579' and num[-1] not in '26' and num.count('7') <= 2:
        k = k + 1
print(k)
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/0a888798-5892-4b73-9822-6067357d93e3
'''
M = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:] - перевод в 2-ю систему из 10-й
    if n % 2 == 0:
        s += '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)  # Перевод из 2-й в 10-ю
    if r > 156:
        M.append(n)
print(min(M))
'''


# https://education.yandex.ru/ege/task/fef8d85c-6b9d-43d3-954c-6acb16a1f5a9
'''
for n in range(11, 1000):
    s = f'{n:b}'
    if n % 5 == 0:
        s += s[-3:]   # Последние три
    else:
        x = (n % 5) * 5
        s = f'{x:b}' + s
    r = int(s, 2)
    if r > 512:
        print(n)
        break
'''


# https://education.yandex.ru/ege/task/66fb491b-168a-42e5-a671-b20d4487cf41
'''
M = []
for n in range(1, 1000):
    s = f'{n:b}'
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    r = int(s, 2)
    if r > 48:
        M.append(r)
print(min(M))
'''


# https://education.yandex.ru/ege/task/638ac2c9-defe-4ca9-971a-ee65a1774d31
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(1, 10000):
    s = convert(n, 3)
    summa = sum(map(int, s))
    if summa % 2 == 0:
        s = '2' + s[2:] + '0'
    else:
        s = '20' + s[2:] + '1'
    r = int(s, 3)
    if r > 75:
        print(n)
        break
'''


# https://education.yandex.ru/ege/task/9fb60578-88e4-465d-b603-dbf30d312808
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


for n in range(11, 1000):
    s = convert(n, 5)
    if n % 5 == 0:
        s += s[-3:]
    else:
        x = (n % 5) * 5
        s = convert(x, 5) + s
    r = int(s, 5)
    if r > 375:
        print(n)
        break
'''


# https://education.yandex.ru/ege/task/f1fac643-8eea-4ba9-8bb9-85670cd87bdd


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for n in range(1, 1000):
    s = convert(n, 2)
    if n % 2 == 0:
        s = '1' + s + '1'
    else:
        s += '10'
    r = int(s, 2)
    if r > 179:
        print(n)
        break

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
