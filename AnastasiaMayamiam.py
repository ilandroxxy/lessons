# region Домашка: ******************************************************************

# № 11669 (Уровень: Базовый)
# https://stepik.org/lesson/1221217/step/4?unit=1234627
'''
from math import ceil, floor

def F(s, n):
    if s <= 116:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 7, n - 1), F(floor(s/3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(max([s for s in range(117, 10000 + 1) if F(s, n=3)]))
print([s for s in range(117, 10000 + 1) if F(s, 3) and not F(s, 1)])
print([s for s in range(117, 10000 + 1) if F(s, 4) and not F(s, 2)])
'''
import shutil

# № 8710 (Уровень: Средний)
# https://stepik.org/lesson/1221217/step/5?unit=1234627
'''
def F(s, n):
    if s <= 1:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 1, n - 1)]
    if s >= 4:
        h += [F(s - 4, n - 1)]
    if s % 3 == 0:
        h += [F(s / 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(4, 100 + 1) if F(s, 2)])
print([s for s in range(4, 100 + 1) if F(s, 3) and not F(s, 1)])
print([s for s in range(4, 100 + 1) if F(s, 4) and not F(s, 2)])
'''


# № 12928 (Уровень: Средний)
# https://stepik.org/lesson/1221217/step/11?unit=1234627
'''
def F(s, n):
    if s >= 21:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)


# print([s for s in range(1, 21) if F(s, 2)])
print([s for s in range(1, 21) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 21) if F(s, 4) and not F(s, 2)])
print([s for s in range(1, 21) if F(s, 5) and not F(s, 3) and not F(s, 1)])
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# № 21404 Досрочная волна 2025 (Уровень: Базовый)
'''
for n in range(1, 10000):
    # b = bin(n)[2:]
    # b = convert(n, 2)
    b = f'{n:b}'

    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r = int(b, 2)
    if r > 480:
        print(n)
        break
'''


'''
# i   012345
s = ['123456']

print(s[2:])  # ['3456']
'''


# № 20486 (Уровень: Базовый)
'''
R = []
for n in range(1, 10000):
    b = f'{n:b}'
    if n % 2 == 0:
        b = b + b[:3]
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    if r > 600:
        R.append(r)

print(min(R))
'''


# № 20278 (Уровень: Средний)
'''
for n in range(1, 1000):
    b = f'{n:b}'
    if sum(map(int, b)) % 2 == 0:
        b = '101' + b[3:] + '01'
    else:
        b = '111' + b[3:] + '11'
    r = int(b, 2)
    if r < 385:
        print(n)
'''

# № 20182 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for n in range(1, 10000):
    b = convert(n, 3)
    if sum(map(int, b)) % 2 == 0:
        b = '12' + b[2:] + '0'
    else:
        b = '10' + b[2:] + '2'
    r = int(b, 3)
    if r > 105:
        print(n)
        break
'''



# n - это число, которое будем переводить
# b - система счисления в которую будем переводить
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


print(convert(8, 2))


n = 8
print(bin(n)[2:])  # 1000
print(oct(n)[2:])  # 10
print(hex(n)[2:])  # 8


print(f'{n:b}')  # 1000
print(f'{n:o}')  # 10
print(f'{n:x}')  # 8
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 15, 16, 23, 19-21]
# КЕГЭ  = []
# на следующем уроке: 7, 8, 9, 13, 25

# Первый пробник 21.12.24:
# Анастасия 9/29 -> 48 вторичных баллов +[1, 2, 4, 12, 16, 14, 15, 23, 20-21] -[3, 8, 10, 11, 18, 19]
