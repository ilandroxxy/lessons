# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# https://education.yandex.ru/ege/task/d26658b5-8543-4e2d-bb16-d916165bdde9
'''
from math import ceil
sym = 8  # кол-во символов
alp = 7  # 2 ** i >= alp
i = 3  # бит на один символ

bit = sym * i  # всего бит на один пароль

print(bit / 8)  # 3.0 - тут всегда округляем вверх (ceil)
byte = 3  # всего байт на один пароль
# byte = ceil(bit / 8)

# user = byte + dop
dop = 8  # всего байт на дополнительные сведения пользователя
user = byte + dop
print(user * 42)
'''


# https://education.yandex.ru/ege/task/a1beb780-b471-41fe-a815-b22e0ec632dc
'''
bytes = 276 * 2**10  # байт на 862 серийных номера
byte = bytes / 862  # байт на один серийный номер
print(byte)  # 327.870069 - не более, значит округляем вниз
byte = 327

bit = byte * 2**3  # бит на один серийный номер

alp = 10 + 52 + 458  # 2 ** 10 >= 520 (alp)
i = 10

sym = bit / i
print(sym)  # 261.6
'''


# https://education.yandex.ru/ege/task/f2ae72ec-dd45-47c0-996a-69d1b524b2e9
'''
sym1 = 10
alp1 = 10
i1 = 4
bit1 = sym1 * i1

sym2 = 10
alp2 = 26
i2 = 5
bit2 = sym2 * i2

bit = bit1 + bit2
print(bit / 8)  # 11.25 -> 12
byte = 12

user = 600 / 20
print(user - byte)
'''


print(1632 / 42)
print(2 ** 38)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 6, 14, 15, 17
