# region Домашка: ******************************************************************


# № 9781 Основная волна 20.06.23 (Уровень: Базовый)
# https://stepik.org/lesson/1038682/step/8?unit=1062773
'''
L = []
for n in range(4, 1000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    L.append(summa)
print(max(L))
'''


# № 6786 (Уровень: Средний)
# https://stepik.org/lesson/1038682/step/15?unit=1062773
'''
for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    count = 0
    for j in range(1, summa+1):
        if summa % j == 0:
            count += 1

    if count == 2:
        print(n)
        break
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Встроенные системы счисления
'''
n = 8
print(bin(n)[2:])  # 2-я
print(oct(n)[2:])  # 8-я
print(hex(n)[2:])  # 16-я


print(f'{n:b}')  # 2-я
print(f'{n:o}')  # 8-я
print(f'{n:x}')  # 16-я
print(f'{n:X}')  # 16-я
'''

# Задание 5 https://education.yandex.ru/ege/task/0a888798-5892-4b73-9822-6067357d93e3
'''
M = []
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]  # Перевод в 2-ю систему счисления
    if n % 2 == 0:
        s = s + '01'
    else:
        s = '1' + s + '1'
    r = int(s, 2)  # Перевод из 10-й в 2-ю
    if r > 156:
        M.append(n)
print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/f8355528-2d18-46e8-a782-1798a2682495
'''
n = 115
s = oct(n)[2:]
for x in '02468':
    s = s.replace(x, '')
r = int(s, 8)
print(r)
'''


# Задание 5 https://education.yandex.ru/ege/task/5f631ae3-da90-45d6-84fa-5c18717831b8
'''
cnt = 0
for n in range(1, 1000):
    s = oct(n)[2:]
    if n % 2 != 0:
        s = s + '00'
    else:
        s = s + '10'
    r = int(s, 8)
    # if 100 <= r <= 999:
    if len(str(r)) == 3:
        cnt += 1
print(cnt)
'''

# Задание 5 https://education.yandex.ru/ege/task/71189626-0f31-4380-b790-94a173acd59a
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]

# print(convert(8, 2))  # 1000


M = []
for n in range(1, 1000):
    s = convert(n, 7)
    new_s = ''
    for x in s:
        if x in '13579':
            new_s += str(int(x) + 1)
        else:
            new_s += x
    summa = sum([int(x) for x in new_s])
    new_s = convert(summa, 7) + new_s
    if new_s[0] in '13579':
        new_s = s[0] + new_s
    r = int(new_s, 7)
    if r > 2000:
        M.append(r)

print(min(M))
'''


# Задание 5 https://education.yandex.ru/ege/task/b90d79be-0bcc-4425-9d1b-e5ac3b4003ab
'''
K = []
for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        l = bin((n % 3) * 3)[2:]
        s = s + l
    r = int(s, 2)
    if r < 76:
        K.append(n)
print(max(K))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
