# region Домашка: ******************************************************************
'''
import turtle as t

t.screensize(-3000, 3000)
t.tracer(0)
size = 40
t.left(90)
for i in range(3):
    t.forward(7 * size)
    t.right(90)
    t.forward(12 * size)
    t.right(90)
t.up()
t.forward(4 * size)
t.right(90)
t.forward(6 * size)
t.left(90)
t.down()
for i in range(4):
    t.forward(83 * size)
    t.right(90)
    t.forward(77 * size)
    t.right(90)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * size, y * size)
        t.dot(3, 'red')
t.update()
t.done()
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
# ПОКА нашлось (333) ИЛИ нашлось (888)
#   ЕСЛИ нашлось (333)
#     ТО заменить (333, 8)
#     ИНАЧЕ заменить (888, 3)
'''
'''
s = '8' * 125
while '333' in s or '888' in s:
    if '333' in s:
        s = s.replace('333', '8', 1)
    else:
        s = s.replace('888', '3', 1)
print(s)
'''

'''
s= '1' + '0' * 80
while '10' in s or '1' in s:
    if '10' in s:
        s = s.replace('10', '001', 1)
    elif '1' in s:
        s = s.replace('1', '000', 1)
print(s.count('0'))
'''

# Тип 16 №4643
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(1) = 1;
# F(n) = 5·F(n – 1)+3·n при n > 1.
#
# Чему равно значение функции F(4)? В ответе запишите только натуральное число.

'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 5 * F(n - 1) + 3*n


print(F(4))
'''


def F(n):
    if n <= 2:
        return n - 1
    if n > 2:
        return 3 * F(n - 1) - F(n - 2)


print(F(6))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 4, 6]
# КЕГЭ  = []
# на следующем уроке:
