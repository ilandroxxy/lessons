# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 6 Статград 23.10.25 вариант 1
'''
import turtle as t
t.tracer(0)
t.left(90)
t.screensize(5000, 5000)
size = 40

for i in range(7):
    t.forward(15*size)
    t.right(90)
    t.forward(23 * size)
    t.right(90)
t.up()
t.forward(3 * size)
t.right(90)
t.forward(5 * size)
t.right(90)
t.down()
for i in range(7):
    t.forward(252*size)
    t.right(90)
    t.forward(398 * size)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * size, y * size)
        t.dot(3, 'red')

t.update()
t.done()
'''

# Задание 8 Статград 23.10.25 вариант 1
'''
cnt = 0
alp = '0123456789ABCDE'
for a in alp:
    for b in alp:
        for c in alp:
            for d in alp:
                word = a + b + c + d
                if word[0] != '0':
                    if word.count('8') == 1:
                        # if word[0] != word[1] and word[1] != word[2] and word[2] != word[3]:
                        if all(p*2 not in word for p in '0123456789ABCDE'):
                            cnt += 1
print(cnt)
'''


# Задание 9 Статград 23.10.25 вариант 1
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    if 2 <= M.count(min(M)) <= 3 and 5 <= len(copied1) <= 6:
        if min(copied1) ** 2 + max(copied1) ** 2 <= (sum(copied1) - max(copied1) - min(copied1)) ** 2:
            cnt += 1
print(cnt)
'''

# M = [1, 2, 3, 4, 5]
# max(M)  # 5
# min(M)  # 1
# sum(M)  # 1+2+3+4+5
# sum(M) - min(M) - max(M)  # 2+3+4



# Задание 17 Статград 23.10.25 вариант 1
'''
M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if x < 0]
B = [x for x in A if len(str(abs(x))) == 3 and abs(x) % 6 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) > max(B):
            R.append(x**2 + y**2)
print(len(R), max(R))
'''
# сумма квадратов x ** 2 + y ** 2
# квадрат суммы (x + y) ** 2


# Задание 19-21 Статград 23.10.25 вариант 1
'''
from math import ceil, floor
def F(s, n):
    if s <= 505:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s-3, n-1), F(floor(s/5), n-1)]
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(505, 100000) if F(s, n=2)]) # 2532 Не правильно
# print([s for s in range(505, 100000) if F(s, n=3) and not F(s, n=1)]) # 2533, 2534
# print([s for s in range(505, 100000) if F(s, n=4) and not F(s, n=2)]) # 2536
'''


# Задание 27 Статград 23.10.25 вариант 1
"""
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if x < 50:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if 22 < x < 30 and 25 < y < 32:
        clustersB[0].append([x, y])
    if 20 < x < 27 and 34 < y < 41:
        clustersB[1].append([x, y])
    if 19 < x < 26 and 43 < y < 50:
        clustersB[2].append([x, y])

# Проверка, что класетры не пустые:
'''
print(clustersA[0])
print(clustersA[1])
print(clustersB[0])
print(clustersB[1])
print(clustersB[2])
'''

def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
            R.append([summa, p])
    return max(R)[1]

print(center(clustersA[0]))  # [16.99841482246666, 95.6727515672738]
print(center(clustersA[1]))  # [63.94062638636294, 87.77751031781972]

print(len(clustersA[0]))  # 102
print(len(clustersA[1]))  # 113

P1 = 16.99841482246666 + 95.6727515672738
P2 = 63.94062638636294 + 87.77751031781972
print(int(P1 * 10000), int(P2 * 10000))


print(center(clustersB[0]))  # [23.329917580199655, 26.41328219493777]
print(center(clustersB[1]))  # [22.1707588150025, 39.65891347675987]
print(center(clustersB[2]))  # [21.38834573144159, 48.899310705252915]

print(dist(center(clustersB[0]), [0, 0]))  # 35.24126176243305
print(dist(center(clustersB[1]), [0, 0]))  # 45.43536028898788
print(dist(center(clustersB[2]), [0, 0]))  # 53.37231417670156

Qx = 21.38834573144159
Qy = 26.41328219493777
print(int(Qx * 10000), int(Qy * 10000))  # 213883 264132
"""


# № 27275 (Уровень: Базовый)
# На вход алгоритма подается натуральное число N. Алгоритм строит по нему новое число R следующим образом:
# 1. Строится троичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
#   а) если число N делится на 3, то к этой записи справа дописываются цифры 21, а слева – цифра 1;
#   б) если число N на 3 не делится, то остаток от деления числа N на 3 умножается на 5,
#   переводится в троичную систему счисления и дописывается в конец числа.
# Полученная таким образом запись является троичной записью искомого числа R.
# Укажите максимальное нечётное число N, после обработки которого с помощью этого
# алгоритма получается число R, не превышающее 1130.
'''
def G(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r


L = []
for n in range(1, 100000):
    s = G(n, 3)
    if n % 3 == 0:
        s = '1' + s + '21'
    else:
        x = (n % 3) * 5
        s = s + G(x, 3)

    r = int(s, 3)
    if r <= 1130 and n % 2 != 0:
        L.append(n)
print(max(L))
'''

# № 27276 (Уровень: Базовый)
# На вход алгоритма подается натуральное число N. Алгоритм строит по нему новое число R следующим образом:
# 1. Строится троичная запись числа N.
# 2. Далее эта запись обрабатывается по следующему правилу:
#   а) если число N делится на 3, то к этой записи справа дописываются две её последние цифры,
#   а слева – цифра 1;
#   б) если число N на 3 не делится, то сумма цифр троичной записи умножается на 5,
#   переводится в троичную систему счисления и дописывается в конец числа.
# Полученная таким образом запись является троичной записью искомого числа R.
# Укажите число R, ближайшее к числу 1000, которое может быть получено в результате работы алгоритма.

L = []
def convert(n, b):
    r = ''
    while n > 0:
        r = str(n % b) + r
        n //= b
    return r

for n in range(1, 1000):
    n3 = convert(n, 3)
    if n % 3 == 0:
        n3 = '1' + n3 + n3[-2:]
    else:
        n3 = n3 + convert((sum([int(x) for x in n3]) * 5), 3)
    r = int(n3, 3)
    if 995 < r < 1005:
        print(r)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [11, 19-21]
# на следующем уроке: (26)


# region 📖 Пробник (Вариант 2)

# Студент #Татьяна
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 3, 4, 6, 7, 10, 11, 14, 16, 17, 19, 20, 21, 22, 23, 25
# ⛔️ Неверно: 5, 8, 12
# ❔ Без ответа: 9, 13, 15, 18, 24, 26, 27
# Итог: 17/29 первичных балла ~ 70 вторичных


# Студент #Анна
# Дата: #Суббота #28Февраля2026
# ✅ Верно: 1, 2, 4, 7, 8, 11, 12, 14, 15, 16, 17, 18, 23, 25
# ⛔️ Неверно: 3, 5, 6, 10, 19, 20, 21, 27
# ❔ Без ответа: 9, 13, 22, 24, 26
# Итог: 14/29 первичных балла ~ 62 вторичных

# endregion 📖 Пробник (Вариант 2)


