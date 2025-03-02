# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
import turtle as t
k = 30
t.screensize(2000,2000)
t.tracer(0)
t.left(90)
t.down()

for i in range(4):
    t.forward(10*k)
    t.right(270)
t.up()
t.forward(3*k)
t.right(270)
t.forward(5*k)
t.right(90)
t.down()
for j in range(2):
    t.forward(10*k)
    t.right(270)
    t.forward(12*k)
    t.right(270)
t.up()
for x in range(-30,30):
    for y in range(-30,30):
        t.setpos(x*k, y*k)
        t.dot(3, 'blue')
t.update()
t.done()
'''


# № 20488 (Уровень: Сложный)
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) > 1]
    uncopied = [x for x in M if M.count(x) == 1]

    # if len(M) != len(set(M)):
    if len(copied) > 0 and len(uncopied) > 0:

        if M.count(max(M)) == 1:

            if sum(uncopied) >= (3 * sum(copied)):
                print(copied, uncopied)
                cnt += 1
print(cnt)
'''
# Ответ: 1382


# https://education.yandex.ru/ege/task/0f1bb8de-fe34-40c1-a82e-8d012e8519dc
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if (max(M) + min(M)) ** 2 > M[1] ** 2 + M[2] ** 2 + M[3] ** 2:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/2f370a43-39d3-4557-97a3-920195435a5d
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if len(M) == len(set(M)):
        if 3 * (M[0] + M[-1]) >= 2 * sum(M[1:-1]):
            cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/task/96c09be1-da8c-4460-b91f-05f352ddaa78

cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    flag = 0
    if len(M) != len(set(M)):
        flag += 1
    nechet = [x for x in M if x % 2 != 0]
    if len(nechet) == 3:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Артур 2/9 -> 14 вторичных баллов +[1, 12] -[2, 5, 6, 8, 12, 14, 16]
# Илья 1/9 -> 7 вторичных баллов +[2] -[1, 3, 5, 6, 8, 12, 14, 16]
