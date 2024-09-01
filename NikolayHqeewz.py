# region Домашка: ******************************************************************

'''
import turtle as t
t.screensize(-10000, 10000)
t.tracer(0)
t.left(90)
l = 20
for i in range(2):
    t.fd(8 * l)
    t.rt(90)
    t.fd(18 * l)
    t.rt(90)
t.up()
t.fd(4 * l)
t.rt(90)
t.fd(10 * l)
t.lt(90)
t.down()
for i in range(2):
    t.fd(17 * l)
    t.rt(90)
    t.fd(7 * l)
    t.rt(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(2, "red")

t.update()
t.done()
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
for n in range(2, 10000):
    s = f'{n:b}'  # s = bin(n)[2:]
    s = s[:-1] + s[1] * 2
    r = int(s, 2)
    if r > 76:
        print(n)
        break

R = []
for n in range(2, 10000):
    s = f'{n:b}'  # s = bin(n)[2:]
    s = s[:-1] + s[1] * 2
    r = int(s, 2)
    if r > 76:
        R.append(n)
print(min(R))
'''

# n = 19
# s = f'{n:b}'  # s = bin(n)[2:]
# s = s[:-1] + s[1] * 2
# r = int(s, 2)
# print(r)


# Сделать разбор на канал Тип 5 №51974
'''
R = []
for n in range(1, 10000):
    s = f'{n:b}'
    for _ in range(3):
        summa = sum([int(x) for x in str(int(s, 2))])
        if summa % 2 != 0:
            s += '1'
        else:
            s += '0'
    r = int(s, 2)
    if r > 1028:
        R.append(r)
print(min(R))
'''

'''
R = []
for n in range(1, 10000):
    s = f'{n:b}'
    for _ in range(3):
        s += str(sum([int(x) for x in str(int(s, 2))]) % 2)
    r = int(s, 2)
    if r > 1028:
        R.append(r)
print(min(R))
'''

# n = 17
# s = f'{n:b}'
# for _ in range(3):
#     summa = sum([int(x) for x in str(int(s, 2))])
#     if summa % 2 != 0:
#         s += '1'
#     else:
#         s += '0'
# r = int(s, 2)
# print(r)

'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1, 10000):
    s = convert(n, 3)
    s = s + str(n % 3)
    r = int(s, 3)
    if 1000 <= r <= 9999:
        R.append(r)
print(min(R))
'''


# Тип 5 №16809
'''
for n in range(0, 255+1):
    s = f'{n:b}'.zfill(8)
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', '0')
    r = int(s, 2) - n
    if r == 133:
        print(n)
'''


# Тип 5 №18487
'''
for n in range(1, 100):
    s = f'{n:b}'
    s = s[::-1]
    r = int(s, 2)
    if r == 13:
        print(n)
'''


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
