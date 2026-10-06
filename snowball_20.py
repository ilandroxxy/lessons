# region Домашка: ******************************************************************

#8946
'''
c = 0
for i in open('files/9.csv'):
    s = sorted([int(x) for x in i.split(';')])
    if s[-1]**2 > s[0]*s[1]*s[2]*s[3] and s[-1]+s[-2] > (s[0]+s[1]+s[2])*2:
        c += 1
print(c)
'''


#7697
'''
c = 0
for i in open('files/9.csv'):
    s = [int(x) for x in i.split(';')]
    if (sum(s) % 18 == 0)  or (len([x for x in s if x == 18]) == 5):
        c += 1
print(c)
'''

#5946
'''
c = 0
for i in open('files/9.csv'):
    s = [int(x) for x in i.split(';')]
    if len([x for x in s if s.count(x) == 1]) == len(s) and len([x for x in s if x % 2 == 0]) > len([x for x in s if x % 2 == 1]):
        c += 1
print(c)
'''

#23747
'''
for i in open('files/9.csv'):
    s = [int(x) for x in i.split(';')]
    a3 = [x for x in s if s.count(x) == 3]
    a1 = [x for x in s if s.count(x) == 1]
    if len(a3) == 3 and len(a1) == len(s) - 3 and sum(a1)/len(s) - 3 <= sum(a3) / 3:
        k = sum(s)
print(k)
'''

#7995
'''
c = 0
for i in open('files/9.csv'):
    s = sorted([int(x) for x in i.split(';')])
    # if len([x for x in s if s.count(x) == 1]) == len(s):
    if len(s) == len(set(s)):
        if (s[0]+s[-1])**2 >= s[1]*s[2]*s[3]:
            c += 1
print(c)
'''


# 6262
'''
c = 0
for i in open('files/9.csv'):
    s = [int(x) for x in i.split()]
    f = 0
    # if len([x for x in s if s.count(x) == 1]) != len(s):
    # if len(s) != len(set(s)):
    if len([x for x in s if s.count(x) > 1]) > 0:
        f += 1
    if len([x for x in s if x % 2 != 0]) == 3:
        f += 1
    if f == 1:
        c += 1
print(c)
'''


# 8609
'''
c = 0
for i in open('files/9.csv'):
    s = sorted([int(x) for x in i.split(';')])
    if len([x for x in s if s.count(x) == 1]) == len(s):
        if (s[0]+s[-1])*2 <= (s[1]+s[2]+s[3])*3:
            c += 1
print(c)
'''


# 31510
'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        if str(a)[-2] < str(a)[-1]:
            return F(a + 1, b) + F(int(str(a)[0] + str(a)[-1] + str(a)[-2]) , b)
        else:
            return F(a + 1, b)

print(F(100, 141))


def F(a, b):
    if a >= b:
        return a == b
    if str(a)[-2] < str(a)[-1]:
        return F(a + 1, b) + F(int(str(a)[0] + str(a)[-1] + str(a)[-2]) , b)
    else:
        return F(a + 1, b)

print(F(100, 141))
'''


# № 31367 Пересдача 08.07.26(Уровень: Средний)
'''
def F(a, b):
    if a >= b:
        return a == b
    if str(a).count('1') >= 1:
        return F(a + 1, b) + F(int(str(a).replace('1', '3')), b)
    else:
        return F(a + 1, b)

print(F(11, 94))
'''


# № 29977 Апробация 14.05.26(Уровень: Базовый)
'''
def F(a, b):
    if a <= b or a == 9:
        return a == b
    return F(a - 1, b) + F(a - 3, b) + F(a // 2, b)

print(F(19, 12) * F(12, 3))
'''

'''
def F(a, b):
    if a >= b or a == 10:
        return a == b
    return F(a + 1, b) + F(a + 2, b) + F(a * 2, b)

print(F(3, 7) * F(7, 20))


# Ответ: 792

print(792 / 6)  # 132
'''


# № 31128 Основная волна 18.06.26(Уровень: Средний)
# A. Прибавь 1
# B. Поменяй местами
# Первая из этих команд увеличивает число на экране на 1.
# Вторая команда применяется только к числу, у которого цифра в разряде
# десятков по значению меньше цифры, стоящей в разряде единиц,
# и действует, заменяя число на экране числом, в котором
# цифры двух младших разрядов поменялись местами.

# Сколько существует программ, для которых при исходное числе 100 результатом
# является число 150?

def f(a, b):
    if a >= b:
        return a == b
    if str(a)[-2] < str(a)[-1]:
        return f(a + 1, b) + f(int(str(a)[:-2] + str(a)[-1] + str(a)[-2]), b)
    else:
        return f(a + 1, b)

print(f(100, 150))





# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************




# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [9, 14, 22]
# КЕГЭ = []
# на следующем уроке:



