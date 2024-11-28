# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://inf-ege.sdamgia.ru/problem?id=7761
'''
print(bin(4**2020 + 2**2017 - 15)[2:].count('1'))
'''


# https://inf-ege.sdamgia.ru/problem?id=27411
'''
def convert(n, b):
    s = ''
    while n > 0:
        s += str(n % b)
        n //= b
    return s[::-1]


def convert(n, b):
    s = ''
    while n > 0:
        s = str(n % b) + s
        n //= b
    return s


n = 49**7 + 7**21 - 7
print(convert(n, 7).count('6'))
'''


# № 15327 Досрочная волна 2024 (Уровень: Базовый)
'''
12


n = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
print(len([x for x in convert(n, 27) if x > '9']))
'''


# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    s = ''
    while n > 0:
        s = alphabet[n % b] + s
        n //= b
    return s


for x in range(2030+1):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        print(x)
'''


# № 15328 Досрочная волна 2024 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:27]:
    A = int(f'123{x}24', 27)
    B = int(f'135{x}78', 27)
    if (A + B) % 26 == 0:
        print((A + B) // 26)
'''


# https://inf-ege.sdamgia.ru/problem?id=48387
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:11]:
    for y in alphabet[:11]:
        A = int(f'{x}341{y}', 11)
        B = int(f'56{x}1{y}', 19)
        if (A + B) % 305 == 0:
            print((A + B) // 305)
'''

'''
from string import *
alphabet = digits + ascii_uppercase

for p in range(10, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x+y+y, p))
'''


# № 13910 (Уровень: Базовый)
'''
from string import *
alphabet = digits + ascii_uppercase

for i, x in enumerate(alphabet, 0):
    print(i, x)
    # 17 H
    # 21 L
    # 26 Q
    # 29 T
    # 30 U

print(alphabet.find('U'))  # 30

# for p in range(30+1, 36+1):
for p in range(alphabet.find('U')+1, 36+1):
    if int('TH', p) + int('NQ', p) + int('U', p) == int('1L7', p):
        print(p)
'''
# Ответ: 33

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
