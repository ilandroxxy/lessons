# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038700/step/4?unit=1062785
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


# https://stepik.org/lesson/1038700/step/5?unit=1062785
'''
from ipaddress import *
R = []
for mask in range(33):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        R.append(mask)
print(max(R))
'''

# https://stepik.org/lesson/1038700/step/14?unit=1062785
'''
from ipaddress import *
net = ip_network('192.168.32.160/255.255.255.240', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('0') > 21:
        cnt += 1
print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 11259 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(3226, 10**8, 3226):
    if fnmatch(str(x), '3?99?7*8'):
        print(x, x // 3226)
'''

# № 11254 (Уровень: Базовый)
'''
from fnmatch import *
for x in range(5716, 10**10, 5716):
    if fnmatch(str(x), '56*139?4'):
        print(x, x // 5716)
'''

# № 9710 Danov2307 (Уровень: Средний)
'''
from fnmatch import *
R = []
for x in range(2023, 10**10, 2023):
    summa = sum(map(int, str(x)))
    if len(str(x)) == 10:
        if fnmatch(str(x), '1*1'):
            R.append([summa, x // 2023])
            print(summa, x // 2023)

for elem in sorted(R):
    print(elem)
'''

'''
import time
start = time.time()

# def divisors(x):
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
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))

print(time.time() - start)  # 2.81252 -> 0.00033
'''


# № 13488 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(18782, 18822+1):
    d = [j for j in divisors(x) if j % 2 != 0]
    if len(d) == 3:
        print(*d)
'''

# № 6061 (Уровень: Средний)
'''
def is_prime(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


from fnmatch import *
for x in range(10**7):
    if fnmatch(str(x), '34?8*9'):
        d = [j for j in divisors(x) if len(is_prime(j)) == 0]
        if len(d) > 4:
            print(x, max(d))
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
