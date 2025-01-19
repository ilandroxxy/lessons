# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s = s + alphabet[n % b]
        n = n // b
    return s[::-1]


for n in range(1,1000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        x = (n % 3) * 4
        r = r + convert(x, 3)
    res = int(r, 3)
    if res < 199:
        print(n)
'''



'''
import turtle as t
t.left(90)
t.tracer(0)
size = 40

t.right(90)
for i in range(3):
    t.right(45)
    t.forward(10 * size)
    t.right(45)
t.right(315)
t.forward(10 * size)
for i in range(2):
    t.right(90)
    t.forward(10 * size)

t.up()
for x in range(-50,50):
   for y in range(-50,50):
        t.goto(x * size, y * size)
        t.dot(2, 'red')
t.update()
t.done()
'''

'''
s = '0123456789ABCDEF'
cnt = 0
s1 = s[1::2]  # s1 = '13579BDF'
s2 = s[0::2]
for a in s:
    for b in s:
        for c in s:
            num = a + b + c
            if a != '0':
                if len(set(num)) == len(num):
                    if a in s1 and b in s2 and c in s1:
                        cnt += 1
                    if a in s2 and b in s1 and c in s2:
                        cnt += 1
print(cnt)
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 25]
# КЕГЭ  = []
# на следующем уроке:
