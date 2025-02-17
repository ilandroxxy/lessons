# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/658ead8e-8e85-4ad1-a74d-075f3e9f8bf0
'''
symbols1 = 1
alphabet1 = 1000  # 2**10 >= 1000
i1 = 10
bit1 = symbols1 * i1

symbols2 = 10
alphabet2 = 33  # 2**6 >= 33
i2 = 6
bit2 = symbols2 * i2  # бит на один символ
print(bit2)

bit = bit1 + bit2
print(bit / 8)  # 8.75
byte = 9
print(byte * 52)
'''
# Ответ: 468


# https://education.yandex.ru/ege/task/a35ac12d-56d0-45d9-87ef-a1d81dbfd6b1
'''
symbols1 = 1
alphabet1 = 2000  # 2 ** 11 >= 2000
i1 = 11
bit1 = symbols1 * i1
print(bit1 / 8)  # 1.375
byte1 = 2

symbols2 = 30 + 10
alphabet2 = 26 + 10 + 2  # 2 ** 6 >= 38
i2 = 6
bit2 = symbols2 * i2
print(bit2 / 8)  # 30.0
byte2 = 30


symbols3 = 60
alphabet3 = 33*2 + 2  # 2 ** 7 >= 68
i3 = 7
bit3 = symbols3 * i3
print(bit3 / 8)  # 52.5
byte3 = 53

print((byte1 + byte2 + byte3) * 30)
'''
# Ответ: 2550


# https://education.yandex.ru/ege/task/638ac2c9-defe-4ca9-971a-ee65a1774d31
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if sum(map(int, s)) % 2 == 0:
        s = '2' + s[2:] + '0'
    else:
        s = '20' + s[2:] + '1'
    r = int(s, 3)
    if r > 75:
        R.append([r, n])

print(min(R))

for x in R:
    if x[0] == 78:
        print(x)
'''
# R = [[78, 44], [78, 62], [78, 80], [78, 44]]
# min(R) [78, 44]


'''
n = 8
print(bin(n)[2:])  # двоичная
print(convert(n, 2))

print(oct(n)[2:])  # восьмеричная
print(convert(n, 8))

print(hex(n)[2:])  # шестнадцатеричная
print(convert(n, 16))

print(convert(n, 3))  # трочиная 
'''
# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# todo Разобрать сложную задачку:
# https://education.yandex.ru/ege/task/724475c0-8d62-4879-80a6-99e86710b738

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке:
