# region Домашка: ******************************************************************

'''
s = input()
print(f"Символ + встречается {s.count('+')} раз")
print('Символ * встречается', s.count('*'), 'раз')
'''


# Поиск длинного слова
# https://stepik.org/lesson/1309454/step/9?unit=1324570
'''
a = input()
words = a.split()
maxi = len(words[0])
for w in words:
    # if len(w) > maxi:
    #     maxi = len(w)
    maxi = max(maxi, len(w))
print(maxi)
'''


'''
n = int(input())
num = ''
while n > 0:
    num = str(n % 3) + num
    n //= 3
print(num)
'''

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

# Задание 12 https://education.yandex.ru/ege/task/6cb04d25-0f77-4e49-9517-6908c16815de

# Дана программа для Редактора:

# ПОКА нашлось(444) ИЛИ нашлось(222)
#    заменить(444, 2)
#    заменить(222, 4)

# Исходная состоит из 31 цифры 4.
# Какая строка получится в результате выполнения алгоритма?
'''
s = '4' * 31
while '444' in s or '222' in s:
    s = s.replace('444', '2', 1)
    s = s.replace('222', '4', 1)
print(s)
'''


# Задание 12 https://education.yandex.ru/ege/task/ebd5c150-9b1a-44f5-99f9-b0c6adfa95d9
# Определите, сколько различных строк может получиться в результате её работы.
'''
my_set = set()
for n in range(4, 1000):
    s = '4' + '9' * n

    while '44' in s or '9299' in s or '49' in s:
        s = s.replace('49', '944', 1)
        s = s.replace('44', '2', 1)
        s = s.replace('9299', '4', 1)
    my_set.add(s)
print(len(my_set))
'''


# https://education.yandex.ru/ege/task/99da765f-ae28-4087-9286-3b636b34b035
'''
for n in range(4, 1000):
    s = '2' + '5' * n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if s.count('3') == 2:
        print(n)
        break
'''


# https://education.yandex.ru/ege/task/c21fb755-a462-4ee3-97b3-4c3be812dd68
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
