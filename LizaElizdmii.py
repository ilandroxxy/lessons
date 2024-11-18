# region Домашка: ******************************************************************


# https://stepik.org/lesson/1228668/step/8?unit=1242201
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


m = []
for n in range(11, 1000):
    s = convert(n, 3)

    nechet = 0
    chet = 0

    for x in s:
        if x in '13579':
            nechet += 1
        else:
            chet += 1

    if chet > nechet:
        s = '22' + s
    else:
        s = '11' + s

    r = int(s, 3)
    if r > 100:
        m.append(r)
print(min(m))
'''

'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


m = []
for n in range(11, 1000):
    s = convert(n, 3)

    nechet = [x for x in s if x in '13579']
    chet = [x for x in s if x in '02468']

    if len(chet) > len(nechet):
        s = '22' + s
    else:
        s = '11' + s

    r = int(s, 3)
    if r > 100:
        m.append(r)
print(min(m))
'''


# https://stepik.org/lesson/1228668/step/7?unit=1242201

'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


m = []
for n in range(1, 1000):
    s = convert(n, 6)

    if n % 3 == 0:
        s = s + s[:2]
    else:
        k = (n % 3) * 10
        s = s + convert(k, 6)
    r = int(s, 6)
    if r > 680:
        m.append(r)
print(min(m))
'''


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 14 https://education.yandex.ru/ege/task/83d644e9-902c-44d8-a9e5-d7f946811a29
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 7**21 + 49**13 - 7**10
s = convert(n, 7)
print(s.count('6'))
'''


# Задание 14 https://education.yandex.ru/ege/task/39991489-2021-4ee7-96a1-f45152dbfcd2
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(1, 10000):
    n = 9**1942 + 9*6**971 + 214 - x
    s = convert(n, 9)
    if abs(s.count('2') - s.count('8')) == 471:
        print(x)
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


for x in range(2042, 0, -1):
    n = 25**61 + 5**178 - x
    s = convert(n, 5)
    if s.count('0') == 60:
        print(x)
        break
'''


'''
print(int('1000', 2))  # 8
print(int('000001000', 2))  # 8
print(int('10000', 2))  # 16
'''


# Задание 14 https://education.yandex.ru/ege/task/12b3aabc-7777-4808-b29a-29993b289cca
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(convert(n, 25).count('0'))
'''


# Задание 14 https://education.yandex.ru/ege/task/2269ff29-1320-4c26-b127-c149167e1c9a
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
            exit()
'''

L = []
alphabet = sorted('0123456789qwertyuiopasdfghjklzxcvbnm'.upper())
for x in alphabet[:13]:
    A = int(f'537{x}623', 13)
    B = int(f'6{x}35{x}2', 13)
    if (A - B) % 3 == 0:
        L.append(alphabet.index('A'))
print(max(L))


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
