# region Домашка: ******************************************************************

'''
for n in range(3, 10000):
    s = '5' + '2' * n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1 )
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    summa = sum([int(x) for x in s])
    if summa==64:
        print(n)
        break
'''


#5
#На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1) Строится троичная запись числа N.
# 2) Если N кратно 3, то в конец троичной записи числа дописываются три последние цифры троичной записи числа.
# Иначе в конец троичной записи числа дописывается остаток отделения n на 3, умноженный на 3,
# записанный в троичной записи.
# Полученная таким образом запись является троичной записью искомого числа R.
# Укажите минимальное число N, после обработки которого автомат получает число, большее 150.В ответе это число запишите в десятичной системе.
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


L = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n%3==0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 3)

    r = int(s, 3)
    if r > 150:
        L.append(n)
print(min(L))
'''
# Ответ:151


#8
# Нам дан набор, состоящий из букв С, Б, О, Р, Н, И, К. Из данного набора составляют слова
# длиной шесть символов, самое главное – символы могут повторяться. Все слова, которые
# возможно составить, расположили в алфавитном порядке, а наша задача – узнать
# под каким номером находится последнее слово, которое не начинается с буквы Р,
# содержит только две буквы Б и не более одной буквы К.
'''
from itertools import *
nomer = 0
for p in product(sorted('СБОРНИК'), repeat = 6):
    word = ''.join(p)
    nomer += 1
    if word[0]!='Р' and word.count('Б')==2 and word.count('К')<=1:
        print(nomer)
'''
# Ответ: 117601


#15
# Для какого наименьшего целого неотрицательного числа А выражение
# (x < A) ∨ (3y + 2x > 120) ∨ (A > y) тождественно истинно (т.е. принимает значение 1)
# при любых целых неотрицательных х и у
'''
def F(x, y, A):
    return (x < A) or (3 * y + 2 * x > 120) or (A > y)

L = []
for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        L.append(A)
print(min(L))
'''
# Ответ: 25

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 13429 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
from fnmatch import *
for x in range(83, 10**6, 83):
    if fnmatch(str(x), '1*578*'):
        print(x, x // 83)
'''
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''

# 12741 (Уровень: Базовый)
'''
from fnmatch import *
R = []
for x in range(1234, 10**10, 1234):
    if fnmatch(str(x), '4*5*6'):
        if fnmatch(str(x), '?74*68?'):
            R.append([x, x // 1234])

for x in R[::-1]:
    print(*x)
'''

# № 12416 (Уровень: Базовый)

def divisors(n):
    div = []
    for j in range(1, int(n ** 0.5)+1):
        div.append(j)
        div.append(n // j)
    return sorted(set(div))

from fnmatch import *
for x in range(7777, 10**10, 7777):
    if fnmatch(str(x), '12*567?'):
        d = divisors(x)
        if (min(d) + max(d)) % 2 != 0:
            print(x, x // 7777)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Egor 7/10 -> 40 вторичных баллов +[1, 4, 5, 10, 12, 13] -[2, 6, 8]

# Второй пробник 28.02.25:
# Egor 12/16 -> 56 вторичных баллов +[1-4, 6, 7, 11-14, 16, 23] -[5, 8, 10, 15]
