# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# I = pixels * i
# I - вес картинки в бит
# i - это бит на один пиксель

# colors = 2 ** i


# https://education.yandex.ru/ege/inf/task/c0059c7b-fccc-42d5-b1b0-dffa46d4fccc
'''
pixels = 480 * 768
# i - ?

I = 405 * 2**13  # бит
i = I / pixels
print(i)  # 9.0

# 2+1 2+1 2+1 -> 6 бит на хранение одного пикселя
print(2**6)  # 64
'''


# https://education.yandex.ru/ege/inf/task/2a1fcef0-3aad-4539-8b04-4a51298a0b08
'''
pixels = 1660 * 4048
I = 13 * 2**23  # бит

i = I / pixels
print(i)  # 16.22873470165246

i = 16
print(2**i)
'''


# https://education.yandex.ru/ege/inf/task/2640303f-cc77-424f-989c-f142e11c46f6
'''
i = 24+8
pixels = 1024 * 768

I = pixels * i
print(I / 2**13)
'''


# https://education.yandex.ru/ege/inf/task/6332cc39-3e04-4b5b-acef-8c71dc0f1e3f
'''
pixels = 1024 * 768
i = 12
I = pixels * i  # бит

U = 1_310_720  # бит/с
t = 300

print(U * t / I)  # 41.666666
'''


# https://education.yandex.ru/ege/inf/task/f6a4cbda-6370-43f2-839e-f3b856609737
'''
pixels = 640 * 320
i = 6

I = pixels * i
print(I / 2**13)
'''


# https://education.yandex.ru/ege/inf/task/ce57772b-890f-46fc-814d-c8818d3e67ca

# I = a * b * c * t
# a - кол-во каналов (шт)
# b - частота кадров (гц)
# c - глубина кодирования (бит)
# t - длительность (сек)
'''
t = 3*60
a = 4
c = 16
b = 48000
I = a * b * c * t   # бит

U = 3200  # бит / с
T = I / U  # сек
print(T / (60 * 60))
'''


# https://education.yandex.ru/ege/inf/task/69f7445f-bff9-4586-bd5b-1bbfa80ff30d
# I = a * b * c * t
# a - кол-во каналов (шт)
# b - частота кадров (гц)
# c - глубина кодирования (бит)
# t - длительность (сек)
'''
a = 2
t = 90
b = 48000
c = 16
I = a * b * c * t

T = I / 3200
print(T)
'''


# https://education.yandex.ru/ege/inf/task/e981a8c4-5b49-4b78-8dea-e70229591c14
# I = a * b * c * t
# a - кол-во каналов (шт)
# b - частота кадров (гц)
# c - глубина кодирования (бит)
# t - длительность (сек)
'''
a = 4
t = 3*60
b = 44 * 1000
c = 16 * 8
I = a * b * c * t

U = 768 * 2**13  # бит/с
T = I / U
print(T)
'''

# https://education.yandex.ru/ege/inf/task/d5d28bd5-14b2-4087-86d2-8e093fc949e4
'''
picxels = 1024*768
t = 288
U = 65536
I = t * U

i = I/picxels
print(2**i)
'''


# https://education.yandex.ru/ege/inf/task/2761e91c-9239-4e0e-b7c1-1e56166f3fc4
'''
picxels = 1600*900
i = 11
I = i * picxels
I = I * 16
T = 300
print(I / T)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 4, 5, 6, 7, 8, 9, 13, 14, 15, 16, 17, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 11
