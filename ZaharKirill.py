# region Домашка: ******************************************************************

'''
n = int(input())  # кол-во элементов в списке
R = []
for i in range(n):
    x = int(input())
    R.append(x)
print(R)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 5 https://education.yandex.ru/ege/task/0aee931e-3422-4216-ba75-793cf3df8188
'''
M = []
for n in range(26, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 != 0:
        s = s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)  # Перевод из 2-й в 10-ю
    M.append(r)
print(min(M))
'''

# Задание 5 https://education.yandex.ru/ege/task/0aee931e-3422-4216-ba75-793cf3df8188
'''
M = []
for n in range(26, 1000):
    s = f'{n:b}'  # s = bin(n)[2:]
    if n % 2 != 0:
        s = s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)  # Перевод из 2-й в 10-ю
    M.append(r)
print(min(M))
'''

# Задание 5 https://education.yandex.ru/ege/task/70da2546-57ff-4c1f-a941-5e7c3809d06a
'''
n = 232
s = hex(n)[2:]
for x in '0123456789':
    s = s.replace(x, '')
if len(s) > 0:
    r = int(s, 16)
    print(r)
'''

# Задание 5 https://education.yandex.ru/ege/task/b6dd36d9-014f-45db-a9d2-9eb8eb02cb23
'''
for n in range(130+1, 255+1):
    s = f'{n:b}'.zfill(8)
    s = s[:2] + s[-2:]
    r = int(s, 2)
    if r == 10:
        print(n)
        break
'''



# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [2, 6]
# КЕГЭ  = []
# на следующем уроке:
