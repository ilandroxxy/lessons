# region Домашка: ******************************************************************

# № 5667 (Уровень: Базовый)
'''
for n in range(1, 100):
    s = '3' * 15 + '2' * 18 + '1' * n

    while '31' in s or '33' in s or '21' in s:
        if '31' in s:
            s = s.replace('31', '123', 1)
        if '33' in s:
            s = s.replace('33', '211', 1)
        if '21' in s:
            s = s.replace('21', '1', 1)

    summa = sum(map(int, s))

    summa = 0
    for x in s:   # s = '1321'
        summa += int(x)

    summa = sum([int(x) for x in s])


    if summa > 24:
        print(n)
        break
'''


# № 6786 (Уровень: Средний)
'''
def is_prime(n):  # n - 12
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


for n in range(1, 100):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    # summa = sum(map(int, s))
    summa = sum([int(x) for x in s if x.isdigit()])
    if is_prime(summa):
        print(n)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 5 https://education.yandex.ru/ege/task/46daeb92-f360-4dd2-aaaf-173ef18d4da0
'''
M = []
for n in range(1, 10000):
    s = bin(n)[2:]  # s = f'{n:b}'
    if s.count('1') % 2 == 0:
        s = '11' + s
    else:
        s = s + '00'
    r = int(s, 2)
    if r > 116:
        M.append(n)
print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/aee298d7-cf16-40a1-8b47-b0d531e27555
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]



M = []
for n in range(1, 1000):
    s = convert(n, 2)  # s = bin(n)[2:]
    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')
    s = s + str(s.count('1') % 2)
    r = int(s, 2)
    if r < 170:
        M.append(r)
print(max(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/0f0be116-5c24-4561-8675-493fe3c6ba53
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]



M = []
for n in range(1, 1000):
    s = convert(n, 5)  # s = bin(n)[2:]
    if n % 25 == 0:
        s = s[-3:] + s
    else:
        x = (n % 25)
        s = s + convert(x, 5)
    r = int(s, 5)
    if r > 10000:
        print(n)
        break
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 5, 12]
# КЕГЭ  = []
# на следующем уроке:
