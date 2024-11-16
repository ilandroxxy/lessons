# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 14 https://education.yandex.ru/ege/task/83d644e9-902c-44d8-a9e5-d7f946811a29
'''
n = 7**21 + 49**13 - 7**10
b = 7
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()
print(sum(M))
'''


# Задание 14 https://education.yandex.ru/ege/task/5e073e81-80b9-451e-96c3-7949af5d9b22
'''
cnt = 0
for x in range(1, 100):
    n = 5**3 + 4**2 + 3 ** 1 - x
    b = 5
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    r = r[::-1]
    if int(r, 5) % 2 == 0:
        cnt += 1
print(cnt)
'''


# Задание 14 https://education.yandex.ru/ege/task/5b214f5e-974b-46db-bf04-5aa73d9d99d3
'''
n = 3 * 15**1140 + 2*15**1025 +15**923 - 3*15**85 + 2 * 15 ** 74 + 3
b = 15
M = []
while n > 0:
    M.append(n % b)
    n //= b
M.reverse()

count = 1
maxi = 0
for i in range(len(M)-1):
    if M[i] == M[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''


# Задание 14 https://education.yandex.ru/ege/task/945d02c3-876e-4bd3-8a57-0e076865e42a
'''
for x in range(2030+1):
    n = 6**260 + 6 ** 160 + 6 ** 60 - x
    b = 6
    M = []
    while n > 0:
        M.append(n % b)
        n //= b
    M.reverse()
    if M.count(0) == 202:
        print(x)
        break
'''


# Задание 14 https://education.yandex.ru/ege/task/e07ffce3-c3fb-4aad-933f-4291ee998760
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alphabet[:14]:
    for y in alphabet[:14]:
        A = int(f'14{y}5{x}2', 14)
        B = int(f'31{x}2{y}3', 14)
        if (A + B) % 9 == 0:
            R.append((A + B) // 9)
print(max(R))
'''


# Тип 14 №48387
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in alphabet[:11]:
    for y in alphabet[:11]:
        A = int(f'{x}341{y}', 11)
        B = int(f'56{x}1{y}', 19)
        if (A + B) % 305 == 0:
            R.append((A + B) // 305)
print(min(R))
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 5, 6, 8, 12, 14]
# КЕГЭ  = []
# на следующем уроке:
