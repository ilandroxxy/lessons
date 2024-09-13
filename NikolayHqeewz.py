# region Домашка: ******************************************************************

# КЕГЭ № 10778 (Уровень: Базовый)
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'163.232.136.60/{mask}', 0)
    print(net, mask)
'''


# КЕГЭ № 12922 (Уровень: Базовый)
'''
from ipaddress import *
net = ip_network('136.36.240.16/255.255.255.248', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if '101' not in s:
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 25 №56525
# Маска числа — это последовательность цифр, в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру,
# символ «*» означает произвольную (в том числе пустую) последовательность цифр.
#
# Найдите все натуральные числа, не превышающие 10**10, которые соответствуют маске 1?7246*1
# и при этом без остатка делятся на 4173.
# В ответе запишите все найденные числа в порядке возрастания.
'''
from fnmatch import *
for x in range(4173, 10**10, 4173):
    if fnmatch(str(x), '1?7246*1'):
        print(x)
'''

# № 12741 (Уровень: Базовый)
'''
R = []
from fnmatch import *
for x in range(1234, 10**10, 1234):
    if fnmatch(str(x), '4*5*6') and fnmatch(str(x), '?74*68?'):
        R.append(f'{x} {x // 1234}')
        
R.reverse()
for x in R:
    print(x)
'''

# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
'''
def prime(x):
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


from fnmatch import *
for x in range(10**7):
    if fnmatch(str(x), '3?1111*'):
        if prime(x):
            print(x)
'''
'''
from fnmatch import fnmatch
for x in range(10**10):
    if fnmatch(str(x), '12*34?5'):
        pass
'''

# Идеальная функция для поиска делителей числа
'''
import time
start = time.time()

# def divisors(x):  # 24
#     div = []
#     for j in range(1, x+1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(100_000_000))

print(time.time() - start)  # 3.1233971118927  -> 0.00033
'''


# Тип 25 №37160
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(500_001, 10**10):
    div = [j for j in divisors(x) if j != 8 and j % 10 == 8]
    if len(div) > 0:
        print(x, min(div))
        cnt += 1
        if cnt == 5:
            break
'''


# Тип 25 №39254
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(500_000_000+1, 10**10):
    div = divisors(x)
    if len(div) >= 5:
        M = div[0] * div[1] * div[2] * div[3] * div[4]
        if 0 < M < x:
            print(M)
            cnt += 1
            if cnt == 5:
                break
'''

# Тип 25 №27854
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(110203, 110245+1):
    div = [i for i in divisors(x) if i % 2 == 0]
    if len(div) == 4:
        print(*div)
'''


# Тип 25 №33104

def divisors(x):
    div = []
    if x ** 0.5 == int(x ** 0.5):  # Число имеет целый квадратный корень
        for j in range(2, int(x**0.5)+1):
            if x % j == 0:
                div += [j, x // j]
    return sorted(set(div))


for x in range(289123456, 389123456+1):
    div = divisors(x)
    if len(div) == 3:
        print(x, max(div))

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
