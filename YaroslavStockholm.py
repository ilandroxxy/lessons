# region Домашка: ******************************************************************


'''
M = []
for n in range(9, 1000+1):
    s = bin(n)[2:]

    if n % 2 == 0:
        s = '1' + s + '00'
    else:
        s = s + bin(s.count('1'))[2:]
    r = int(s, 2)
    if r > 88:
        M.append([r, n])

print(min(M)[1])
'''
import sys
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


from string import *
alphabet = digits + ascii_uppercase
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


# Задание 14 https://education.yandex.ru/ege/task/18a7009f-9d5c-467d-88c4-102e7ed5aca4
'''
n = 2*729**75 + 2*243**78 + 81**81 + 2 *27**84 + 2*9**87 + 58
s = convert(n, 27)
print(s.count('0'))
'''

# Задание 14 https://education.yandex.ru/ege/task/1b5ee551-6d66-4c66-b1ae-8169874ee37b
'''
for x in range(2030+1):
    n = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 5:
        print(x)
'''

# Задание 14 https://education.yandex.ru/ege/task/f1486087-bcff-4963-a860-bf501c4686db
'''
n = 7*49**120 - 6*343**65 - 5*7**40
print(convert(n, 7).count('6'))
'''

# Задание 14 https://education.yandex.ru/ege/task/a8903831-c37e-4e0a-8633-b69e0bd7a182
'''
n = 5*7776**7 + 4*1296**6 + 3*216 - 7776
s = convert(n, 36)
print(s.count('I') + s.count('U') + s.count('Z'))
print(len([x for x in s if x in 'IUZ']))
'''


# Задание 14 https://education.yandex.ru/ege/task/a8c96097-e410-484b-8fe6-9d1034a9e228
'''
for x in range(2030+1):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''


# Задание 14 https://education.yandex.ru/ege/task/660f09fb-51cc-496a-a57e-6aa856698de9
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
summa = 0
for x in alphabet[:15]:
    A = int(f'97968{x}13', 15)
    B = int(f'7{x}213', 15)
    if (A + B) % 11 == 0:
        summa += alphabet.index(x)

print(summa)
'''


# Задание 14 https://education.yandex.ru/ege/task/258db83f-773f-43a0-88da-89f8e3c2ab70
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:18]:
    A = int(f'77968{x}11', 18)
    B = int(f'4{x}213', 18)
    if (A + B) % 7 == 0:
        print((A + B) // 7)
'''

alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for y in alphabet[:17]:
    for x in alphabet[:15]:
        A = int(f'123{x}5', 15)
        B = int(f'67{y}9', 17)
        if (A + B) % 131 == 0:
            print((A + B) // 131)
            exit()



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
