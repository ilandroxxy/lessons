# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# № 47403 (Уровень: Базовый)
'''
import turtle as t
t.left(90)
t.tracer(0)
t.screensize(-4000, 4000)
size = 40

for i in range(4):
    t.fd(12*size)
    t.rt(90)
t.rt(30)
for i in range(3):
    t.fd(8*size)
    t.rt(60)
    t.fd(8*size)
    t.rt(120)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


# № 7264 OpenFIPI (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r

print(convert(8, 2))  # 1000


n = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
R = []
while n > 0:
    R.append(n % 7)
    n //= 7
R.reverse()
print(R.count(6))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


n = 343**515 - 6*49**520 + 5*49**510 - 3*7**530 - 550
s = convert(n, 7)
print(s.count('6'))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


for x in range(1, 2030+1):
    n = 3**100 - x
    r = convert(n, 3)
    if r.count('0') == 1:
        print(x)
'''


# № 19484 (Уровень: Базовый)
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# print(alphabet[25])
def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r

n = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017
s = convert(n, 27)
print([alphabet.index(x) for x in s if x < 'P' and x in alphabet[0::2]])
print(sum([alphabet.index(x) for x in s if x < 'P' and x in alphabet[0::2]]))
'''


# № 19246 ЕГКР 21.12.24 (Уровень: Базовый)


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:25]:
    A = int(f'11353{x}12', 25)
    B = int(f'135{x}21', 25)
    if (A + B) % 24 == 0:
        print((A + B) // 24)


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ = []
# на следующем уроке: 15, 17
