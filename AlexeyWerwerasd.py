# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************



#5
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


R = []
for n in range(1,1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        x = sum(map(int, s))
        s = s + convert(x, 3)
    r = int(s, 3)
    if r >= 220 and r % 2 == 0:
        R.append(r)
print(min(R))
'''

#6
'''
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
size = 30
for i in range (8):
    t.forward(16*size)
    t.right(90)
    t.forward(22*size)
    t.right(90)
t.up()
t.forward(5*size)
t.right(90)
t.forward(5*size)
t.left(90)
t.down()
for i in range(8):
    t.forward(52*size)
    t.right(90)
    t.forward(77*size)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''


#8
'''
s = sorted('ЯНВАРЬ')
R = []
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e 
                    n += 1
                    if 'ЯЯ' not in slovo and slovo.count('Ь') <= 1 and slovo[0] != 'Я':
                        R.append(n)
print(max(R))
'''


#11
'''
sym = 377
byte = (5536 * 1024) / 23155
print(byte) # 244.82245735262362 
byte = 245
bit = byte * 8
i = bit / sym
print(i)  # 5.1989 -> 6
i = 6

print(2**5+1)  # минимальная
print(2**6)  # максимальная
'''


#17
'''
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5 and abs(x) % 100 == 43]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) >= 1:
        if (x**2 + y**2 + z**2) <= max(A) ** 2:
            R.append(x**2 + y**2 + z**2)
print(len(R), min(R))
'''

#23
'''
def F(a, b):
    if a <= b or a == 24:
        return a == b
    return F(a - 1, b) + F(a - 6, b) + F(a // 2, b)
print(F(34, 29) * F(29, 19) * F(19, 6))
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [5, 8, 17]
# на следующем уроке:


# Второй пробник 10.02.25:
# 7/29 -> 42 вторичных баллов +[1, 4, 6, 12, 14, 15, 16] -[3, 5, 8, 23, 25]
