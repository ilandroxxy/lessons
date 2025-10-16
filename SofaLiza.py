# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://stepik.org/lesson/1038432/step/7?unit=1060804
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    summa = sum(map(int, s))
    if summa % 2 == 0:
        s = '10' + s[2:] + '1'
    else:
        s = '1' + s[2:] + '11'
    r = int(s, 2)
    if r >= 100:
        RES.append(n)
print(min(RES))
'''


# https://stepik.org/lesson/1038432/step/8?unit=1060804
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    summa = sum(map(int, s))
    if n % 2 == 0:
        s = '1' + s + '00'
    else:
        s = s + bin(summa)[2:]
    r = int(s, 2)
    if n > 8 and r > 88:
        RES.append([r, n])
print(min(RES)[1])
'''


# https://stepik.org/lesson/1038432/step/12?unit=1060804
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]  # 11100100  2
    for i in range(2):
        summa = sum(map(int, s))
        if summa % 2 == 0:
            s = '11' + s[2:] + '00'
        else:
            s = '10' + s[2:] + '11'
    r = int(s, 2)
    if n < 100:
        RES.append(r)
print(max(RES))
'''


# https://stepik.org/lesson/1038432/step/15?unit=1060804
'''
RES = []
for n in range(1, 10000):
    s = bin(n)[2:]
    summa = sum(map(int, s))
    if summa % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s, 2)
    if r > 50:
        RES.append(n)
print(min(RES))
'''

# https://stepik.org/lesson/1038703/step/15?unit=1062210
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for x in range(1, 2031):
    n = 3**100 - x
    s = convert(n, 3)
    if s.count('0') == 5:
        RES.append(x)
print(max(RES))
'''

# https://stepik.org/lesson/1038703/step/2?unit=1062210
'''
def convert(n, b):
    alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

n = (11 * 15 ** 65) + (18 * 15 ** 38) - (14 * 15 ** 17) + (19 * 15 ** 11) + 18338
s = convert(n, 15)
print(len(set(s)))
'''


# https://stepik.org/lesson/1038703/step/9?unit=1062210
'''
RES = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for y in alp[:17]:
    for x in alp[:15]:
        A = int(f'123{x}5', 15)
        B = int(f'67{y}9', 17)
        if(A + B) % 131 == 0:
            print((A + B) // 131)
            exit()
            # x y res
            # B 8 686
            # 0 A 685
'''




# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 14]
# КЕГЭ = []
# на следующем уроке:
