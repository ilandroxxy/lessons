# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Переводы в системы счисления
'''
n = 125
print(bin(n))  # 0b1111101 - Двоичная система счисления
print(oct(n))  # 0o175 - Восьмеричная система счисления
print(hex(n))  # 0x7d - Шестнадцетиричная система счисления

print(bin(n)[2:])  # 1111101 - Двоичная система счисления
print(oct(n)[2:])  # 175 - Восьмеричная система счисления
print(hex(n)[2:])  # 7d - Шестнадцетиричная система счисления

print(f'{n:b}')  # 1111101 - Двоичная система счисления
print(f'{n:o}')  # 175 - Восьмеричная система счисления
print(f'{n:x}')  # 7d - Шестнадцетиричная система счисления

# Функция обратного перевода
print(int('1111101', 2))  # 125
print(int('175', 8))  # 125
print(int('7d', 16))  # 125

# print(int('289478932', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0
'''


# Шпаргалка: универсальная функция перевода в b-ю систему счисления
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


print(convert(8, 2))  # 1000
'''


# Задание 5 https://education.yandex.ru/ege/task/f831cc07-c244-4635-9989-adcb36a54e26
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 10000):
    s = convert(n, 7)
    if n % 7 == 0:
        s = s + s[-2:]
    else:
        x = (n % 7) * 2
        s = s + convert(x, 7)
    r = int(s, 7)
    if r < 220:
        M.append(n)
print(max(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/9dc9bcae-00bb-4e7a-b93e-9e03ec567fad
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 10000, 2):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0]
        s = s + '1'
    else:
        s = s + str(n % 3)
    r = int(s, 4)
    if r < 340:
        M.append(r)

print(max(M))
'''

# Задание 5 https://education.yandex.ru/ege/task/2330b1ca-d047-4466-a7a1-b0ff32db6318
'''
M = []
for n in range(1, 1000):
    # s = convert(n, 2)
    # s = f'{n:b}'
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = (n % 3) * 3
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r >= 195:
        M.append(r)

print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/6e679e3e-d6c0-4c26-9e5e-d6b89730c238
'''
M = []
for n in range(1, 12+1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s, 2)
    M.append(r)

print(max(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/80ff89a4-46bc-4fed-b6df-f221b8bbcdfb
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        x = (n % 3) * 4
        s = s + convert(x, 3)
    r = int(s, 3)
    if r < 199:
        M.append(n)

print(max(M))
'''


'''
s = '231908209'
summa = sum([int(x) for x in s])

s = '10101010'
summa = s.count('1')
'''


# № 6995 (Уровень: Средний)
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if s[-1] == '0':
        s = s[:-1] + '1'
    else:
        s = s[:-1] + '0'
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r > 78:
        M.append([r, n])

print(min(M)[1])  # [80, 41]
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
