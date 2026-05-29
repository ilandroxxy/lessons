# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

#4 https://stepik.org/lesson/1228671/step/5?unit=1242204
'''
from functools import *

@lru_cache(None)
def F(n):
    if n**0.5 == int(n**0.5):  # число n имеет полный квадратный корень
        return n**0.5
    else:
        return F(n + 1) + 1

for i in range(5100 - 1, -1 , -1):
    F(i)

print(int(F(4850) + F(5000)))
'''


#5 https://stepik.org/lesson/1228671/step/7?unit=1242204
'''
from functools import *
@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return (n + F(n - 2)) // 5
    if n > 2 and n % 2 != 0:
        return (2 * n + F(n - 1) + F(n - 2)) // 4

for i in range(0, 100):
    F(i)

print(F(50))
'''



#6 https://stepik.org/lesson/1228671/step/8?unit=1242204
'''
from functools import *
@lru_cache(None)

def F(n):
    if n > 3456:
        return n + 1
    if n <= 3456 and n % 3 == 0:
        return F( n + 1) + F(n + 2)
    if n <= 3456 and n % 3 != 0:
        return F(n + n % 3) + 2

for i in range(3500 -1, -1 , -1):
    F(i)

print(F(12) - F(17))
'''


#7 https://stepik.org/lesson/1228671/step/9?unit=1242204
'''
def F(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + F(2 * n)
def G(n):
    return F(n) // n

r = G(2000)

cnt = 0
for n in range(1, 10000+1):
    if G(n) == r:
        cnt += 1
print(cnt)
'''


#10 https://stepik.org/lesson/1228671/step/11?unit=1242204
'''
from math import factorial
from functools import *
@lru_cache(None)
def F(n):
    if n >= 5000:
        return factorial(n)
    if 1 <= n < 5000:
        return 2 * F(n + 1) // (n + 1)

for n in range(5000-1, -1, -1):
    F(n)

print(1000 * F(7) // F(4))
'''

#12 https://stepik.org/lesson/1228671/step/13?unit=1242204
'''
from functools import *

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + F(n - 1)

for n in range(2025):
    F(n)

r = F(2023)
cnt = 0
for n in range(1, 101):
    if (r // F(n)) % 2 == 0:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/5b359b5d-e6d1-4701-9d12-c1b1db50e775
'''
sym = 116
alp = 16 + 2035
print(alp, 2 ** 12)
i = 12  # i - это кол-во бит на один символ
bit = sym * i
print(bit / 8)
byte = 174
print((byte * 65536) / 2 ** 20)  # 10.875 -> 11
'''

# https://education.yandex.ru/ege/inf/task/8573fa7f-3072-44f1-af39-6d9c62588c9a

sym = 289
alp = 1015 + 10
i = 11
bit = sym * i
print(bit / 8) # 397.375 -> 398
byte = 398

print((byte * 524_288) / 2 ** 20)


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25, 27]
# КЕГЭ = [22, 6, 7, 10, 11, 12, 17]
# на следующем уроке: 11 номер прототипы обратные 22, 17


# region 📖 Пробник (Вариант 2)

# Студент #Софья
# Дата: #Пятница #27Февраля2026
# ✅ Верно: 1, 2, 3, 5, 7, 8, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 4, 6, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# Студент #Лиза
# Дата: #Понедельник #02Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 11, 13, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 9, 10, 12, 14, 17, 22, 24, 26, 27
# ❔ Без ответа: Нет
# Итог: 16/29 первичных балла ~ 67 вторичных

# endregion 📖 Пробник (Вариант 2)
