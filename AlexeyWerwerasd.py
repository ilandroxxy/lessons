# region Домашка: ************************************************************


# endregion Домашка: *********************************************************
# #
# #
# region Урок: ************************************************************

'''
import turtle as t
t.lt(90)
size = 10
t.screensize(-2000, 2000)
t.tracer(0)
t.down()
for i in range(2):
    t.fd(77 * size)
    t.rt(90)
    t.fd(101 * size)
    t.rt(90)
t.up()
t.fd(29 * size)
t.lt(90)
t.fd(44*size)
t.rt(90)
t.down()
for i in range(7):
    t.fd(88 * size)
    t.rt(90)
    t.fd(75 * size)
    t.rt(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.setpos(x * size, y * size)
        t.dot(2,'red')
t.update()
t.done()
'''


# 18116
n = 0
summa = 0
for s in open('0. files/9.csv'):
  M = [int(x) for x in s.split(';')]
  n += 1
  F = [x for x in M if M.count(x) == 3 and x % 2 == 0]
  f = [x for x in M if M.count(x) == 1 and x % 2 != 0]
  if len(F) == 3 and len(f) == 3:
    if sum(F)**2 > sum(f)**2:
      summa += n
print(summa)


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
