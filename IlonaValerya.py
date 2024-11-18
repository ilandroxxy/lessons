# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
n = 125
print(bin(n))  # 0b1111101 - Перевод в двоичную систему счисления
print(bin(n)[2:])  # 1111101 - Берем все символы, кроме первых двух
print(f'{n:b}')  # 1111101
print(int('1111101', 2))  # 125

print(oct(n))  # 0o175 - Перевод в восьмеричную систему счисления
print(oct(n)[2:])  # 175 - Берем все символы, кроме первых двух
print(f'{n:o}')  # 175
print(int('175', 8))  # 125

print(hex(n))  # 0x7d - Перевод в шестнадцетеричная систему счисления
print(hex(n)[2:])  # 7d - Берем все символы, кроме первых двух
print(f'{n:x}')  # 7d
print(f'{n:X}')  # 7D
print(int('7D', 16))  # 125
'''


# Задание 5 https://education.yandex.ru/ege/task/5f631ae3-da90-45d6-84fa-5c18717831b8
'''
cnt = 0
for n in range(1, 1000):
    s = oct(n)[2:]  # Строится восьмеричная запись числа N
    if n % 2 != 0:  # если число N нечётное
        s = s + '00'  # то к этой записи справа дописываются два нуля 00
    else:  # если число N чётное
        s = s + '10'
    r = int(s, 8)  # Затем число R переводится в десятичную систему счисления.
    if 100 <= r <= 999:
        cnt += 1
print(cnt)
'''


# Задание 5 https://education.yandex.ru/ege/task/da1c175a-d87f-46d0-9211-35a2d2a5b554
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]  # Строится двоичная запись числа N
    if n % 5 == 0:   # если число N делится на 5
        # s = s + s[-3] + s[-2] + s[-1]
        s = s + s[-3:]
    else:  # если число N не делится на 5
        x = (n % 5) * 5
        s = s + bin(x)[2:]
    r = int(s, 2)
    if r > 256:
        M.append(n)  # .append() добавляем новый элемент в конец списка

print(min(M))
'''


# Задание 5  https://education.yandex.ru/ege/task/0a888798-5892-4b73-9822-6067357d93e3
'''
M = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)
    if r > 156:
        M.append(n)

print(min(M))
'''


# Задание 5 # https://education.yandex.ru/ege/task/bcf2f1cf-26f3-4678-bf57-1b1eb99555ad
'''
M = []
for n in range(2, 1000):
    s = bin(n)[2:]

    for i in range(2):
        if s[-1] == s[-2]:

            # if s[-1] == s[-2]:
            #                 ~^^^^
            # IndexError: string index out of range
            s = s + '0'
        else:
            s = s + '1'

    r = int(s, 2)
    if r > 93:
        M.append(n)

print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/9fb60578-88e4-465d-b603-dbf30d312808
'''
def convert(n, b):  # n - число для перевода, b - в какую систему будем переводить
    s = ''
    while n > 0:
        s = s + str(n % b)
        n = n // b  # n //= b
    return s[::-1]


def convert(n, b):
    s = ''
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


M = []
for n in range(11, 1000):
    s = convert(n, 5)
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = convert(x, 5) + s
    r = int(s, 5)

    if r > 375:
        M.append(n)
print(min(M))
'''


# Задание 5  https://education.yandex.ru/ege/task/8cf5f358-d940-4c96-b34d-e8448147eeb5

def convert(n, b):
    s = ''
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


M = []
for n in range(1, 1000):
    s = convert(n, 2)
    if n % 2 == 0:
        s = s + '0' * s.count('0')  # кол-во '0' в строке s
    else:
        s = '1' * s.count('1') + s
    r = int(s, 2)
    if r > 2000:
        M.append(n)

print(min(M))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
