# region Домашка: ******************************************************************

# Номер 5
'''
def cnv(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(1, 100):
    a = cnv(n)
    if n % 3 == 0:
        a = a + a[-3:]
    else:
        a = a + cnv((n % 3) * 3)
    e = int(a, 3)
    if e > 150:
        print(n)
        break
'''


# Номер 13
'''
from ipaddress import *
for mask in range(33):
    net = ip_network(f'111.118.179.50/{mask}', 0)
    print(net, mask, 32-mask, net.netmask)
    # if '111.118.178.0' in str(net):
    #     print(net, net.netmask)  # 255.255.254.0
'''

'''
from ipaddress import *
for m in range(33):
    net = ip_network(f'111.118.179.50/{m}', 0)
    if '111.118.178.0' in str(net):
        mask = '1' * m + '0' * (32 - m)
        mask = mask[16:24]
        print(int(mask, 2))
        
        
        print(int(('1'*m)[16:]+'0', 2))
'''

# Номер 12
'''
for n in range(4, 10000):
    a = '5' + '2'*n
    while '52' in a or '1122' in a or '2222' in a:
        if '52' in a:
            a = a.replace('52', '11', 1)
        if '2222' in a:
            a = a.replace('2222', '5', 1)
        if '1122' in a:
            a = a.replace('1122', '25', 1)

    b = 0
    for i in range(len(a)):
        b += int(a[i])

    b = sum(map(int, a))
    
    b = sum([int(x) for x in a])
    
    if b == 64:
        print(n)
        break
'''

# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(uncopied) == 3 and len(copied2) == 4:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''

# Номер 17
'''
s = [int(x) for x in open('0. files/17.txt')]
end_29 = [x for x in s if abs(x) % 100 == 29]
len_5 = [x for x in s if len(str(abs(x))) == 5]
R = []
for i in range(len(s)-2):
    x, y, z = s[i:i+3]
    if (x in len_5) + (y in len_5) + (z in len_5) == 2:
        if (x + y + z) < max(end_29):
            R.append(x + y + z)
print(len(R), max(R))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo разобрать задачку Тип 24 №59847
'''
s = open('0. files/24.txt').readline()
s = s.replace('WW', ' ')
s = s.split()
maxi = 0
for i in range(len(s)-100):
    r = 'W' + 'WW'.join(s[i:i+101]) + 'W'
    maxi = max(maxi, len(r))
print(maxi)
'''

# зацепка может быть тут https://inf-ege.sdamgia.ru/problem?id=59729
# В строке TTTT пара символов встречается ровно 3 раза.

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 4, 5, 8, 9, 12, 13, 14, 15, 16, 17, 18, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Дима 4/9 -> 27 вторичных баллов +[1, 12, 14, 16] -[5, 8, 13, 23, 25]
# Максим 11/14 -> 54 вторичных баллов +[1, 2, 3, 4, 5, 8, 13, 14, 16, 23, 25] -[7, 11, 12]

# Второй пробник 28.02.25:
# Дима 10/29 -> 51 вторичных баллов +[1, 4, 7, 8, 13-16, 23, 25] -[5, 9, 12, 17]
# Максим 16/29 -> 67 вторичных баллов +[1-4, 6, 8, 9, 11, 12, 14-17, 19, 23, 25] -[5, 7, 13, 18]