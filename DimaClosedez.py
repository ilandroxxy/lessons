# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or (not y)) and (not(y==z)) and (not w)
                if F == 1:
                    print(x,y,z,w)
'''
# x y z w
# 0 0 1 0
# 1 0 1 0
# 1 1 0 0


# Номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''

# Номер 13
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    if '111.118.178.0' in str(net):
        print(net.netmask)
        # 255.255.254.0
'''
# Ответ: 254

'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

for x in range(100_000, 200_000):
    d = divisors(x)
    if sum(d) % 10 == 9:
        print(x, sum(d))
'''

# № 17642 Основная волна 19.06.24 (Уровень: Базовый)

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


k = 0
for x in range(800_000+1, 10**10):
    d = [j for j in divisors(x) if j % 10 == 9 and j != 9 and j != x]
    if len(d) > 0:
        print(x, min(d))
        k += 1
        if k == 5:
            break


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 26.1]
# КЕГЭ  = []
# на следующем уроке: 13, 14, 22

# Второй пробник 28.02.25:
# Дмитрий 14/29 -> 62 вторичных баллов +[1, 3, 4, 5, 8, 9, 12, 15, 16, 17, 23, 18, 19-21] -[13, 14, 22]


