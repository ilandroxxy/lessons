# region Домашка: ******************************************************************

# № 1933 (Уровень: Базовый)
'''
from itertools import permutations
R = []
for p in permutations('КЛАБХАУС', r=8):
    word = ''.join(p)
    if 'АА' not in word:
        R.append(word)
print(len(set(R)))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 23764 Демоверсия 2026 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# – символ «?» означает ровно одну произвольную цифру;
# – символ «*» означает любую последовательность цифр
# произвольной длины; в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа,
# соответствующие маске 3?12?14*5, делящиеся на 1917 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа
# в порядке возрастания, а во втором столбце – соответствующие им
# результаты деления этих чисел на 1917.
'''
from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)


from re import *
for x in range(1917, 10**10, 1917):
    if fullmatch('3[0-9]12[0-9]14[0-9]*5', str(x)):
        print(x, x // 1917)
'''


# Универсальная функция поиска делителей числа:
'''
import time
start = time.time()

# Плохая функция поиска делителей (медленная)
# def divisors(n):
#     d = []
#     for j in range(1, n+1):
#         if n % j == 0:
#             d.append(j)
#     return d

def divisors(n):
    d = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(300_000_000))  #

end = time.time()
print(end - start)  # 5.52384 -> 0.0007
'''


# № 23763 Демоверсия 2026 (Уровень: Базовый)
'''
def divisors(n):
    d = []
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа.
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

cnt = 0
for n in range(800_000+1, 10**10):
    d = divisors(n)
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 10 == 4:
            print(n, M)
            cnt += 1
            if cnt == 5:
                break
'''


# № 20144 (Уровень: Средний)
'''
def divisors(n):
    d = []
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа.
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

cnt = 0
for n in range(3_333_337+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) >= 2:
        R = max(d) - min(d)
        if R > 1000 and R % 3 == 0:
            print(n, R)
            cnt += 1
            if cnt == 5:
                break
'''


# № 19778 (Уровень: Средний)
'''
def divisors(n):
    d = []
    for j in range(2, int(n**0.5)+1):  # не считая единицы и самого числа.
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

cnt = 0
for n in range(9_500_000+1, 10**10):
    d = [j for j in divisors(n) if len(divisors(j)) == 0]
    if len(d) > 0:
        F = int(sum(d) / len(d))
        if F != 0 and F % 813 == 0:
            print(n, F)
            cnt += 1
            if cnt == 5:
                break
'''




# № 21422 Досрочная волна 2025 (Уровень: Базовый)
'''
def divisors(n):
    d = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

cnt = 0
for n in range(1_125_000+1, 10**10):
    d = [j for j in divisors(n) if j % 10 == 7 and j != 7 and j != n]
    if len(d) > 0:
        print(n, min(d))
        cnt += 1
        if cnt == 5:
            break
'''


# № 23382 Резервный день 19.06.25 (Уровень: Средний)
'''
def is_prime(n):
    d = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))


def divisors(n):
    d = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            if len(is_prime(j)) == 2 and len(is_prime(n // j)) == 2:
                if str(j).count('2') == 1 and str(n // j).count('2') == 1:
                    d.append(j)
                    d.append(n // j)
    return sorted(d)

cnt = 0
for n in range(6_651_220+1, 10**10):
    d = divisors(n)
    if len(d) >= 2:
        print(n, max(d))
        cnt += 1
        if cnt == 5:
            break
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 8, 14, 15, 16, 23, 19-21, 25]
# КЕГЭ = []
# на следующем уроке:
