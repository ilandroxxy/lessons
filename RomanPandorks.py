# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/inf/task/6c7fa5a4-f36b-4599-bac5-09a8e7b2b360
# Сеть задана IP-адресом одного из входящих неё узлов 190.202.83.62
# и сетевой маской 255.255.252.0.
#
# Найдите наибольший и наименьший IP-адрес в данной сети, который
# может быть назначен компьютеру.
# В ответе укажите сумму числовых значений октетов найденных IP-адресов.
'''
from ipaddress import *
net = ip_network('190.202.83.62/255.255.252.0', 0)
for ip in net:
    print(ip)

# 190.202.80.1
# 190.202.83.254

print(190 + 202 + 80 + 1 + 190 + 202 + 83 + 254)
'''
# 22, 17, 15, 13



# https://education.yandex.ru/ege/inf/task/2f051464-92d4-4df3-a837-b8939edd9174
'''
from ipaddress import *
net = ip_network('192.168.0.0/255.255.192.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('1') > ip2.count('0'):
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/bb30cfa6-5991-411e-b2df-dc6d007aec69
'''
from ipaddress import *
net = ip_network('235.86.56.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    # if ip2[-2] == '1' and ip2[-1] == '1':
    if ip2[-2:] == '11':
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/380757d9-1361-41c9-b23d-f25fc5439be8
'''
cnt = 0
from ipaddress import *
net = ip_network('172.30.0.0/255.254.0.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 12 != 0:
        cnt+=1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/d3bde6f0-4eae-4994-bb5d-f757607b9d5f
'''
from ipaddress import*
net = ip_network("87.226.26.72/255.255.255.252", 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count("0") % 2 == 0:
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/4c127bff-f349-43b8-a4f4-d778197a9167
'''
cnt = 0
from ipaddress import *
net=ip_network('192.168.63.0/255.255.255.128')
for ip in net:
    if f'{ip:b}'.count('0')%5!=0:
        cnt+=1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/4cb38e00-cf16-4ae7-bf88-9a33e46ff749
'''
from ipaddress import *
net = ip_network("123.222.99.192/255.255.255.248", 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count("0") < ip2.count("1"):
        cnt += 1
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/311278cb-12ec-4f14-bde6-571d7045cc02
# Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0.
# Чему равно наименьшее возможное значение третьего слева байта маски?
# Ответ запишите в виде десятичного числа.
'''
from ipaddress import *
for mask in range(0, 32+1):
    net = ip_network(f'111.81.208.27/{mask}', 0)
    if '111.81.192.0' in str(net):
        print(net.netmask)
        # 255.255.192.0
        # 255.255.224.0
'''

## https://education.yandex.ru/ege/inf/task/5892806e-4cce-44f5-8031-b8b7be653bfe
'''
from ipaddress import *
for mask in range(0, 32+1):
    net = ip_network(f'117.191.138.37/{mask}', 0)
    if '117.191.136.0' in str(net):
        print(net.netmask)
'''
# https://education.yandex.ru/ege/inf/task/22742d23-3bdb-4c5e-be06-0c1f7fc59bb8
'''
from ipaddress import *
for mask in range(0, 32+1):
    net = ip_network(f"208.207.230.65/{mask}", 0)
    if '208.207.224.0' in str(net):
        print(net)
 '''




## #https://education.yandex.ru/ege/inf/task/020dbd7f-2c15-4a0c-af2c-fea4ab2b122a
# Обозначим через ДЕЛ(n, m) утверждение «натуральное
# число n делится без остатка на
#натуральное число m».
# Для какого наименьшего натурального числа А формула
# ¬(ДЕЛ(x,3) ∧ ДЕЛ(x,5)) ∨ (A ≥ 42−x)
# тождественно истинна (т. е. принимает значение 1)
# при любом натуральном значении переменной х?
'''
for a in range(1, 10000):
    if all(((not ((x%3==0) and (x%5==0))) or (a >= (42-x))) for x in range(1, 10000)):
        print(a)
        break
'''

# https://education.yandex.ru/ege/inf/task/1e0d34d8-9728-4d55-a0a3-bdbde5927c1d
'''
for a in range(1, 10000):
    if all(((x % a == 0) <= ((not (x % 25 == 0)) or (x % 16 == 0))) for x in range(1, 10000)):
        print(a)
        break
'''

# https://education.yandex.ru/ege/inf/task/f5dc5b2a-ddaf-41fb-93d4-7a698e31cda8
'''
for a in range(10000-1, -1, -1):
    if all((((x>=a) or (121>=x**2)) and ((y**2<49) or (a<y))) for x in range(0, 100) for y in range(0, 100)):
        print(a)
        break
'''
# Пусть на числовой прямой дан отрезок B=[132;150].
# Для какого наименьшего натурального числа А большего 1 логическое выражение
#
# (¬ДЕЛ(x,A)∧(x∈B))→¬ДЕЛ(x,13)
# истинно (т. е. принимает значение 1) при любом целом положительном
# значении переменной х?

'''
for a in range(2, 10000):
    if all((((not (x%a==0)) and (132 <= x <= 150)) <= (not (x%13==0))) for x in range(1, 10000)):
        print(a)
        break
   '''


# https://education.yandex.ru/ege/inf/task/1452a6ee-c08b-4f20-8169-6fe1a281193d
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return (P) <= (((Q) and (not A)) <= (not P))

R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''

# https://education.yandex.ru/ege/inf/task/605fc61c-bfe9-4169-97a7-57abdd43a5e9
# На числовой прямой даны два отрезка: B=[22;40] и C=[32;50].
# Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение
# ¬(x∈A)→((x∈B)≡(x∈C))
# истинно (т. е. принимает значение 1) при любом значении переменной х.
'''
def f(x, a1, a2):
    b = 22 <= x <= 40
    c = 32 <= x <= 50
    a = a1 <= x <= a2
    return (not a)<=((b)==(c))
r = []
m = [x/4 for x in range(15 * 4, 60 * 4)]
for a1 in m:
    for a2 in m:
        if all(f(x, a1, a2) for x in m):
            r.append(a2-a1)
print(min(r))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27.1]
# КЕГЭ = [3, 5, 7, 8, 9, 12, 14, 15, 16, 17, 18, 19-21, 23, 25]
# на следующем уроке: 17


# region 📖 Пробник (Вариант 2)

# Студент #Влад
# Дата: #Четверг #12Марта2026
# ✅ Верно: 1, 2, 3, 4, 10, 14, 16, 18, 19, 20, 21, 23
# ⛔️ Неверно: 6, 7, 8
# ❔ Без ответа: 5, 9, 11, 12, 13, 15, 17, 22, 24, 25, 26, 27
# Итог: 12/29 первичных балла ~ 56 вторичных

# endregion 📖 Пробник (Вариант 2)
