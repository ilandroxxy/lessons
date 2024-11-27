# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/12b3aabc-7777-4808-b29a-29993b289cca
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = alphabet[n % b] + s
        n //= b
    return s


n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25 ** 4 - 2024
print(convert(n, 25).count('0'))
'''


# https://education.yandex.ru/ege/task/730369b5-bb1f-4ec1-a50e-7a44f0b0ae09

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = alphabet[n % b] + s
        n //= b
    return s


for x in range(1, 1000):
    n = 27**7 - 3**11 + 36 - x
    s = convert(n, 3)
    summa = sum([int(i) for i in s])
    if summa == 22:
        print(x)
        break



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
