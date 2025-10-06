# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************




# Универсальная функция перевода
'''

from string import digits, ascii_uppercase
alp = digits + ascii_uppercase
print(alp)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ


alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

print(convert(8, 2))  # 1000
print(int('1000', 2))  # 8 
'''


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2 * 2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(s.count('0'))   # Какое кол-во нулей получилось в результате
print(len(s) - s.count('0'))   # Какое кол-во ненулевых элементов получилось в результате
print(len(set(s)))  # Кол-во РАЗЛИЧНЫХ элементов
print(s.count('0') + s.count('4'))
print(len([x for x in s if x > '9']))
'''


# Генераторы списков
'''
# Генератор[что_кладем откуда_это_берем]
# Генератор[что_кладем откуда_это_берем при_каком_условии]

R = []
for i in range(2, 8+1):
    R.append(i)
print(R)  # [2, 3, 4, 5, 6, 7, 8]

R = [i for i in range(2, 8+1)]
print(R)  # [2, 3, 4, 5, 6, 7, 8]

R = [i for i in range(2, 8+1) if i % 2 == 0]
print(R)  # [2, 4, 6, 8]

R = [i**2 for i in range(2, 8+1) if i % 2 == 0]
print(R)  # [4, 16, 36, 64]


# Открытие 17 файла
M = [int(x) for x in open('0. files/17.txt')]
print(M)

A = [x for x in M if x % 100 == 20]
print(A)

B = [x for x in M if len(str(x)) == 4]
print(B)

# Открытие 9 файла

for s in open('0. files/9.txt'):
    M = [int(x) for x in s.split()]
    print(M)
'''


# № 23754 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 3000+1):
    n = 9 * 11**210 + 8*11**150 - x
    s = convert(n, 11)
    if s.count('0') == 60:
        RES.append(x)
print(max(RES))
'''



# № 21709 ЕГКР 19.04.25 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

RES = []
for x in range(1, 3000+1):
    n = 4**210 + 4**110 - x
    s = convert(n, 4)
    if s.count('0') == 105:
        print(x)
        # 1024
        # 2048
    RES.append(s.count('0'))
print(max(RES))  # 105
'''

# Пример использования f-строк
'''
name = input('Введите имя: ')
print('Имя пользователя:', name)
print(f'Имя пользователя: {name}')
'''



# № 21413 Досрочная волна 2025 (Уровень: Базовый)
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A + B + C) % 20 == 0:
        RES.append((A + B + C) // 20)
print(min(RES))
'''


# № 14345 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
for x in alp[:14]:
    A = int(f'4B3{x}1', 14)
    B = int(f'5{x}F83', 16)
    if (A + B) % 13 == 0:
        print((A + B) // 13)
'''


'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
for p in range(16, 36):
    A = int('17496', p)
    B = int('91F83', p)
    C = int('D9543', p)
    if (A + B + C) % 12 == 0:
        print((A + B + C) // 12)
        break
'''
# ValueError: int() base must be >= 2 and <= 36, or 0


# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')
for p in range(10, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            A = int(f'24{x}9', p)
            B = int(y + x + y + '3', p)
            C = int(f'{x}4{y}0', p)
            if A + B == C:
                print(int(x + y + y, p))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14]
# КЕГЭ = []
# на следующем уроке:
