# region Домашка: ******************************************************************

# № 12088
'''
from ipaddress import *
net = ip_network(f'112.154.133.208/255.255.252.0', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s[16:].count('0') % 2 != 0:
        if s[:16].count('1') <= s[16:].count('0'):
            cnt += 1
print(cnt)   # 502

# суммарное количество единиц в левых двух байтах не больше суммарного нечётного количества нулей в правых двух байтах.

#      112.154              133.208
# 01110000.10011010    10000101.11010000
#   s[:8]  s[8:16]     s[16:24]  s[24:]
print(bin(208)[2:].zfill(8))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Тип 25 №48446
# Маска числа — это последовательность цифр,
# в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру, символ «*»
# означает произвольную (в том числе пустую) последовательность цифр.
#
# Найдите все натуральные числа, не превышающие 10**10,
# которые соответствуют маске 1?493*41 и при этом без остатка делятся на 2023.
# В ответе запишите все найденные числа в порядке возрастания.
'''
from fnmatch import *
for x in range(0, 10**10, 2023):
    if fnmatch(str(x), '1?493*41'):
        print(x)

        # 1349341
        # 1249338041
        # 1549348941
        # 1849359841
'''


# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
def prime(n):  # 12
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


from fnmatch import *
for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if prime(x):
            print(x)
            # 311111
            # 361111
            # 3011117
            # 3011119
            # 3311117
            # 3611119
            # 3811117
            # 3911111
'''

'''
import time
start = time.time()

# def divisors(n):  # Скорость: 3.093
#     div = []
#     for j in range(1, n+1):
#         if n % j == 0:
#             div.append(j)
#     return div


def divisors(n):  # 0.000351
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


print(3.093 / 0.000351)  # 8811.96581

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(106_000_000))

print(time.time() - start)
'''


# Тип 25 №33770
'''
def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


for n in range(106_000_000, 107_000_000+1):
    chet = [x for x in divisors(n) if x % 2 == 0]
    if len(chet) == 3:
        print(n)
'''


# Тип 25 №39254
'''
from math import prod

def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


cnt = 0
for n in range(500_000_000+1, 10**10):
    div = divisors(n)
    if len(div) >= 5:
        # M = div[0] * div[1] * div[2] * div[3] * div[4]
        # print(div[:5])
        # print(div[0], div[1], div[2], div[3], div[4])
        M = prod(div[:5])
        if 0 < M < n:
            print(M)
            cnt += 1
            if cnt == 5:
                break
'''


# Тип 25 №27852
'''
def divisors(n):
    div = []
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


for n in range(185_311, 185_330+1):
    div = divisors(n)
    if len(div) == 4:
        print(*div)
 '''

# Тип 25 №33104
# Назовём нетривиальным делителем натурального числа его делитель,
# не равный единице и самому числу. Например, у числа 6 есть два
# нетривиальных делителя: 2 и 3. Найдите все натуральные числа, принадлежащие
# отрезку [289123456; 389123456] и имеющие ровно три нетривиальных делителя.
'''
def divisors(n):
    div = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            div.append(j)
            div.append(n // j)
    return sorted(set(div))


for n in range(289123456, 389123456+1):
    if n ** 0.5 == int(n ** 0.5):  # Если у числа есть целый квадратный корень
        div = divisors(n)
        if len(div) == 3:
            print(n, max(div))
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
