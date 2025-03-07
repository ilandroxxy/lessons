# region Домашка: ******************************************************************

# Тип 13 №73868
# Узлы с IP адресами 206.123.209.193 и 206.123.210.118 принадлежат одной сети.
# Какое наименьшее количество IP-адресов, в двоичной записи которых ровно 15 единиц,
# может содержаться в этой сети?
'''
from ipaddress import *

for mask in range(15, 33):
    net1 = ip_network(f'206.123.209.193/{mask}', 0)
    net2 = ip_network(f'206.123.210.118/{mask}', 0)
    if net1 == net2:
        cnt = 0
        for ip in net1:
            s = f'{ip:b}'
            if s.count('1') == 15:
                cnt += 1
        print(cnt)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Единицы измерения информации:
# 1 бит - минимальная единица измерения
# 1 байт - 8 бит - 2**3 бит
# 1 Кбайт - 1024 байт - 2**10 байт - 2**13 бит
# 1 Мбайт - 1024 Кбайт - 2**20 байт - 2**23 бит
# 1 Гбайт - 1024 Мбайт - 2**30 байт - 2**33 бит

# Задачи с картинками:
'''
v - весь фото в бит
v = pixels * i, где i - это кол-во бит на один пиксель
colors = 2 ** i

colors = 256 -> i = 8
colors = 260 -> i = 9
2 ** i >= colors
'''

# Задачи с музыкой:
'''
v - весь звуковой файл (в бит)
v = a * b * c * t

a - кол-во каналов записи (шт)
b - частотой дискретизации (Гц) 
c - глубина кодирования (бит)
t - продолжительность записи (сек)
'''

# Тип 7 №18078
# Какой минимальный объём памяти (в Кбайт) нужно зарезервировать,
# чтобы можно было сохранить любое растровое изображение
# размером 640 на 320 пикселей при условии, что в изображении
# могут использоваться 64 различных цвета?
# В ответе запишите только целое число, единицу измерения писать не нужно.
'''
pixels = 640 * 320
colors = 64
i = 6
v = pixels * i  # бит
print(v / 2 ** 13)
'''
# Ответ: 150


# Тип 7 №72565
# Камера дорожного наблюдения делает цветные фотографии с разрешением 1024 * 768 пикселей,
# используя палитру из 4096 цветов. Снимки сохраняются в памяти камеры, группируются
# в пакеты по 100 штук и отправляются в центр обработки по каналу связи с пропускной
# способностью 128 Кбайт/сек. На сколько процентов необходимо сжать изображения,
# чтобы передавать один пакет за 6 минут?
# В ответе запишите число — округлённый до целого процент сжатия.
'''
pixels = 1024 * 768
colors = 4096  # 2 ** i >= 4096
i = 12

v = pixels * i  # бит
v = v * 0.4  # -60%
v_100 = v * 100

u = 128 * 2**13  # бит/с
T = (v_100 / u) / 60
print(T)  # 15.0
'''


# Тип 7 №28545
# Для проведения эксперимента создаются изображения, содержащие случайные наборы
# цветных пикселей. Размер изображения — 320x240пк, при сохранении изображения каждый
# пиксель кодируется одинаковым числом битов, все коды пикселей записываются подряд,
# методы сжатия не используются. Размер файла не должен превышать 100 Кбайт,
# при этом 20 Кбайт необходимо выделить для служебной информации.
# Какое максимальное количество различных цветов и оттенков можно использовать
# в изображении?
'''
pixels = 320 * 240
v = (100-20) * 2**13  # то что уходит только на пиксели
i = v / pixels
print(i)  # 8.53333
i = 8  # бит на один пиксель
print(2**i)
'''


# Тип 7 №57414
'''
a = 2
b = 48000
c = 16
t = 90
v = a * b * c * t  # бит

u = 3200  # бит/с
T = v / u
print(T)  # 4320
'''


# № 20482 (Уровень: Базовый)
'''
a = 1
b = 240_000
# c - ?
t = 1

u = 168 * 2**13  # бит/с
v = u * t

c = ((v / 28) * 100) / (a * b * t)
print(c)  # 20.48 -> 20
'''


# № 20425 (Уровень: Средний)

a = 2
b = 48000
c = 16
t = 90

# v_video = v_music + v_photo
v_music = a * b * c * t
v_video = 54691875  * 2**13  # бит
v_photos = v_video - v_music

pixels = 3840 * 2160
photos = 60 * t
# colors - ?
# i - ?

v_photo = v_photos / photos

i = v_photo / pixels
print(i)  # 10.0
colors = 2 ** i
print(colors)

# Ответ: 1024



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]

# Второй пробник 28.02.25:
# Dmitry 13/16 -> 58 вторичных баллов +[1-5, 7, 8, 12, 14-16, 23, 25] -[6, 9, 13, 17]
