# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
n = 82433987
b = 16
r = ''
while n > 0:
    r += alp[n % b]
    n //= b
r = r[::-1]
print(r)
'''
from traceback import print_tb

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    r = r[::-1]
    return r

print(convert(8, 2))
'''

'''
n = 82433987
b = 16
R = []
while n > 0:
    R.append(n % b)
    n //= b
R = R[::-1]
print(R)
'''

'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    r = r[::-1]
    return r


r = convert(8, 2)
print(r)
'''

# № 14343 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    r = r[::-1]
    return r

n = 5 * 343**2031 + 4*49**2142 - 3*7**111 + 7**222
r = convert(n, 7)
print(sum(map(int, r)))
print(sum([int(x) for x in r]))
'''

# № 12923 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    r = r[::-1]
    return r

n = 3*3125**9 + 2*625**8 - 4*625**7 + 3*125**6 -2*25**5 - 2024
r = convert(n, 25)
print(r.count('0'))

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6, 8, 12, 14.1]
# КЕГЭ  = []
# на следующем уроке:
