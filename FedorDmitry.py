# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from math import floor
def G(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    t = [G(s - 3, n - 1), G(s - 7, n - 1), G(floor(s / 4), n - 1)]
    return any(t) if (n - 1) % 2 == 0 else all(t)
    return any(t) if (n - 1) % 2 == 0 else any(t)


print([s for s in range(16, 1000) if G(s, n=2)])
print([s for s in range(16, 1000) if G(s, n=3) and not G(s, n=1)])
print([s for s in range(16, 1000) if G(s, n=4) and not G(s, n=2)])
'''


'''
a=open("files/24.txt").readline()
a=a.replace('2025','2 025')
t=a.split(' ')
m=0
for i in range(0,len(t)-50):
   a=t[i]
   for j in range(50):
       a+=t[j]
   if a.count('Y')>=140:
       m=max(m,len(a)+3)
       print(a)


print(m)
'''


s = open('files/24.txt').readline()
s = s.split('2025')
maxi = 0
for i in range(len(s)-50):
    r = '***' + '2025'.join(s[i:i+50]) + '2025'
    # j = r.rindex('2025')
    # r = r[:j+4]
    if r.count('Y') >= 140:
        maxi = max(maxi, len(r))
print(maxi)




# ¬x       |   (not x)
# ¬(w≡z)   |   (not(w == z))
# x ∧ y    |    x and y
# x ∨ x    |    x or y
# x → w    |    x <= w
# w ≡ z    |    w == z
'''
print('x y z w')
for x in 0, 1:
   for y in 0, 1:
       for z in 0, 1:
           for w in 0, 1:
               F = (not((x <= w) <= (w == z))) and y
               if F == 1:
                   print(w, z, y, x)
'''


'''
print((1024 * 768 * 30 - 800 * 600 * 28) * 100 / 2 ** 13)

pixels1 = 1024 * 768
i1 = 30
I1 = pixels1 * i1

pixels2 = 800 * 600
i2 = 28
I2 = pixels2 * i2

print(((I1 - I2) * 100) / 2 ** 13)
'''

# • 1 байт = 2³ бит
# • 1 Кбайт = 2¹⁰ байт = 2¹³ бит
# • 1 Мбайт = 2²⁰ байт = 2²³ бит
# • 1 Гбайт = 2³⁰ байт = 2³³ бит
# • 1 Тбайт = 2⁴⁰ байт = 2⁴³ бит


'''
def divisors(x):
    d = []
    for j in range(2, int(x ** 0.5) + 1):  # не считая самого числа
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(7_800_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) >= 2:
        M = min(d) + max(d)
        if M % 100 == 63:
            if M % len(d) == 0:
                print(x, M)
                cnt += 1
                if cnt == 5:
                    break
'''

#
# № 28944 ЕГКР 18.04.26 (Уровень: Базовый)
# Напишите программу, которая перебирает целые числа, большие
# 8 996 452, в порядке возрастания и ищет среди них числа,
# представленные в виде произведения ровно двух простых множителей,
# не обязательно различных, каждый из которых содержит в своей
# записи ровно две цифры 3.
# В ответе в первом столбце таблицы запишите первые 5 найденных
# чисел в порядке возрастания, а во втором столбце - для каждого
# из чисел соответствующий им наибольший из найденных множителей.
# Количество строк в таблице для ответа избыточно.
'''
from itertools import product
def divisors(x):
    d = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(8_996_452+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 2 and str(j).count('3') == 2]
    if len(d) > 0:
        for p in product(d, repeat=2):
            if p[0] * p[1] == x:
                print(x, max(p))
                cnt += 1
                break
        if cnt == 5:
            break



from itertools import product
def divisors(x):
    d = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            d += [j, x // j]
    return sorted(set(d))

cnt = 0
for x in range(8_996_452+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 2 and str(j).count('3') == 2]
    if len(d) > 0:
        if any(p[0] * p[1] == x for p in product(d, repeat=2)):
            print(x, max(d))
            cnt += 1
            if cnt == 5:
                break
'''






# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 27]
# КЕГЭ = [8, 9, 15, 16, 23, 25]
# на следующем уроке:


# region 📖 Пробник (Вариант 2)

# Студент #Федор
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 10, 17, 22, 24, 27
# ❔ Без ответа: 26
# Итог: 19/29 первичных балла ~ 75 вторичных

# Студент #Вадим
# Дата: #Суббота #04Апреля2026
# ✅ Верно: 1, 2, 7, 10, 11, 12, 13, 14, 15, 16, 19, 20, 23, 25
# ⛔️ Неверно: 3, 4, 5, 6, 8, 9, 18, 21, 22, 24
# ❔ Без ответа: 17, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных


# endregion 📖 Пробник (Вариант 2)



