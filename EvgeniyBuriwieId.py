# region Домашка: ************************************************************

# https://stepik.org/lesson/1227099/step/3?unit=1240617
'''
s = sorted("ПАРУС")
k = 0
R = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    k += 1
                    if "АА" not in slovo and slovo.count('У') <= 1:
                        R.append(k)

print(max(R))
'''

'''
s = '>234'
summa = sum([int(x) for x in s if x.isdigit()])
print(summa)  # ValueError: invalid literal for int() with base 10: '>'
'''

# https://stepik.org/lesson/1171547/step/5?unit=1183971
'''
def IsPrime(n):  # 8
    if n <= 1:
        return False
    for j in range(2, n):  # исключил 1 и n
        if n % j == 0:
            return False
    return True


for n in range(1, 10000):
    s = ">" + "1" * 16 + "2" * n + "3" * 16
    while ">1" in s or ">3" in s or ">2" in s:
        if ">1" in s:
            s = s.replace(">1", "1>", 1)
        if ">3" in s:
            s = s.replace(">3", ">2", 1)
        if ">2" in s:
            s = s.replace(">2", ">1", 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if IsPrime(summa):
        print(n)
        break
'''


# https://stepik.org/lesson/1171547/step/3?unit=1183971
'''
s = "7" * 333
while "66" in s or "77777" in s:
    if "66" in s:
        s = s.replace("66", "7", 1)
    else:
        s = s.replace("77777", "676676", 1)


total = 1
for x in s:
    total *= int(x)
print(total)
'''


# https://stepik.org/lesson/1038816/step/3?unit=1062780
'''
from fnmatch import *
cnt = 0
for x in range(700_011, 10**9, 13):
    if not fnmatch(str(x), "*0??3*") and not fnmatch(str(x), "*4??2") and not fnmatch(str(x), "*1*"):
        print(x, sum(int(i) for i in str(x)))
        cnt += 1
        if cnt == 5:
            break
'''


'''
from fnmatch import*
for x in range(237, 10**8, 237):
    if fnmatch(str(x), "81?2*80") and not fnmatch(str(x), "*9*"):
        print(x, x // 237)
'''


# https://stepik.org/lesson/1038816/step/12?unit=1062780
'''
from fnmatch import*
R = []
for x in range(11071, 10**10,  11071):
    if fnmatch(str(x), "?136*1"):
        if str(x)[0] in '13579' and str(x)[-2] in '02468':
            R.append([x, x // 11071])

print(*R[-5])
print(*R[-4])
print(*R[-3])
print(*R[-2])
print(*R[-1])
'''


print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))

# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23, 25.1]
# КЕГЭ = [12]
# на следующем уроке:
