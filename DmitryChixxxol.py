# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# № 20144
'''
def divisors(x):
    div = []
    for j in range(2, int(x ** 0.5) + 1):  # не считая самого числа
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

# print([x for x in range(2, 100) if len(divisors(x)) == 0])

cnt = 0
for x in range(3_333_337+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        R = max(d) - min(d)
        if R > 1000 and R % 3 == 0:
            print(x, R)
            cnt += 1
            if cnt == 5:
                break
'''


# 20068
'''
print(25 * 34 + 25 * 17 - 13 * 17)

import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
l = 30

for x in range(777):
    t.forward(25 * l)
    t.left(90)
    t.forward(34 * l)
    t.left(90)
t.up()
t.forward(12 * l)
t.left(90)
t.forward(17 * l)
t.right(90)
t.down()
for x in range(1996):
    t.forward(25 * l)
    t.left(90)
    t.forward(17 * l)
    t.left(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * l, y * l)
        t.dot(3, 'red')
t.update()
t.done()

'''


# 19895
'''
# sym - ?
alp = 10 + 2040
print(2**12)
i = 12

byte = 369 * 2**10 / 718
print(byte)  # 526.261
byte = 526

bit = byte * 8

sym = bit / i
print(sym)  # 350.66
'''


# 19892
'''
pixels = 1920 * 1080
i = 16  # 2 ** 16 >= colors
bit = pixels * i  # бит на одну фотографию
print(512 - 52)  # 460

for i in range(1, 15):
    if 460 % i == 0:
        print(i, 460 // i)
        # 5 92


print((92 * bit) / 2**23)  # 363.86
'''
# Ответ: 364



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 23, 25]
# КЕГЭ  = [23]
# на следующем уроке:


# Первый пробник 21.12.24:
# Dmitry 11/14 -> 54 вторичных баллов +[1, 2, 4-7, 10-12, 14, 25] -[3, 8, 13]

# Второй пробник 28.02.25:
# Dmitry 13/16 -> 58 вторичных баллов +[1-5, 7, 8, 12, 14-16, 23, 25] -[6, 9, 13, 17]
