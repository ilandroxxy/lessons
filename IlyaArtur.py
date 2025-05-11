# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Единицы измерения информации
# 1 бит - минимальная единица измерения информации
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит

# № 7338 (Уровень: Базовый)
'''
sym = 10
alp = 26
i = 5

bit = sym * i
print(bit / 8)  # 6.25 -> 7
byte = 7
print(byte * 350)
'''


# Прототип номер 1 (картинка)
'''
pixels = 640 * 320
# colors = 2 ** i
colors = 64
i = 6  # 2 ** 6 >= 64
# i - это бит на один пиксель

# bit = pixels * i
bit = pixels * i
print(bit / 2**13)
'''


# https://education.yandex.ru/ege/task/2f2c0411-60b9-4a6b-abe8-186ecd97afe2
'''
pixels = 1079 * 1919
colors = 7999
i = 13  # 2 ** 13 >= 7999
bit = pixels * i

bit_199 = bit * 199

print(bit_199 / 19_999_999)
'''
# 267.832252


# https://education.yandex.ru/ege/task/c4adfb30-2b1d-4601-869e-d52ed7dab6cb
'''
pixels = 1024 * 768

bit_27 = 1_638_400 * 220
bit = bit_27 / 27

i = bit / pixels
print(i)  # 16.9753
i = 16
print(2**i)
'''

# https://education.yandex.ru/ege/task/6332cc39-3e04-4b5b-acef-8c71dc0f1e3f
'''
pixels = 1024 * 768
colors = 4096
i = 12
bit = pixels * i
print(bit)

bit_all = 1_310_720 * 300
print(bit_all / bit)  # 41.666
'''


# https://education.yandex.ru/ege/task/b211c7d5-1f29-4efd-bbdd-ee32b831869e
'''
pixels = 1280 * 1024
i = 32
bit = pixels * i
bit = bit * 0.6
print(bit / 2**23)
'''

# https://education.yandex.ru/ege/task/b70dd558-b67e-416b-ae44-a056f98c933d
'''
colors = 28
pixels = 1024 * 768
speed = 65536
i = 5

bits = pixels * i

time = bits/speed

print(time / 60)
'''

# Прототип номер 2 (музыка)

# bit = a (шт) * b (Гц) * c (бит) * t (сек)

# https://education.yandex.ru/ege/task/97232e31-d97b-4f20-badf-1c38458126c4
'''
a = 2
b = 48000
c = 10  # 2**10 = 1024 уровнями квантования.
# t - ? длина самого музыкального фрагмента

# T - время передачи данных
U = 256_000  # бит/с
T = 18 * 60  # с
bit = U * T
print(bit)
bit = (bit / 60) * 100
print(bit)
t = bit / (a * b * c)
print(t / 60)
'''


# https://education.yandex.ru/ege/task/7e9d81e1-0e8a-4d19-b107-ed2daadbbdb4
'''
a = 1
b = 16000
t = 1.5 * 60 * 60
# c - ?

bit = 256 * 2**23
print(bit / (a * b * t))  # 24.855
'''


# https://education.yandex.ru/ege/task/7407e7ee-2ca4-4372-b173-b39bffa2d1d9
'''
a = 2
b = 44000
c = 16
t = 60
bit = a * b * c * t

bit_32 = bit * 32

print(bit_32 / 1_802_240)
'''


# https://education.yandex.ru/ege/task/69f7445f-bff9-4586-bd5b-1bbfa80ff30d

a = 2
t = 90
b = 48000
c = 16
print((a * b * c * t) / 3200)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
