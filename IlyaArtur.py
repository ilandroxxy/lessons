# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/ba906ead-d64b-46b6-930b-859ba8de9004
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


cnt = 0
for n in range(1, 1000):
    r = convert(n, 17)
    if r[0] == '3' and r[-1] == 'D':
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/4babe488-42fc-4124-946f-edefedd0d21f
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

summa = 0
cnt = 0
for n in range(95):
    r3 = convert(n, 3)
    r5 = convert(n, 5)
    if r3[-2:] == '21':
        if r5[0] == '3':
            summa += n
            cnt += 1
print(summa)
print(cnt)
'''


# https://education.yandex.ru/ege/task/945d02c3-876e-4bd3-8a57-0e076865e42a
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for x in range(1, 2030+1):
    n = 6**260 + 6**160 + 6**60 - x
    r = convert(n, 6)
    if r.count('0') == 202:
        print(x)
        break
'''


# https://education.yandex.ru/ege/task/1b5ee551-6d66-4c66-b1ae-8169874ee37b
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for x in range(1, 2030+1):
    n = 3 ** 100 - x
    r = convert(n, 3)
    if r.count('0') == 5:
        print(x)
'''


# https://education.yandex.ru/ege/task/e5f6be71-eb11-46e1-8dec-d1d1a4346927
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]

n = 125 ** 10
r = convert(n, 5)
print(r.count('0'))
'''


# https://education.yandex.ru/ege/task/749a92f0-0083-4931-90cf-8c987a48ed9c
'''
R = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:16]:
    for y in alphabet[:16]:
        A = int(f'27A{x}23', 16)
        B = int(f'8{y}E5D2', 16)
        if (A + B) % 5 == 0:
            R.append(int(x, 16) + int(y, 16))
print(max(R))
'''


'''
r = '432890978354'

# summa = r.count('1') + r.count('2') * 2 + r.count('3') * 3

summa = 0
for x in r:
    summa += int(x)


summa = sum([int(x) for x in r])

summa = sum(map(int, r))
print(summa)
'''

'''
R = []
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:15]:
    A = int(f'9897{x}21', 15)
    B = int(f'12{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
