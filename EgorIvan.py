# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# https://education.yandex.ru/ege/task/39bb599c-c811-49fe-84b7-be8dd035d167
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

n = 5**23 + 25 ** 12
s = convert(n, 5)
print(s.count('0'))

# Вариант 2
n = 5**23 + 25 ** 12
s = []
while n > 0:
    s.append(n % 5)
    n //= 5
s = s[::-1]
print(s.count(0))


# Вариант 3
n = 5**23 + 25 ** 12
s = ''
while n > 0:
    s = str(n % 5) + s
    n //= 5
print(s.count('0'))
'''
from runpy import run_path

# https://education.yandex.ru/ege/task/1b5ee551-6d66-4c66-b1ae-8169874ee37b
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for x in range(2030):
    n = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 5:
        print(x)
'''


# https://education.yandex.ru/ege/task/d90014d9-5105-4860-a4d3-f9cd62ad463e
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for x in range(2030):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        print(x)
'''

# https://education.yandex.ru/ege/task/68ca56c6-8e43-49bf-8ece-91cf0c76d3ba
'''
print(bin(2**24 + 2**14 - 2**5)[2:].count('1'))
'''


alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:2])  # ['0', '1']
print(alp[:8])  # ['0', '1', '2', '3', '4', '5', '6', '7']


# https://education.yandex.ru/ege/task/c87ec1c9-cbb1-4c23-b8ae-aae45260058c
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    A = int(f'98897{x}21', 19)
    B = int(f'2{x}923', 19)
    if (A + B) % 18 == 0:
        print(x, (A + B) // 18)
'''


# https://education.yandex.ru/ege/task/2269ff29-1320-4c26-b127-c149167e1c9a
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:15]:
    A = int(f'9897{x}21', 15)
    B = int(f'12{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
'''

# Егор
# https://education.yandex.ru/ege/task/dd1ad283-40a2-4123-9328-5bb0cbcb8092
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:15]:
    A = int(f'99658{x}29', 15)
    B = int(f'102{x}023', 15)
    if (A + B) % 14 == 0:
        print((A + B) // 14)
'''


# https://education.yandex.ru/ege/task/038952ca-0ea6-4083-8831-34ab2aac8eba
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

n = 36**65 + 6**112 - 136
s = convert(n, 6)
print(s[-3:])
'''


# https://education.yandex.ru/ege/task/fb0fcacf-ba6f-49bc-bf96-3eee0b9d6a01
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp)
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = 625**90+125**120 - 5*25
s = convert(n, 25)
print(sum([int(x, 25) for x in s if x in alp[0::2]]))
'''


# https://education.yandex.ru/ege/task/6e6c2557-26e8-4b87-a6ff-96defe05f178
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

n = 5**20 + 5**10 - 5**13 - 5**3
s = convert(n, 5)  # '44444440004444444000'
print(s.count('4') * 4)
'''

# Сумма цифр числа
'''
n = 44444440004444444000

summa0 = str(n).count('4') * 4
print(summa0)

summa1 = 0
for x in str(n):
    summa1 += int(x)
print(summa1)

summa2 = sum([int(x) for x in str(n)])
print(summa2)

summa3 = sum(map(int, str(n)))
print(summa3)
'''


# https://education.yandex.ru/ege/task/730369b5-bb1f-4ec1-a50e-7a44f0b0ae09
'''
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for x in range(1, 10000):
    n = 27**7 - 3**11 + 36 - x
    s = convert(n, 3)
    if sum(map(int, s)) == 22:
        print(x)
        break
'''


# № 13246 Открытый курс "Слово пацана" (Уровень: Средний)
'''
# ValueError: int() base must be >= 2 and <= 36, or 0

alp = sorted('0123456789QWERTYUIOPSDFGHAJKLZXCVBNM')
for p in range(10, 36+1):
    for x in alp[:p]:
        for y in alp[:p]:
            if int(f'24{x}9', p) + int(f'{y}{x}{y}3', p) == int(f'{x}4{y}0', p):
                print(int(x + y + y, p))
'''






# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 14]
# КЕГЭ = []
# на следующем уроке:
