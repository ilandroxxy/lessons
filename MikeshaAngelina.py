# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
f = open('9.csv')
c = 0
for s in f:
    z = [int(i) for i in s.split(';')]
    d = [z.count(i) for i in z]

    p = [i for i in z if z.count(i) > 1]
    np = [i for i in z if z.count(i) == 1]

    u1 = d.count(2) == 2 and d.count(1) == 5

    # print(z,d,p,np,u1)
    if u1:
        if (sum(p) / len(p)) < (sum(np) / len(np)):
            c += 1
print(c)


f = open('17.txt')
z = [int(i) for i in f]

a5 = [i for i in z if len(str(abs(i))) == 5]
maxi = max([i for i in z if abs(i) % 100 == 29])
ans = []
for i in range(len(z) - 2):
    a, b, c = z[i:i + 3]
    u1 = (a in a5) + (b in a5) + (c in a5) == 2
    u2 = a + b + c <= maxi
    if u1 and u2:
        ans += [a + b + c]

print(len(ans), max(ans))
'''


'''
# Открытие и чтение файла 17 номера
M = [int(x) for x in open('0. files/17.txt')]
R = []  # сюда будем складывать результат

# Три прототипа 17 номера:
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]

# 3. Под парой подразумевается два различных элемента
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''


# № 19249 ЕГКР 21.12.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5 and abs(x) % 100 == 43]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) >= 1:
        if (x**2 + y**2 + z**2) <= max(A)**2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''


# № 19749 (Уровень: Средний)
'''
M = [int(x) for x in open('0. files/17.txt')]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x % 3 == min(M) % 3) + (y % 3 == min(M) % 3) + (z % 3 == min(M) % 3) == 1:
        if (x % 7 == max(M) % 7) + (y % 7 == max(M) % 7) + (z % 7 == max(M) % 7) >= 2:
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 18045 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if ((abs(x) % 10) + (abs(y) % 10)) == len(A):
        R.append(x + y)
print(len(R), min(R))
'''

# двоичная запись маски, нам нужно взять 3 байт
# mask[:8] mask[8:16] mask[16:24] mask[24:]
'''
n = 10**8
print(bin(n)[2:])
print(f'{n:b}')

print(oct(n)[2:])
print(f'{n:o}')

print(hex(n)[2:])  # 5f5e100
print(f'{n:x}')  # 5f5e100
print(f'{n:X}')  # 5F5E100
'''

# № 20902 Апробация 05.03.25 (Уровень: Базовый)
# Сеть задана IP-адресом 172.16.80.0 и маской сети 255.255.248.0.
# Сколько в этой сети IP-адресов, для которых количество
# единиц в двоичной записи IP-адреса не кратно 2?
'''
from ipaddress import *
net = ip_network('172.16.80.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    # print(bin(int(ip))[2:], f'{ip:b}')
    b = f'{ip:b}'  # двоичная запись ip
    if b.count('1') % 2 != 0:
        cnt += 1
print(cnt)
'''
# print(net)  # 172.16.80.0/21, где 21 - это кол-во единиц в двоичной записи маски сети
# print(net.network_address)


# № 18159 (Уровень: Базовый)
# Для узла с IP-адресом 205.154.212.20 адрес сети
# равен 205.154.192.0. Чему равно наибольшее возможное
# значение третьего слева байта маски?
# Ответ запишите в виде десятичного числа.

'''
from ipaddress import *
for mask in range(0, 32+1):
    net = ip_network(f'205.154.212.20/{mask}', 0)
    if '205.154.192.0' in str(net):
        print(net, net.netmask)
        # 205.154.192.0/18 255.255.192.0
        # 205.154.192.0/19 255.255.224.0
'''
# Ответ: 224


# № 19748 (Уровень: Средний)
# Узлы с IP-адресами 157.220.185.237 и 157.220.184.230
# принадлежат одной сети.
# Какое наименьшее количество IP-адресов, в двоичной
# записи которых ровно 15 единиц, может содержаться в этой сети?
'''
from ipaddress import *
for mask in range(10, 32+1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            b = f'{ip:b}'
            if b.count('1') == 15:
                cnt += 1
        print(mask, cnt)
'''

# № 18487 (Уровень: Средний)
# Сеть, в которой содержится узел с IP-адресом 192.214.A.184,
# задана маской сети 255.255.255.224, где A - некоторое допустимое
# для записи IP-адреса число. Определите минимальное значение A,
# для которого для всех IP-адресов этой сети в двоичной записи
# IP-адреса суммарное количество единиц будет больше 15.
# В ответе укажите только число.
'''
from ipaddress import *
for A in range(0, 255+1):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    if all(f'{ip:b}'.count('1') > 15 for ip in net):
        print(A)
        break
'''

def go(x):
    return {x + 1, x + 5, x * 4}


game = {x for x in range(1, 5000) if x < 473}
gameover = {x for x in range(1, 5000) if x >= 473}

w1 = {x for x in game if go(x) & gameover}
game -= w1

l1 = {x for x in game if go(x) <= w1}
game -= l1

w2 = {x for x in game if go(x) & l1}
game -= w2

l2 = {x for x in game if go(x) <= (w1 | w2)}
game -= l2

print(min(l1))  # 19
print(sorted(w2)[0], sorted(w2)[1])  # 20
print(min(l2))  # 21


def F(s, n):
    if s >= 51:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 51) if F(s, 2)])
print([s for s in range(1, 51) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 51) if F(s, 4) and not F(s, 2)])

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [22, 25]
# КЕГЭ  = []
# на следующем уроке: 8, 9, 11, 17, 19-21

# Первый пробник 5.02.25:
# Ангелина 11/29 -> 54 вторичных баллов +[1-5, 7, 14-16, 20-21] -[6, 8, 9, 10, 11, 12, 13, 17, 18, 19, 22, 23, 25]
# Сергей 16/29 -> 67 вторичных баллов +[1-6, 10, 12, 14, 15, 16, 19-21, 23, 24] -[7, 8, 9, 11, 13, 17, 18, 22, 25]

# Второй пробник 28.02.25:
# Ангелина 10/29 -> 51 вторичных баллов +[2, 3, 4, 7, 9, 10, 14, 18, 23, 25] -[1, 5, 6, 8, 12, 11, 13, 15, 17]
# Сергей 16/29 -> 67 вторичных баллов +[1, 2, 5, 6, 8, 11, 13-18, 19-21, 23, 25] -[3, 4, 7, 9, 10, 12, 22, 24]
