# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/c5e4d9a3-018f-4705-b0dc-68403da4763f
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


n = 3*7**82 - 4*49**21 + 5*343**25
s = convert(n, 7)
print(sum([int(x) for x in s]))
'''


# https://education.yandex.ru/ege/task/038952ca-0ea6-4083-8831-34ab2aac8eba
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


n = 36**65 + 6**112 - 136
s = convert(n, 6)
print(s[-3:])
'''


# https://education.yandex.ru/ege/task/35d1a21d-f415-4666-830a-8028485771a4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r += alphabet[n % b]
        n //= b
    return r[::-1]


for x in range(2042):
    n = 25**61 + 5**178 - x
    s = convert(n, 5)
    if s.count('0') == 60:
        print(x)
'''

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

# 0123456789ABC
for x in alphabet[:15]:
    A = int(f'9897{x}21', 15)
    B = int(f'12{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
