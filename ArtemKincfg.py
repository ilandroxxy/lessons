# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# https://education.yandex.ru/ege/task/9dc9bcae-00bb-4e7a-b93e-9e03ec567fad

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 1000):
    s = convert(n, 4)
    if n % 3 == 0:
        s = s[-1] + s[1:-1] + s[0] + '1'
    else:
        s = s + str(n % 3)
    r = int(s, 4)
    if r < 340:
        M.append(r)
print(max(M))
'''


# https://education.yandex.ru/ege/task/326fe818-6354-4d1c-b1ff-3d8d646f1705
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[:16])

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


M = []
for n in range(1, 1000):
    s = convert(n, 2)
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        x = (n % 3) * 3
        s = s + convert(x, 2)
    r = int(s, 2)
    if r > 151:
        M.append(r)

print(min(M))
'''


# https://education.yandex.ru/ege/task/12b3aabc-7777-4808-b29a-29993b289cca
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


n = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
s = convert(n, 25)
print(s.count('0'))
'''


# https://education.yandex.ru/ege/task/d90014d9-5105-4860-a4d3-f9cd62ad463e
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')


def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(2030+1):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        print(x)
'''


# https://education.yandex.ru/ege/task/749a92f0-0083-4931-90cf-8c987a48ed9c
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

M = []
for x in alphabet[:16]:
    for y in alphabet[:16]:
        A = int(f'27A{x}23', 16)
        B = int(f'8{y}E5D2', 16)
        if (A + B) % 5 == 0:
            M.append(alphabet.index(x) + alphabet.index(y))
print(max(M))
'''


# https://education.yandex.ru/ege/task/29fa61ad-cac1-4b57-a9ac-673ff4abd400
'''
def prime(x):
    if x < 1:
        return False
    for g in range(2, x):
        if x % g==0:
            return False
    return True


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

cnt = 0
for x in alphabet[:18]:
    A = int(f'56{x}3', 18)
    B = int(f'4{x}9', 18)
    C = int(f'57{x}1', 18)
    if prime(A + B - C):
        cnt += 1
print(cnt)
'''


# Тип 14 №48392
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:9]:
    for y in alphabet[:9]:
        A = int(f'2{y}66{x}', 9)
        B = int(f'{x}0{y}1', 12)
        if (A + B) % 170 == 0:
            print((A + B) // 170)
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
