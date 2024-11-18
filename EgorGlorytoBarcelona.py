# region Домашка: ******************************************************************

'''
L=[]
for n in range(4, 10000):
    s= '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s=s.replace('52', '11', 1)
        if '2222' in s:
            s=s.replace('2222', '5', 1)
        if '1122' in s:
            s=s.replace('1122', '25', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if summa % 10 == 7:
        print(n)
        break
'''


# Задание 5 https://education.yandex.ru/ege/task/da1c175a-d87f-46d0-9211-35a2d2a5b554
'''
for n in range(1, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 5 == 0:
        s = s + s[-3:]
    else:
        x = (n % 5) * 5
        s = s + f'{x:b}'
    r = int(s, 2)

    if r > 256:
        print(n)
        break
'''


# Задание 5 https://education.yandex.ru/ege/task/5f631ae3-da90-45d6-84fa-5c18717831b8
'''
cnt = 0
for n in range(1, 10000):
    s = f'{n:o}'  # s = oct(n)[2:]
    if n % 2 == 0:
        s = s + '00'
    else:
        s += '10'
    r = int(s, 8)

    if 100 <= r <= 999:
        cnt += 1
print(cnt)
'''

# Задание 5 https://education.yandex.ru/ege/task/3ef214b5-fef2-4500-9f74-5be832f60ef6
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


M = []
for n in range(1, 1000):
    s = convert(n, 5)
    if len(s) % 2 == 0:
        s = s[:len(s) // 2] + '0' + s[len(s) // 2:]

    r = int(s, 5)
    if r <= 250:
        M.append(n)
print(max(M))
'''


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
# ФИПИ = [2, 4, 6, 12]
# КЕГЭ  = []
# на следующем уроке:
