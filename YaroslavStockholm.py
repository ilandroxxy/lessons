# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 5 https://education.yandex.ru/ege/task/fef8d85c-6b9d-43d3-954c-6acb16a1f5a9

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[:2])  # ['0', '1']
print(alphabet[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']
print(alphabet[:16])  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


R = []
for n in range(11, 1000):
    # s = bin(n)[2:]
    # s = f'{n:b}'
    s = convert(n, 2)
    if n % 5 == 0:
        # s = s + s[-3] + s[-2] + s[-1]
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = convert(x, 2) + s
    r = int(s, 2)
    if r > 512:
        R.append(n)

print(min(R))
'''


# Задание 5 https://education.yandex.ru/ege/task/a579a1b6-fe4b-45e9-afc3-57649ff2fa75

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for n in range(1, 10000):
    s = convert(n, 7)
    if s.count('2') % 2 == 0:
        s = s + '555'
    else:
        s = '1' + s
    r = int(s, 7)
    if r < 3799:
        print(n)


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6]
# КЕГЭ  = []
# на следующем уроке:
