# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# 1 бит - минимальная единица измерения информации
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 - байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит


# Задание 7 https://education.yandex.ru/ege/task/37dd91ce-1a3d-4d33-9370-445d9c44bb85

# pixels - кол-во пикселей на картинке (разрешение)
# V - вес картинки в бит
# i - сколько бит выделяется для 1 пикселя

# V = pixels * i

# colors - кол-во цветов передаваемое пикселем
# colors = 2 ** i
'''
i = 5  # бит
pixels = 300 * 400
V = (pixels * i) / (2**3) # бит
print(V)
'''


# https://education.yandex.ru/ege/task/c4adfb30-2b1d-4601-869e-d52ed7dab6cb
'''
pixels = 1024 * 768

V = (1_638_400 * 220) / 27
i = V / pixels
print(i)  # 16.975
print(2**16)
'''


# https://education.yandex.ru/ege/task/5511c181-ed14-4583-aadc-4a8a2d07ecd0
'''
pixels = 640 * 480
V = 40*2**13
i = V / pixels
print(i)
print(2**1)
'''


# https://education.yandex.ru/ege/task/b211c7d5-1f29-4efd-bbdd-ee32b831869e
'''
pixels = 1280 * 1024
i = 32
V = pixels * i
V = (V / 100) * 60
print(V / (2**23))
'''


# https://education.yandex.ru/ege/task/c0059c7b-fccc-42d5-b1b0-dffa46d4fccc
'''
pixels = 480 * 768
V = 405 * 2**13
i = V / pixels
print(i)  # 9
print(2**6)
'''


# https://education.yandex.ru/ege/task/26133fed-3f76-4e26-9b4a-a96c4160e69c
'''
pixels = 1536*1024
V = (9 * 2**23) / 6
i = V / pixels
print(2**i)
'''


# https://education.yandex.ru/ege/task/c750feb6-6609-485a-8bd0-c62b806727d3
'''
colors = 24
i = 5
pixels = 1024 * 768
V = pixels * i
print(V / 65536)
'''

# https://education.yandex.ru/ege/task/5b08e032-88b8-4cff-8b63-329f996e0472
'''
# V = a * b * c * t
a = 2
t = 90
b = 48000

V = 1600 * 86400
c = V / (a * b * t)
print(c)
'''


# https://education.yandex.ru/ege/task/32b13529-3681-4545-9ca9-fa9a88849498
'''
a = 4
c = 8  # глубина кодирования 
t = 8 * 60 + 32

V = 62.5 * 2**23
b = V / (a * c * t)
print(b)
'''

'''
a = 2
b = 16000
t = 4*60 + 16

V = 16*2**23
print(V / (a * b * t))
'''
# 16.384


# https://education.yandex.ru/ege/task/eeee81f3-071e-46a6-967d-043f06c8af92

t = 8
a = 1
b = 10000
c = 16
V = a * b * c * t
print(V / 2**13)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:
