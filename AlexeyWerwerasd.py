# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************


# Номер 5
'''
alfabet = sorted('1234567890qwertyuiopasdfghjklzxcvbnm')
def q (n, b):
    r = ''
    while n > 0:
        r = alfabet[n % b] + r
        n //= b
    return r


R = []
for n in range(1, 10000):
    s = q(n, 3)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + q((n % 3) * 3, 3)
    r = int(s, 3)
    if r > 150:
        R.append(n)
print(min(R))
'''


# Номер 6
'''
import turtle as t
t.lt(90)
size = 30
t.screensize(2000, 2000)
t.tracer(0)
t.down()
for i in range(4):
    t.fd(10 * size)
    t.rt(270)
t.up()
t.fd(3 * size)
t.rt(270)
t.fd(5*size)
t.rt(90)
t.down()
for i in range(2):
    t.fd(10 * size)
    t.rt(270)
    t.fd(12 * size)
    t.rt(270)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.setpos(x * size, y * size)
        t.dot(2,'red')
t.update()
t.done()
'''

# Номер 8
'''
R = []
s = sorted('СБОРНИК')
num = 0
for a in s:
  for b in s:
    for c in s:
      for d in s:
        for e in s:
          for f in s:
            slovo = a + b + c + d + e + f
            num += 1
            if slovo[0] != "Р":
                if slovo.count('Б') == 2:
                    if slovo.count('К') <= 1:
                        R.append(num)

print(max(R))
'''


# Номер 12
'''
for n in range(4, 10000):
  s = '5' + '2' * n
  while '52' in s or '1122' in s or '2222' in s:
    if '52' in s:
      s = s.replace('52', '11', 1)
    if '2222' in s:
      s = s.replace('2222', '5', 1)
    if '1122' in s:
      s = s.replace('1122', '25', 1)
  if s.count('5') * 5 + s.count('2') * 2 + s.count('1') == 64:
    print(n)
'''


# Номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''


# Номер 15
'''
def F(x, y, A):
  return (x < A) or (3*y + 2*x > 120) or (A > y)

R = []
for A in range(1, 1000):
  if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        R.append(A)
print(min(R))
'''

# Номер 16
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + F(n - 1)
print (F(2024) - F(2022))
'''


# Номер 23
'''
def F(a, b):
    if a > b or a == 13:
        return 0
    if a == b:
        return 1
    else:
        return F(a+1, b) + F(a+2, b) + F(a*3, b)

print(F(3, 8) * F(8, 18))
'''


# Номер 25
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):
    if fnmatch(str(x), '2*1?71'):
        print(x, x // 2023)
'''

# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
# КЕГЭ = [5, 8]
# на следующем уроке:

# Второй пробник 10.02.25:
# 7/29 -> 42 вторичных баллов +[1, 4, 6, 12, 14, 15, 16] -[3, 5, 8, 23, 25]
