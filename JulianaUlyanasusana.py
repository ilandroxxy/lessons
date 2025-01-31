# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://stepik.org/lesson/1038709/step/14?unit=1062775
'''
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 3 * G(n - 1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) - 2 * G(n - 1)


x = F(18)
print(sum(map(int, str(x))))  # 18298549
'''


# Поиск суммы цифр строки
'''
s = '18298549'

summa = sum(map(int, s))

summa = sum([int(x) for x in s])

summa = 0
for x in s:
    summa += int(x)
'''

'''
def F(x, y, A):
    return ((108 % x == 0) <= (x % y != 0)) or (x + y > 80) or (A - y > x)


for A in range(1, 1000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''

# № 12469 (Уровень: Базовый)
'''            
            def F(x, a1, a2):
                D = 7 <= x <= 68  # x ∈ D
                C = 29 <= x <= 100
                A = a1 <= x <= a2
                return (D) <= (((not C) and (not A)) <= (not D))
            
            
            R = []
            M = [x / 10 for x in range(5 * 10, 110 * 10)]
            print(M)
            for a1 in M:
                for a2 in M:
                    if all(F(x, a1, a2) for x in M):
                        R.append(a2 - a1)
            
            print(min(R))  # 21.8 -> 21.75 -> 21.9 -> 22
'''

'''
print('x y z w F1 F2')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F1 = (w == x) and (y <= z)
                F2 = (w <= x) <= (y == z)
                print(x, y, z, w, int(F1), ' ', int(F2))
'''


# номер 8
# Андрей составляет 7-буквенные коды из букв А, Н, Д, Р, Е, Й.
# Буквы А и Й должны встречаться в коде ровно по одному разу,
# при этом буква Й не может стоять на первом месте.
# Остальные допустимые буквы могут встречаться произвольное
# количество раз или не встречаться совсем.
# Сколько различных кодов может составить Андрей?
'''
s = 'АНДРЕЙ'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            word = a + b + c + d + e + f + g
                            if word.count('А') == 1 and word.count('Й') == 1:
                                if a != 'Й':
                                    cnt += 1
print(cnt)  # 36864
'''

# номер 14
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:13]:
    A = int(f'8{x}71', 13)
    B = int(f'3{x}DF', 17)
    if (A + B) % 197 == 0:
        print((A + B) // 197)
'''


'''
def F(x, a1, a2):
    A = a1 <= x <= a2
    return (A <= (x**2 <= 100)) and ((x**2 <= 64) <= A)


R = []
for a1 in range(1, 1000):
    for a2 in range(1, 1000):
        if all(F(x, a1, a2) for x in range(1, 1000)):
            R.append(a2 - a1)
print(max(R))
'''

'''
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return F(n / 3)
    if n % 3 > 0:
        return (n % 3) + F(n - (n % 3))


for n in range(1, 1000):
    if F(n) == 11:
        print(n)
        break
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 13, 14, 15, 16, 23, 25]
# КЕГЭ  = []
# на следующем уроке:


# Первый пробник 21.12.24:
# Ульяна 5/8 -> 14 вторичных баллов +[1, 2, 4, 6, 12] -[5, 13, 14]
