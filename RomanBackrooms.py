# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# a=int(input())
# b=0
# for i in range(1, a+1):
#     if a%i==0:
#         b+=i
# print(b)

'''
a = int(input())
b = int(input())
for x in range(a, b+1):  # x = 8
    flag = True
    for j in range(2, x):
        if x % j == 0:
            flag = False
    if flag == True:
        print(x)
'''

# Правильная функция поиска простого числа
'''
def is_prime(x):  # def - создать функции с именем is_prime и аргументов x
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


a = int(input())
b = int(input())
for x in range(a, b+1):
    if is_prime(x):
        print(x)
'''

'''
n = int(input())  # 20
summa = 0
for i in range(1, n+1):
    summa += i
    if summa > n:
        print(i)
        break
'''


# Тип 2 №48450
# Логическая функция F задаётся выражением:
# (w → (y ≡ z)) ∧ (y ≡ (z → x))
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (w <= (y == z)) and (y == ( z <= x))
                print(x, y, z, w, int(F))
'''

# (x → y) ∨ ¬(w → z)
#
# ((x ∧ ¬y) ∨ (w → z)) ≡ (z ≡ x)
#
# ((y ∨ z) → (z ∧ w)) ≡ ¬ ((x ∧ z) → (w ∨ y))

'''
(x <= y) or (not(w <= z))

((x and (not y)) or (w <= z)) == (z == x)

((y or z) <= (z and w)) == (not((x and z) <= (w or y)))
'''


# Тип 6 №59711
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 10 Направо 270]
# Поднять хвост
# Вперёд 3 Направо 270 Вперёд 5 Направо 90
# Опустить хвост
# Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270].
#
# Определите, сколько точек с целочисленными координатами
# будут находиться внутри объединения фигур, ограниченных
# заданными алгоритмом линиями, включая точки на линиях.
'''
import turtle as t
t.screensize(-2000, 2000)
t.tracer(0)
size = 40

# Пишем псевдокод:
for i in range(4):  # Повтори 4 [Вперёд 10 Направо 270]
    t.forward(10 * size)
    t.right(270)
t.up()  # Поднять хвост
t.forward(3 * size)
t.right(270)
t.forward(5 * size)
t.right(90)
t.down()  # Опустить хвост
for i in range(2):  # Повтори 2 [Вперёд 10 Направо 270 Вперёд 12 Направо 270].
    t.forward(10 * size)
    t.right(270)
    t.forward(12 * size)
    t.right(270)

# Тут рисует точки
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
