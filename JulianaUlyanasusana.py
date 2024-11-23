# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038432/step/2?unit=1060804
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '11' + s[2:] + '00'
    else:
        s = '10' + s[2:] + '11'

    if s.count('1') % 2 == 0:
        s = '11' + s[2:] + '00'
    else:
        s = '10' + s[2:] + '11'
    r = int(s, 2)
    if n < 100:
        M.append(r)

print(max(M))
'''


# https://stepik.org/lesson/1038432/step/5?unit=1060804
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    s = s + str(s.count('1') % 2)
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 75:
        print(r)
        M.append(r)
print(min(M))
'''


'''
for n in range(1, 1000):
    s = bin(n)[2:]
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    s = '1' + s
    if s.count('1') % 2 != 0:
        s = s + '1'
    else:
        s = s + '0'
    r = int(s, 2)
    if r > 180:
        print(n)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Тип 14 №16043
# Значение арифметического выражения 9**7 + 3**21 - 9
# записали в системе счисления с основанием 3.
# Сколько цифр 2 содержится в этой записи?
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 9**7 + 3**21 - 9
print(convert(n, 3).count('2'))
'''


# Тип 14 №60292
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 3 * 3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
print(convert(n, 25).count('0'))
'''


# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
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
# i                0123456789
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2030+1):
    n = 6**260 + 6**160 + 6**60 - x
    s = convert(n, 6)
    if s.count('0') == 202:
        print(x)
        break
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2030+1):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''


# № 12246 ЕГКР 16.12.23 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 2*729**333 + 2*243**334 - 81**335 + 2 * 27 ** 336 - 2*9**337 - 338
s = convert(n, 9)
print(len(s) - s.count('0'))
'''
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
