# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# https://education.yandex.ru/ege/task/7954f17b-5247-4104-b3ac-b8f0d668abb2
'''
pixels = 1280 * 960
i = 11
bit_photo = pixels * i
# t = ?

a = 1
b = 32000
c = 16
# t = ?

bit_video = 96_468_992 * 200
# bit_video = music_bit + photo_bit
# bit_video = (a * b * c * t) + (bit_photo * 10 * t)
# bit_video = (a * b * c + bit_photo * 10) * t
t = bit_video / (a * b * c + bit_photo * 10)
print(t)
'''


# https://education.yandex.ru/ege/task/1769ee78-deec-48be-a248-12165baef040
'''
from itertools import *
n = 0
cnt = 0
for p in product(sorted('ВЕЧНОСТЬ'), repeat=6):
    word = ''.join(p)
    n += 1
    if n % 2 == 0:
        if word.count('О') >= 2:
            if word[0] not in 'ВЧНСТ':
                cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/052ffd67-7571-4f91-a8a9-3b5a3e5926e1
'''
from fnmatch import *
for x in range(3226, 10**8, 3226):
    if fnmatch(str(x), '3?99?7*8'):
        print(x, x // 3226)


from re import *
for x in range(3226, 10**8, 3226):
    if fullmatch('3[0-9]99[0-9]7[0-9]*8', str(x)):
        print(x, x // 3226)
'''

# https://education.yandex.ru/ege/task/bc14c08c-63b5-4523-99c3-06e9daeb1e7c
'''
def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x//j]
    return sorted(set(div))


for x in range(333555, 777999+1):
    d = [j for j in divisors(x) if len(str(j)) == 2]
    if len(d) == 35:
        print(min(d), max(d))
'''


# https://education.yandex.ru/ege/task/ad067f91-26ed-4058-b28a-cb9fc3d92ac0
'''
def divisors(x):
    div = []
    for j in range(2, int(x ** 0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

print(divisors(24))  # [2, 3, 4, 6 , 8, 12]


for x in range(625681, 758642):
    if int(x**0.5) == (x**0.5):
        d = [j if (j >= 10) else -1 for j in divisors(x)]
        if len(d) == 7:
            if -1 not in d:
                print(*d[-2:])
'''




# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [5, 8, 9, 14, 15, 19-21, 23]
# КЕГЭ = []
# на следующем уроке: 25, 26/27


# Первый пробник 7.03.25:
# Лев 8/46 -> _ вторичных баллов +[2, 5, 15, 16, 19, 20, 23, 25] -[8, 9, 12, 21]
