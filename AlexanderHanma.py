# region Домашка: ******************************************************************
'''
x = int(input())
summ = 0
a = x // 10000
b = (x // 1000) % 10
c = (x // 100) % 10
d = (x // 10) % 10
e = x % 10

if a+b+e == c-d:
    print('Да')
else:
    print('Нет')
'''

'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
r = 1
if a > 0:
    r *= a
if b > 0:
    r *= b
if c > 0:
    r *= c
if d > 0:
    r *= d
print(r)
'''

'''
a = int(input())
if (99 < a < 1000) and (a % 5 == 0 or a % 13 == 0):
    print('Да')
else:
    print('Нет')
'''

'''
a = int(input())
b = int(input())
c = int(input())
summ = 0
if (a % 5 == 0 and a % 20 != 0) or a % 160 == 0:
    summ += a

if b % 5 == 0 and b % 20 != 0 or b % 160 == 0:
    summ += b

if c % 5 == 0 and c % 20 != 0 or c % 160 == 0:
    summ += c
print(summ)
'''
'''
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
if a > b:
    for i in range(b, a + 1):
        print(i)
'''

n = int(input())
R = []
while n > 0:
    c = n % 10
    print(c)
    n //= 10
print(max(R))
print(min(R))
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ  = []
# на следующем уроке:
