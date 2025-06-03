# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
s = '01234567'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for g in s:
                        num = a+b+c+d+e+g
                        if a != '0':
                            if '54' not in num and '26' in num:
                                if len(set(num))== len(num):
                                    cnt += 1
                                    print(cnt)
'''


'''
def convert(n,b):
    s = ''
    while n > 0:
        s = s + str(n % b)
        n = n // b
    return s[::-1]

M = []
for n in range(1, 10000):
    r = convert(n,4)
    if sum(map(int, r)) % 2 == 0:
        r = '31' + r +'02'
    else:
        x = (n % 3) * 7
        r = '1' + r + convert(x, 4)
    r = int(r,4)
    if r < 4528:
        M.append(n)
print(max(M))
'''

'''
def ch(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x = x // 4

    return s


res = []
for n in range(1, 10000):
    s = ch(n)
    if sum(int(e) for e in s) % 2 == 0:
        s = '31' + s + '02'
    else:
        s = '1' + s + ch((n % 3) * 7)
    r = int(s, 4)
    if r < 4528:
        res.append(n)
print(max(res))
'''


print(135 * 122 + 149 * 75 - 9*96)
print(26799)

import turtle as t
t.screensize(5000, 5000)
t.left(90)
t.tracer(0)
l = 10

t.color('teal')
for _ in range(4):
    t.forward(135 * l)
    t.right(90)
    t.forward(122 * l)
    t.right(90)
t.up()
t.forward(41 * l)
t.left(90)
t.forward(66 * l)
t.right(90)
t.down()
t.color('purple')
for _ in range(4):
    t.forward(149 * l)
    t.right(90)
    t.forward(75 * l)
    t.right(90)

t.up()
for x in range(-80, 80):
    for y in range(-80, 80):
        t.goto(x * l, y * l)
        t.dot(3, 'black')
t.done()

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = []
# на следующем уроке: 24, 26, 27
