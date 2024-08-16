# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

# Тип 5 Номер 17668
'''
R = []
for n in range(27+1, 1000):
    s = f'{n:b}'
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    R.append(r)
print(min(R))
'''


# КЕГЭ № 17609 Резервный день 19.06.2024 (Сибирь)
'''
def F(x, A):
    return (x % 33 == 0) <= ((x % A != 0) <= (x % 242 != 0))


R = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(0, 10000)):
        R.append(A)
print(max(R))
'''

# Тип 6 Номер 17669
'''
import turtle as t
t.screensize(-100000, 100000)
t.tracer(0)
t.left(90)
l = 20

# Тут пишем псевдокод
for i in range(4):
    t.forward(19*l)
    t.right(90)
    t.forward(30*l)
    t.right(90)

t.up()

t.fd(2*l)
t.rt(90)
t.fd(8*l)
t.lt(90)

t.down()

for i in range(4):
    t.forward(93*l)
    t.right(90)
    t.forward(97*l)
    t.right(90)

t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*l, y*l)
        t.dot(2, 'red')

t.done()
'''

# Тип 7 Номер 17670
'''
pixels = 1024 * 960
# V = pixels * i
# colors = 2 ** i

V = 140 * 1_474_560  # вес 32 фотографий
V1 = V / 32
i = V1 / pixels
print(i)  # 6.5625 -> 6
print(2 ** 6)  # colors
'''
# Ответ: 64

'''
s = sorted('ЛАЙМ')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    num += 1
                    if 'М' not in slovo and 'Л' not in slovo and 'ЙЙ' not in slovo:
                        print(num)
'''


def F(x, y, A):
    return (x + y <= 24) or (y <= x - 2) or (y >= A)


for A in range(1, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке:
