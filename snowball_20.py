
#6903
'''
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    for _ in range(2):
        if r.count('1') % 2 == 0:
            r += '00'
            r = '11' + r[2:]
        else:
            r += '11'
            r = '10' + r[2:]
    r = int(r,2)
    if n < 100:
        ls.append(r)
print(max(ls))
'''

#6779
'''
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '0'
        r = '101' + r[3:]
    else:
        r += '11'
        r = '10' + r[2:]
    r = int(r,2)
    if r > 68:
        ls.append(n)
print(min(ls))
'''


#6588
# Автомат обрабатывает натуральное число N по следующему алгоритму.
# Строится двоичная запись числа N.
# Все значащие цифры инвертируются (‘0’ заменяется на ‘1’, а ‘1’ на ‘0’).
# К полученному результату слева добавляется ‘1’.
# К двоичной записи полученного числа справа дописывается бит четности: ‘1’,
# если количество единиц в двоичной записи нечетно, ‘0’ - если четно.
# Полученное в результате этих операций число переводится в десятичную системусчисления.
# Укажите такое наименьшее число N, для которого результат работы данного
# алгоритма больше числа 180.

'''
for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', '*')
    n2 = n2.replace('1', '0')
    n2 = n2.replace('*', '1')
    n2 = '1' + n2
    if n2.count('1') % 2 != 0:
        n2 += '1'
    else:
        n2 += '0'
    r = int(n2, 2)
    if r > 180:
        print(n)
        break

for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 = n2.replace('0', '*')
    n2 = n2.replace('1', '0')
    n2 = n2.replace('*', '1')
    n2 = '1' + n2
    if n2.count('1') % 2 != 0:
        n2 += '1'
    else:
        n2 += '0'
    r = int(n2, 2)
    if r > 180:
        print(n)
        break
'''

#6903
'''
ls = []
for n in range(1,100):
    r = bin(n)[2:]
    for _ in range(2):
        if r.count('1') % 2 == 0:
            r += '00'
            r = '11' + r[2:]
        else:
            r += '11'
            r = '10' + r[2:]
    r = int(r,2)
    ls.append(r)
print(max(ls))
'''

'''
#17624
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    for _ in range(2):
        r += bin(r.count('1') % 2)[2:]
    r = int(r,2)
    if r > 75:
        ls.append(r)
print(min(ls))


#5111
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '1'
        r = '10' + r[2:]
    else:
        r += '11'
        r = '1' + r[2:]
    r = int(r,2)
    if r >= 100:
        ls.append(n)
print(min(ls))


#1516
ls = set()
for n in range(100,1000):
    r = int(bin(n)[2:].replace('0',''),2)
    ls.add(r)
print(len(ls))


#6885
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        r += bin(r.count('1'))[2:]
    r = int(r,2)
    if r > 190:
        ls.append(n)
print(min(ls))


#17546
ls = []
for n in range(1,13):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r,2)
    ls.append(r)
print(max(ls))





#6884
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    r = int(r,2)
    if r > 225:
        ls.append(r)
print(min(ls))


#1515
for n in range(1000,100000):
    r = (bin(n)[2:])[::-1]
    r = int(r,2)
    if r == 29:
        print(n)
        break


#17518
ls = []
for n in range(1,1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r += '0'
        r = '10' + r[2:]
    else:
        r += '1'
        r = '11' + r[2:]
    r = int(r,2)
    if r > 50:
        ls.append(n)
print(min(ls))
'''



'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

r = convert(10**8, 16)
print(r)  # 5F5E100
print(int(r, 16))  # 100000000
'''

# № 29346 Открытый вариант 2026(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 5 * 1296 ** 2021 - 4 * 216 ** 2022 + 3 * 36**2023 -2 * 6 ** 2024 - 2025
n36 = convert(n, 36)
print(len([x for x in n36 if int(x, 36) % 2 == 0]))
print(len([x for x in n36 if x in alp[::2]]))
'''


# № 31152 Основная волна 19.06.26(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 2030+1):
    n = 7 ** 170 + 7 ** 100 - x
    n7 = convert(n, 7)
    if n7.count('0') == 70:
        print(x)
'''


# № 28760 Досрочная волна 2026(Уровень: Базовый)
# Значение арифметического выражения: 2 * 2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561
# записали в системе счисления с основанием 27.
# Определите в 27-ричной записи числа количество цифр с чётным числовым значением, превышающим 9.
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


a = convert(2 * 2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561,27)
print(len([x for x in a if int(x, 27) % 2 == 0 and x > '9']))
print(len([x for x in a if x in alp[::2] and x > '9']))
'''

# № 27626 Апробация 04.03.26(Уровень: Базовый)
# Значение арифметического выражения 6** 2030 + 6 ** 100 - х,
# где х - целое положительное число, не превышающее 2030, записали в 6-ричной системе счисления.
# Определите наименьшее количество нулей, которое может содержаться в этой записи.
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


ls = []
for x in range(1, 2030):
    a = convert(6 ** 2030 + 6 ** 100 - x, 6)
    ls.append(a.count('0'))
print(min(ls))
'''

# № 24629 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

a = convert(14 ** 1402 + 28 ** 501 - 14 ** 51 - 1400, 14)
print(a.count('C'))
'''


# № 31511 Демоверсия 2027(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:22]:
    A = int(f'27{x}98876', 22)
    B = int(f'26{x}51', 22)
    C = int(f'711{x}5', 22)
    if (A + B + C) % 21 == 0:
        print((A + B + C) // 21)
        # 276296118
'''


# № 31222 Резерв 22.06.26(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    a = int(f'76{x}79645', 19) + int(f'35{x}42',19) + int(f'332{x}6',19)
    if a % 18 == 0:
        print(a//18)
'''



# № 29968 Апробация 14.05.26(Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


ls = []
for x in range(1, 3000):
    a = convert(9 * 11 ** 210 + 8 * 11 ** 150 - x,11)
    if a.count('0') == 60:
        ls.append(x)
print(max(ls))
'''



# № 22426 (Уровень: Базовый)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

a = convert(15 * 343**2031 + 7*49**1142 - 3 * 7 ** 111 + 7**222 - 16809,7)
n1 = [x for x in a if x in alp[::2]]
n2 = [x for x in a if x not in alp[::2]]
print(abs(len(n1)-len(n2)))

