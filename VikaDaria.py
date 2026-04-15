# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


'''
from functools import *

@lru_cache(None)
def F(n):
    if n >= 14:
        return n * F(n - 1)
    if n < 14:
        return 8 * G(n - 3)

@lru_cache(None)
def G(n):
    if n < 31:
        return 4
    if n >= 31:
        return n / 2 * G(n - 2)

for n in range(0, 650000):
    G(n)

for n in range(0, 330000):
    F(n)

print(F(320726) / G(641450))
'''


# № 23282 Основная волна 11.06.25 (Уровень: Средний)
# Пусть М - сумма минимального и максимального простых натуральных делителей целого
# числа, не считая самого числа. Если таких делителей у числа нет, то значение М считается равным нулю.
# Напишите программу, которая перебирает целые числа, большие 5 400 000, в порядке
# возрастания и ищет среди них такие, для которых М больше 60 000 и является палиндромом,
# т.е. одинаково читается слева направо и справа налево. В ответе запишите в первом столбце
# таблицы первые  пять найденных чисел в порядке возрастания, а во втором столбце - соответствующие им значения М.
'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

cnt = 0
for n in range(5_400_000+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) >= 2:
        M = min(d) + max(d)
        if M > 60000 and str(M) == str(M)[::-1]:
            print(n, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 23382 Резервный день 19.06.25 (Уровень: Средний)
# Напишите программу, которая перебирает целые числа,
# большие 6 651 220, в порядке возрастания и ищет среди них числа,
# представленные в виде произведения ровно двух простых множителей,
# не обязательно различных, каждый из которых содержит в своей записи ровно одну цифру 2.
# В ответе в первом столбце таблицы запишите первые 5 найденных чисел
# в порядке возрастания, а во втором столбце - для каждого из чисел
# соответствующий им наибольший из найденных множителей.
'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

cnt = 0
from itertools import product
for n in range(6_651_220+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        if any(p[0] * p[1] == n and str(p[0]).count('2') == 1 and str(p[1]).count('2') == 1 for p in product(d, repeat=2)):
            print(n, max(d))
            cnt += 1
            if cnt == 5:
                break
'''

# № 28711 (Уровень: Базовый)
# Напишите программу, которая перебирает целые числа, большие 2 400 000,
# в порядке возрастания и ищет среди них числа, представимые в виде произведения
# ровно трёх различных простых множителей, каждый из которых содержит в своей записи
# хотя бы одну цифру 4 или 7. В ответе запишите первые пять чисел в порядке возрастания,
# справа от каждого числа запишите его наибольший простой делитель.
'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

def res(x):
    if str(x).count('4') + str(x).count('7') >= 1:
        return True
    else:
        return False

cnt = 0
from itertools import permutations
for n in range(2_400_000+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        if any(p[0] * p[1] * p[2] == n and res(p[0]) and res(p[1]) and res(p[2]) for p in permutations(d, r=3)):
            print(n, max(d))
            cnt += 1
            if cnt == 5:
                break
'''


# № 23569 Пересдача 03.07.25 (Уровень: Средний)
'''
def divisors(n):
    d = []
    for j in range(2, int(n**0.5)+1):
        if n%j == 0:
            d += [j, n//j]
    return sorted(set(d))

cnt = 0
from itertools import product
for n in range(6_086_055, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        if any(p[0] * p[1] == n and str(p[0]).count('6') == 1 and str(p[1]).count('6') == 1 for p in product(d, repeat=2)):
            print(n, max(d))
            cnt +=1
            if cnt == 5:
                break
'''


# № 24166 (Уровень: Средний)
# (Е. Ширшев) Напишите программу, которая перебирает целые числа, большие 7 305 678,
# в порядке возрастания и ищет среди них числа, представленные в виде произведения
# ровно четырех простых множителей, не обязательно различных, сумма которых является числом палиндромом.
# В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке возрастания,
# а во втором столбце - для каждого из чисел соответствующую ему сумму множителей.
'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

def pal(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False

cnt = 0
from itertools import product
for n in range(7305679+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        for p in product(d, repeat=4):
            if p[0] * p[1] * p[2] * p[3] == n and pal(p[0]+p[1]+p[2]+p[3]):
                print(n, p[0]+p[1]+p[2]+p[3])
                cnt += 1
                break
        if cnt == 5:
            break
'''


#
# № 28710 (Уровень: Базовый)
'''
def divisors(n):
    m = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            m += [j, n // j]
    return sorted(set(m))


def res(x):
    if '3' in str(x) and '5' in str(x):
        return True
    else:
        return False

cnt = 0
from itertools import product
for n in range(4_080_000 + 1, 10 ** 10):
    m = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(m) > 0:
        if any(p[0] * p[1] * p[2] == n and res(p[0]) and res(p[1]) and res(p[2]) for p in product(m, repeat=3)):
            print(n, max(m))
            cnt += 1
            if cnt == 5:
                break

'''

'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

def res(x):
    if str(x).count('3') >= 1 and str(x).count('5') >= 1:
        return True
    else:
        return False

cnt = 0
from itertools import product
for n in range(4_080_000+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        if any(p[0] * p[1] * p[2] == n and res(p[0]) and res(p[1]) and res(p[2]) for p in product(d, repeat=3)):
            print(n, max(d))
            cnt += 1
            if cnt == 5:
                break
'''


# № 28709 (Уровень: Базовый)
'''
def divisors(n):
    m = []
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            m += [j, n // j]
    return sorted(set(m))


def res(x):
    if str(x).count('3')>=1 or str(x).count('4')>=1:
        return True
    else:
        return False


cnt = 0
from itertools import product
for n in range(6_300_000 + 1, 10 ** 10):
    m = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(m)>0:
        if any(p[0] * p[1] * p[2] == n and res(p[0]) and res(p[1]) and res(p[2]) for p in product(m, repeat=3)):
            print(n, max(m))
            cnt += 1
            if cnt == 5:
                break
'''


# № 26685 (Уровень: Средний)
#  (К. Багдасарян) Напишите программу, которая перебирает целые числа, большие 2 700 000,
#  в порядке возрастания и ищет среди них числа, оканчивающиеся на 34, представленные
#  в виде произведения простых множителей, среди которых найдется число, повторяющееся
#  не менее 5 раз. В ответе запишите в первом столбце таблицы первые пять найденных
#  чисел в порядке возрастания, а во втором столбце – наименьший сомножитель, который повторяется не менее 5 раз.
'''
def divisors(n):
    d = []
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            d += [j, n // j]
    return sorted(set(d))

c = 0
for n in range(2700001, 10 ** 10):
    if n % 100 == 34:
        d = len([j for j in divisors(n) if len(divisors(j)) == 0])
        if len(d)>1:
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 16, 25]
# на следующем уроке:


# region 📖 Пробник (Вариант 2)

# Студент #Дарья
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27
# ⛔️ Неверно: 3, 6, 7, 10, 24, 26
# ❔ Без ответа: Нет
# Итог: 22/29 первичных балла ~ 83 вторичных

# Студент #Маша
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 21, 23
# ⛔️ Неверно: 10, 18
# ❔ Без ответа: 9, 17, 22, 24, 25, 26, 27
# Итог: 18/29 первичных балла ~ 72 вторичных

# Студент #Вика
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 6, 7, 8, 13, 14, 16, 17, 19, 20, 21, 25, 27
# ⛔️ Неверно: 5, 9, 12, 15, 23
# ❔ Без ответа: 3, 4, 10, 11, 18, 22, 24, 26
# Итог: 15/29 первичных балла ~ 65 вторичных

# endregion 📖 Пробник (Вариант 2)

