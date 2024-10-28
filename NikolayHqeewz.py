# region Домашка: ******************************************************************

#  № 8954 (Уровень: Базовый
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if abs(x) % 13 == 0 or abs(y) % 13 == 0:
            if abs(x - y) % 36 == 0:
                R.append(x - y)
print(len(R), max(R))
'''


# № 7718 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if ((x * y) % 18 == 0) != ((x + y) % 18 == 0):
            R.append(x + y)
print(len(R), max(R))
'''


# № 8954 (Уровень: Базовый)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if f'{x:X}'[-2:] == '0F']
# A = [x for x in M if hex(x)[-2:] == '0f']
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (abs(x) % 7 == 0) != (abs(y) % 7 == 0):
        if (x + y) % max(D) == 0:
            R.append(x + y)
print(len(R), max(R))
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 18176 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
D = [x for x in M if x > 0 and x % 10 == 4]
R = []
for i in range(len(M)-2):
    # x, y, z = M[i], M[i+1], M[i+2]
    x, y, z = M[i:i+3]
    S = ''.join([str(p) for p in (x, y, z)])
    summa = sum(int(x) for x in S if x.isdigit())
    if summa == min(D):
        R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 11 180738


# 13830 (Уровень: Средний)
'''
def F(a, b, c):
    if a >= b:
        return a == b and c[-1] in 'AC'  # c[-1] !+ 'B'
    return F(a+2, b, c+'A') + F(a+3, b, c+'B') + F(a*2, b, c+'C')


print(F(3, 20, ''))
'''


# № 12779 (Уровень: Средний)
'''
def F(n, x):
    if n >= 3000:
        return n
    if n < 3000:
        return n + x + F(n + 2, x)


for x in range(-100, 100):
    if F(2984, x) - F(2988, x) == 5916:
        print(x)
'''


# № 13910 (Уровень: Базовый)
# ValueError: int() base must be >= 2 and <= 36, or 0

'''
from string import *
alphabet = digits + ascii_uppercase

for i in range(len(alphabet)):
    print(i, alphabet[i])
    # 25 P
    # 26 Q
    # 27 R
    # 28 S
    # 29 T
    # 30 U
'''
'''
for p in range(31, 36+1):
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)
'''

# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase

for p in range(10, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x+y+y, p))
'''


# № 12467 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
# Адрес сети равен 183.192.A.0, где А — некоторое допустимое
# для записи адреса сети число, а маска сети 255.255.252.0.
#
# Определите минимальное значение А, для которого для всех IP-адресов
# этой сети в двоичной записи IP-адреса суммарное количество единиц
# в правых двух байтах больше трёх.
'''
from ipaddress import *
for A in range(0, 255+1):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        break
'''
# 11111111_2 -> 255_10

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
