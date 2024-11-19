# region Домашка: ******************************************************************

'''
m = []
for n in range(1, 100):
    s = bin(n)[2:]

    for i in range(2):
        if s.count('1') % 2 == 0:
            s = '11' + s[2:] + '00'
        else:
            s = '10' + s[2:] + '11'

    r = int(s, 2)
    m.append(r)
print(max(m))
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 14 https://education.yandex.ru/ege/task/18a7009f-9d5c-467d-88c4-102e7ed5aca4
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 2 * 729**75 + 2 * 243 ** 78 + 81 ** 81 + 2*27**84 + 2*9**87 + 58
s = convert(n, 27)
print(s.count('0'))
'''


# Задание 14 https://education.yandex.ru/ege/task/5b214f5e-974b-46db-bf04-5aa73d9d99d3
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 3 * 15**1140 + 2 * 15**1025 + 15**923 - 3 * 15**85 + 2 * 15**74 + 3
s = convert(n, 15)

maxi = 0
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''


# Задание 14 https://education.yandex.ru/ege/task/eca565e6-aa59-4e06-8e2c-fccdac9e9fd7
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print((A + B) // 18)
'''

# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12]
# КЕГЭ  = []
# на следующем уроке:
