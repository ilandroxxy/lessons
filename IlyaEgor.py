# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Единицы измерения информации (101010100101 биты)
# 1 бит - минимальная единица измерения информации
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит


# Фото
'''
# V = pixels * i  - вес фотографии в бит
# i - это кол-во бит на один пиксель
# colors <= 2 ** i

colors = 129   # 2**8 >= 129
# i = 8
'''


# https://education.yandex.ru/ege/inf/task/c750feb6-6609-485a-8bd0-c62b806727d3
'''
pixels = 1024 * 768
colors = 24  # 2 ** 5 >= 24
i = 5

V = pixels * i  # вес фото в бит
U = 65536  # бит/с

print(V / U)  # 60
'''

# https://education.yandex.ru/ege/inf/task/d5d28bd5-14b2-4087-86d2-8e093fc949e4
'''
# T = V / U
U = 65536  # бит/с
T = 288
V = U * T  # бит на одно фото

pixels = 1024 * 768
i = V / pixels
print(i)  # 24.0 -> 24
print(2 ** i)
'''


# https://education.yandex.ru/ege/inf/task/bf064a47-3902-46d8-a405-a5300e8caf5b
'''
pixels = 1024 * 768
colors = 4096  # 2 ** 12 >= 4096
i = 12

V = pixels * i  # бит на одну картинку
V_256 = V * 256

print(V_256 / 2**23)
'''


# https://education.yandex.ru/ege/inf/task/1027a3bb-c702-4d3e-9815-3c8d9ac033d6
'''
pixels = 1920 * 1080
i = 32  # глубиной кодирования
V = pixels * i  # вес одной фотографии

V_all = V + (120 * 8)

print((8 * 2**33) / V_all)  # 1035.61 -> 1035
'''


# https://education.yandex.ru/ege/inf/task/9bad2f7e-3d65-46c8-97e1-7c0546979d97
'''
pixels = 1200 * 1800
i = 2 * 8
V = pixels * i

print(V / (6*60))
'''


# https://education.yandex.ru/ege/inf/task/957625ec-a644-4180-bcee-896315e53052
'''
pixels = 2560*1440
i = 30
V = pixels * i

pixels2 = 1920*1080
i2 = 28
V2 = pixels2 * i2

print(((V - V2) * 130 )/ 2**13)
'''


# Музыка

# V = a * b * c * t - вес картинки (в бит)
# a - кол-во каналов (шт) - моно/стерео/квадра == 1/2/4
# b - частота дискретизации (Гц)
# c - битное разрешение == глубина кодирования (бит)
# t - длина записи (сек)


# https://education.yandex.ru/ege/inf/task/eeee81f3-071e-46a6-967d-043f06c8af92
'''
a = 1
b = 10000
c = 16
t = 8
V = a * b * c * t  # бит

print(V / 2**13)  # 156.25
'''


# https://education.yandex.ru/ege/inf/task/eb4d9b1f-9e48-4163-a44c-78007d760e63
'''
a = 2
b = 48000
c = 16
t = 150
V = a * b * c * t  # бит
V = V * 0.5

U = 3200  # бит/с

T = V / U
print(T / 3600)
'''


# https://education.yandex.ru/ege/inf/task/964a0dd2-e83b-4306-80c0-e5e22a49f05d
'''
a = 2
b = 44100
c = 32

V = 50 * 2**23

t = V / (a * b * c)
print(t / 60)
print(round(t / 60))
'''


# https://education.yandex.ru/ege/inf/task/21c8d3fd-6a3a-4352-aaa3-fcfd629d1c75
'''
a = 2
b = 192000
c = 24
t = 10* 60
V_all = a * b * c * t

U = 12800 # бит/с
T = 20
V1 = U * T

print(V_all / V1)
'''

# Три прототипа 11 номера
# 1. sym, alp = byte
# 2. sym, byte = alp
# 3. alp, byte = sym


# https://education.yandex.ru/ege/inf/task/b931a5bf-94b1-4fb8-86ec-e452222a1723
# 1. sym, alp = byte
'''
sym = 11
alp = 9540  # alp <= 2**i
# i - это бит на один символ

i = 14  # 2**14 >= 9540
bit = sym * i  # бит на один пароль


print(bit / 8)  # 19.25 -> 20
byte = 20

print((byte * 21504) / 2**10)
'''


# https://education.yandex.ru/ege/inf/task/f2ae72ec-dd45-47c0-996a-69d1b524b2e9
'''
sym1 = 10
alp1 = 26
i1 = 5
bit1 = sym1 * i1

sym2 = 10
alp2 = 10
i2 = 4
bit2 = sym2 * i2

bit = bit2 + bit1

print(bit / 8)  # 11.25 -> 12
byte = 12

# user = byte + dop
user = 600 / 20
print(user - byte)
'''

# https://education.yandex.ru/ege/inf/task/8bc85415-c843-4706-a859-a2ebe4e1c132
# 3. alp, byte = sym
'''
alp = 4088 + 10
i = 13   # 2 ** 13 >= alp

byte = (12 * 2**10) / 186
print(byte)  # 66.06451 -> 66 (потребовалось не более 12 Кбайт)
bit = 66 * 8

sym = bit / i
print(sym)  # 40.61538 -> 40
'''


# https://education.yandex.ru/ege/inf/task/2038f860-2bb1-4606-861f-802a7efb7062
# 2. sym, byte = alp
'''
sym = 2783

byte = (11 * 2**30) / 3_845_627
print(byte)  # 3071.3223 -> 3072 (требуется не менее 11 Гбайт памяти)
bit = 3072 * 8

i = bit / sym
print(i) # 8.8278 -> 9 (требуется не менее 11 Гбайт памяти)
i = 9

print(f'Определите минимально возможную мощность алфавита: {2**8 + 1}')
print(f'Определите максимальная возможную мощность алфавита: {2**9}')

alp = 256 # i = 8
alp = 129  # i = 8

alp = 128  # i = 7
alp = 80  # i = 7
alp = 65  # i = 7

alp = 64  # i = 6
alp = 33  # i = 6
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке:
