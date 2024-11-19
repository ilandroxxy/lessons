# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 12 https://education.yandex.ru/ege/task/50a1b75e-3829-4e52-96bc-44d8e024790e
'''
s = '3' * 70

while '333' in s or '77777' in s:
    if '333' in s:
        s = s.replace('333', '77', 1)
    else:
        s = s.replace('77777', '7', 1)
print(s)
print(s.count('7'))
print(sum(map(int, s)))
print(sum([int(x) for x in s]))
'''


# Задание 12 https://education.yandex.ru/ege/task/0dae60c5-8bfc-40e6-9913-2395abbd6a99
'''
for n in range(4, 10000):
    s = '5' + '2' * n

    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    summa = sum([int(x) for x in s])
    if summa == 64:
        print(n)
'''


# Задание 12 https://education.yandex.ru/ege/task/c21fb755-a462-4ee3-97b3-4c3be812dd68
'''
for x in range(50):
    for y in range(50):
        for z in range(50):
            s = '0' + '1' * x + '2' * y + '3' * z

            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1201', 1)
            if s.count('1') == 31 and s.count('2') == 24 and s.count('3') == 46:
                print(z)
'''

# Функция проверки на простое число
'''
def is_prime(x):  # 8
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


print(is_prime(4))  # False
print(is_prime(7))  # True
print([x for x in range(100) if is_prime(x)])
'''

# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [8, 12]
# КЕГЭ  = []
# на следующем уроке: 5, 14
