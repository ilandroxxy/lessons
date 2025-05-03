# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

# 2
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not (x <= y)) or (z == w) or z
                if not F:
                    print(x, y, z, w)
'''

# 6
'''
import turtle as t
t.screensize(-2000,2000)
t.tracer(0)
size = 25
t.left(90)
for i in range (2):
    t.forward(28*size)
    t.right(90)
    t.forward(18*size)
    t.right(90)
t.up()
t.forward(14*size)
t.right(90)
t.forward(10*size)
t.left(90)
t.down()
for i in range(2):
    t.forward(30*size)
    t.right(90)
    t.forward(7*size)
    t.right(900)
t.up()
for x in range (-40, 40):
    for y in range (-40,40):
        t.goto(x*size, y*size)
        t.dot(4, 'red')
t.update()
t.done()
'''

# 5
'''
def to_ternary(num):
  result = ''
  while num:
      result += str(num % 3)
      num //= 3
  return result[::-1]
for N in range(3, 100)[::-1]:
    R = to_ternary(N)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += to_ternary((N % 3) * 3)
    R = int(R, 3)
    if R <= 150:
        print(N)
        break
'''

# 8
'''
R = []
s = sorted('ПОБЕДА')
num = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                  for f in s:
                    slovo = a + b + c + d + e + f
                    num += 1
                    if slovo[0] == 'О' and slovo.count('О') == 1 and slovo.count('П') == 1 and slovo.count('Б') == 1 and slovo.count('Е') == 1 and slovo.count('Д') == 1 and slovo.count('А') == 1:
                      if num % 2 == 0:
                        R.append(num)
print(max(R))
'''

# 12
'''
for n in range(4, 10000):
    s = '4' + '2' * n
    while '42' in s or '8222' in s or '2222' in s:
      if '42' in s:
        s = s.replace('42', '2', 1)
      if '8222' in s:
        s = s.replace('8222', '24', 1)
      if '2222' in s:
        s = s.replace('2222', '8', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if summa == 110:
        print(n)
        break
'''

'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if sorted(M)[::-1] == M:
        M = sorted(M)
        if (min(M) + max(M)) / 2 > (M[1] + M[2] + M[3] + M[4] + M[5]) / 5:
            print(sum(M))
            break
'''


pixels = 7680 * 4320
i = 16  # colors = 2 ** 16
bit = pixels * i  # бит на одно фото

card = 9 * 2**33  # (2**33)
count = card / bit
print(count)  # 145.635 - на одной карте памяти поместится 145 фотографий


print(4010 // 145)  # 27 - это 27 карт памяти
print(4010 % 145)  # 95 - это 95 фотографий не поместилось, то есть находятся на последней


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [5, 8]
# на следующем уроке: сложные 11 и 7 номера


# Второй пробник 10.02.25:
# 7/29 -> 42 вторичных баллов +[1, 4, 6, 12, 14, 15, 16] -[3, 5, 8, 23, 25]
