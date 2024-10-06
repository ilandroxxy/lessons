# region Домашка: ******************************************************************

'''
from time import time
start = time()

# def IsPrime(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

def IsPrime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True


R = []
for n in range(124_000_000, 124_000_010):
    if IsPrime(n):
        R.append(n)
print(R)

print(time() - start)  # 4.900 -> 0.0003499
'''


# № 5736 (Уровень: Средний) 🌶
# (Д. Тараскин) Программа перебирает числа больше 10**9
# и выбирает из них числа-палиндромы, у которых наибольший
# делитель (отличный от 1 и самого числа) кратен 7.
# Выведите первые 5 чисел, которые выберет программа,
# и для каждого числа выведите наибольший делитель.
'''
def Divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):  # отличный от 1 и самого числа
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(10**9+1, 10**10):
    if str(x) == str(x)[::-1]:  # числа-палиндромы
        d = Divisors(x)
        if max(d) % 7 == 0:
            print(x, max(d))
            cnt += 1
            if cnt == 5:
                break
'''

'''
def divisors(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(600000+1, 620000):
    if x % 6 == 0 and len(divisors((x - 1))) == 2 and len(divisors((x + 1))) == 2:
        print(x - 1, x + 1)
        cnt += 1
        if cnt == 6:
            break
'''

'''
def IsPrime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True



cnt = 0
for x in range(600000+1, 620000):
    if x % 6 == 0 and IsPrime(x - 1) and IsPrime(x + 1):
        print(x - 1, x + 1)
        cnt += 1
        if cnt == 6:
            break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 16 №5810
# Алгоритм вычисления значения функции F(n),
# где n — натуральное число, задан следующими соотношениями:
# F(n)=n при n ≤ 2;
# F(n)=F(n− 1)+3·F(n − 2) при n > 2.
# Чему равно значение функции F(6)? В ответе запишите только натуральное число.
'''
def F(n):
    if n <= 2:
        return n
    if n > 2:
        return F(n - 1) + 3*F(n - 2)


print(F(6))
'''


# Тип 16 №59694
# Алгоритм вычисления значения функции F(n),
# где n — натуральное число, задан следующими соотношениями:
# F(n)=n, при n<11;
# F(n)=n+F(n−1), если n≥11.
# Чему равно значение выражения F(2024)−F(2021)?
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n < 11:
        return n
    if n >= 11:
        return n + F(n-1)


print(F(2024) - F(2021))  # 6069
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# F(2024) = 2024 + F(2023)
# F(2023) = 2023 + F(2022)
# F(2022) = 2022 + F(2021) - F(2021)

print(2024 + 2023 + 2022)  # 6069
'''


# Тип 16 №35474
# F(0)=0;
# F(n)=F(n / 3), если n > 0 и при этом mod(n, 3)=0;
# F(n)=mod(n, 3)+F(n − mod(n, 3)), если mod(n, 3) > 0.
#
# Назовите минимальное значение n, для которого F(n)=11.
'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return F(n / 3)
    if n % 3 > 0:
        return (n % 3) + F(n - (n % 3))


for n in range(1, 1000):
    if F(n) == 11:
        print(n)
        break
'''


# Тип 16 №4656
# Алгоритм вычисления значения функции F(n) и G(n),
# где n — натуральное число, задан следующими соотношениями:
# F(1)=0;
# F(n)=F(n – 1)+n при n > 1;
# G(1)=1;
# G(n)=G(n – 1)·n при n > 1.
#
# Чему равно значение функции F(5)+G(5)?
# В ответе запишите только натуральное число.
'''
def F(n):
    if n == 1:
        return 0
    if n > 1:
        return F(n - 1) + n

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return G(n - 1) * n


print(F(5)+G(5))
'''


# Тип 16 №58228
'''
def F(n):
    if n == 1:
        return 1
    if n== 2:
        return 2
    if n > 2 and n % 2 == 0:
        return (4*n - F(n-3)) // 8
    if n > 2 and n % 2 != 0:
        return (4*n - F(n-1) + F(n-2)) // 8


print(F(52) - F(38))
'''


# Тип 16 №58220
'''
def F(n):
    if n < 3:
        return 1
    if n > 2:
        return sum([F(i) for i in range(1, n-1)])

print(F(18))
'''


# № 17679 Пересдача 04.07.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * F(n - 1)


print((F(2024) // 7 - F(2023)) / F(2022))
'''
#            ~~^~~
# OverflowError: integer division result too large for a float

# № 8953 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(100000)


def F(n):
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return F(n + 3) + 7
    if n < 10000 and n % 2 != 0:
        return F(n + 1) - 3


print(F(50) - F(57))
'''


# № 17557 Основная волна 08.06.24 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10000)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)


print((f(2024) // 16 - f(2023)) // f(2022))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 16, 25]
# КЕГЭ  = []
# на следующем уроке:
