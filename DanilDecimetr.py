# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
a = [int(i) for i in open("17_19486.txt")]
x7 = [x for x in a if abs(x) % 10 == 7]
l = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    # if ((x < 0 and y > 0) or (x > 0 and y < 0)):
    if (x > 0) + (y > 0) == 1:
        if x + y < len(x7):
            l.append(x + y)
print(len(l), max(l))
'''


'''
f = open("17_17680.txt")
a = [int(i) for i in f]
m = min(x for x in a if x > 0 and x % 41 == 0)
l = []
for i in range(len(a)-1):
    if a[i] != a[i+1] and (a[i]-a[i+1]) % m == 0:
        l.append(a[i]+a[i+1])
print(len(l), max(l)) 

# Мои небольшие правки 
a = [int(i) for i in open("17_17680.txt")]
m = min(x for x in a if x > 0 and abs(x) % 41 == 0)
l = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if x != y and abs(x - y) % m == 0:
        l.append(x + y)
print(len(l), max(l))
'''


# № 23757 Демоверсия 2026 (Уровень: Базовый)
'''
a = [int(i) for i in open('0. files/17.txt')]
b = [x for x in a if len(str(abs(x))) == 2]
l = []
for i in range(len(a)-1):
    x, y = a[i], a[i+1]
    if (x in b) + (y in b) == 1:
        if (x + y) % min(b) == 0:
            l.append(x + y)
print(len(l), max(l))
'''


a = [int(i) for i in open('0. files/17.txt')]
m = [x for x in a if len(str(abs(x))) == 5]
b = [x for x in a if str(x)[-3:] == '238' or abs(x) % 1000 == 238]
l = []
for i in range(len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (x in m) + (y in m) + (z in m) in (1, 2):
        n3 = [i for i in (x, y, z) if i % 3 == 0]
        n5 = [i for i in (x, y, z) if i % 5 == 0]
        if len(n3) > len(n5):
            if (x + y + z) > max(b):
                l.append(x + y + z)
print(len(l), max(l))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = []
# КЕГЭ = []
# на следующем уроке: Домашка по спискам