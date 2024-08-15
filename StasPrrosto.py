# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240', 0)
cnt = 0
for ip in net:
    cnt += 1
    print(cnt, ip)
    # if int(f'{ip:b}') % 2 == 0:
    #     c += 1
'''


# Тип 25 №64955
# Маска числа — это последовательность цифр, в которой могут встречаться специальные
# символы «?» и «*». Символ «?» означает ровно одну произвольную цифру, символ «*» означает
# произвольную (в том числе пустую) последовательность цифр.
#
# Найдите все натуральные числа, не превышающие 10**10, которые соответствуют маске 1*4182?7
# и при этом без остатка делятся на 1991.
#
# В ответе запишите все найденные числа в порядке возрастания.
'''
from fnmatch import *
for x in range(1991, 10**10, 1991):
    if fnmatch(str(x), '1*4182?7'):
        print(x)
'''


'''
from time import time
start = time()

# def divisors(x):
#     div = []
#     for j in range(1, x + 1):
#         if x % j == 0:
#             div.append(j)
#     return div


def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
            # div.append(j)
            # div.append(x // j)
    return sorted(set(div))

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(divisors(16))  # [1, 2, 4, 8, 16]
print(divisors(100_000_000))  # 0.00034

print(time() - start)
'''


# Тип 25 №27852
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(185_311, 185_330+1):
    div = divisors(x)
    if len(div) == 4:
        print(*div)
'''

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


for x in range(45_000_000, 45_100_000 + 1):
    inchet = [i for i in divisors(x) if i % 2 != 0]
    if len(inchet) == 5:
        print(inchet)
'''


# Тип 25 №37130

def divisors(x):
    div = []
    for j in range(2, int(x**0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(600_000 + 1, 10**10):
    div = [j for j in divisors(x) if j != 7 and j % 10 == 7]
    if len(div) > 0:
        print(x, min(div))
        cnt += 1
        if cnt == 5:
            break





# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14]
# КЕГЭ  = []
# на следующем уроке:
