# region Домашка: ******************************************************************

# https://stepik.org/lesson/1038703/step/2?unit=1062210

# from string import *
# alphabet = digits + ascii_uppercase

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]



n = 11*15**65 + 18*15**38 - 14*15**17 + 19*15 ** 11 + 18338
s = convert(n, 15)
# print(s)
# print(set(s))
print(len(set(s)))
'''


# https://stepik.org/lesson/1038703/step/4?unit=1062210
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
m = []
for x in alphabet[:7]:
    for y in alphabet[:7]:
        a = int(f'{y}{x}320', 7)
        b = int(f'1{x}3{y}3', 9)
        if (a + b) % 181 == 0:
            m.append((a + b) // 181)
print(min(m))
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
m = []

for x in alphabet[:8]:
    for y in alphabet[:8]:
        a = int(f'{y}04{x}5', 11)
        b = int(f'253{x}{y}', 8)
        if (a + b) % 117 == 0:
            m.append((a + b) // 117)
print(min(m))
'''
# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

from fnmatch import *
for x in range(1917, 10**10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x, x // 1917)





# endregion Урок: ********************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14, 25.1]
# КЕГЭ  = []
# на следующем уроке:
