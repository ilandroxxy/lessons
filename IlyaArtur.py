# region Домашка: ******************************************************************

# № 6903 (Уровень: Базовый)
'''
M = []
for i in range(1, 100):
    s = bin(i)[2:]

    for _ in range(2):
        if s.count('1') % 2 == 0:
            s = "11" + s[2:] + '00'
        else:
            s = '10' + s[2:] + '11'

    r = int(s, 2)
    M.append(r)
print(max(M))
'''


#  6779 (Уровень: Базовый)
# https://stepik.org/lesson/1038432/step/3?unit=1060804
'''
M = []
for i in range(1, 1000):
    t = bin(i)[2:]
    if t.count('1') % 2 == 0:
        t = '101' + t[3:] + '0'
    else:
        t = '10' + t[2:] + '11'
    r = int(t, 2)
    if r > 68:
        M.append(i)
print(min(M))
'''


# № 6588 Пробник ИМЦ СПб (Уровень: Средний)
'''
M = []
for i in range(1, 100):
    s = bin(i)[2:]
    s = s.replace('1', '`')
    s = s.replace('0', '1')
    s = s.replace('`', '0')
    s = '1' + s
    if s.count('1') % 2 == 0:
        s += '0'
    else:
        s += '1'
    r = int(s, 2)
    if r > 180:
        M.append(i)
print(min(M))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 14 https://education.yandex.ru/ege/task/fb0fcacf-ba6f-49bc-bf96-3eee0b9d6a01
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 625**90 + 125 ** 120 - 5*25
s = convert(n, 25)
summa = 0
for x in s:
    if alphabet.index(x) % 2 == 0:
        summa += alphabet.index(x)
print(summa)
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 125**10
s = convert(n, 5)
print(s.count('0'))
'''


# Задание 14 https://education.yandex.ru/ege/task/a8903831-c37e-4e0a-8633-b69e0bd7a182
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 5*7776**7 + 4*1296**6 + 3*216 - 7776
s = convert(n, 36)
print(s.count('I') + s.count('U') + s.count('Z'))
print(len([x for x in s if x in 'IUZ']))
'''


# Задание 14 https://education.yandex.ru/ege/task/730369b5-bb1f-4ec1-a50e-7a44f0b0ae09
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(1, 1000):
    n = 27**7 - 3**11 + 36 - x
    s = convert(n, 3)
    # summa = s.count('1') + s.count('2') * 2
    # summa = sum([int(x) for x in s])
    summa = sum(map(int, s))
    if summa == 22:
        print(x)
        break
'''


# Задание 14 https://education.yandex.ru/ege/task/35d1a21d-f415-4666-830a-8028485771a4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2042+1):
    n = 25**61 + 5**178 - x
    s = convert(n, 5)
    if s.count('0') == 60:
        print(x)
'''


# https://education.yandex.ru/ege/task/2269ff29-1320-4c26-b127-c149167e1c9a
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:15]:
    A = int(f'9897{x}21', 15)
    B = int(f'12{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
        break
'''


# https://inf-ege.sdamgia.ru/problem?id=48388
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:12]:
    for y in alphabet[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
            break
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2030+1):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        print(x)

'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2031):
    n = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 5:
        print(x)
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6]
# КЕГЭ  = []
# на следующем уроке:
