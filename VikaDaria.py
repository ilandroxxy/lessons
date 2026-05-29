# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************





# https://education.yandex.ru/ege/inf/task/2d8f6e0c-c37b-4caa-b0b1-6584a5d0261f
'''
s = open('files/24.txt').readline()
while 'AHAHA' in s:
    s = s.replace('AHAHA', 'AHAH HAHA')
print(max([len(x) for x in s.split()]))
'''

# https://education.yandex.ru/ege/inf/task/8fccd20b-438a-48a7-91f8-49e34350e04c
'''
s = open('files/24.txt').readline()
for x in 'ABC':
    s = s.replace(x, 'A')
while 'AA' in s:
    s = s.replace('AA', 'A A')
print(max([len(x) for x in s.split()]))
'''


# https://education.yandex.ru/ege/inf/task/7cecbe1f-be24-497e-8c28-cab3dc437d2f
'''
s = open('files/24 (2).txt').readline()
s = s.replace('CB', '**').replace('AB', '**')
for x in 'ABC':
    s = s.replace(x, ' ')
print(s)
print(max([len(x) for x in s.split()]) / 2)
'''

# https://education.yandex.ru/ege/inf/task/417b95a7-a644-43d9-b3f1-d1a1f753789a
'''
s = open('files/24 (2).txt').readline()
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alp[:14])
for x in alp[14:]:
    s = s.replace(x, ' ')

maxi = 0
cnt = 0
for x in s.split():
    print(x)
    if x.count('0') == len(x):
        continue
    if len(x) > 0:
        if x[0] == '0':
            while x[0] == '0':
                x = x[1:]
            if int(x, 14) > maxi:
                maxi = int(x, 14)
                cnt = len(x)
print(maxi)
print(cnt)
'''

# https://education.yandex.ru/ege/inf/task/97e2f438-d6ce-4c55-95f5-8384f58faea4
'''
s = open('files/24 (2).txt').readline().lower()
for x in '.,qwertyuiopasdfghjklzxcvbnm':
    s = s.replace(x, ' ')
print(max([int(x) for x in s.split()]))
'''

# https://education.yandex.ru/ege/inf/task/105730a4-97f7-485b-a86a-76c11682aa85
'''
s = open('files/24 (3).txt').readline()
cnt = 0
for i in range(len(s)-4):
    r = s[i:i+5]
    if r == r[::-1]:
        cnt += 1
print(cnt)
'''

'''
s = open('files/24 (3).txt').readline()
for x in 'LISENOK':
    s = s.replace(x, ' ')
print(s.split())
'''


# https://education.yandex.ru/ege/inf/task/dc2aa40a-ee08-4e9c-b43f-81fbccbd1d7e
# Определите максимальную длину непрерывной подпоследовательности,
# состоящей только из уникальных символов.

s = open('files/24 (3).txt').readline()
maxi = 0
r = ''
for i in range(len(s)-1):
    if s[i] not in r:
        r += s[i]
    else:
        maxi = max(maxi, len(r))
        # print(len(r), r)
        r = ''

s = open('files/24 (3).txt').readline()
s = s[::-1]
r = ''
for i in range(len(s)-1):
    if s[i] not in r:
        r += s[i]
    else:
        maxi = max(maxi, len(r))
        # print(len(r), r)
        r = ''
print(maxi)

# https://education.yandex.ru/ege/inf/task/c4cc7ed4-97b1-4c98-b7b9-188c7c795351




# https://education.yandex.ru/ege/inf/task/548407d7-a79e-4bad-a87e-36fe6daff4f6

# https://education.yandex.ru/ege/inf/task/5f634652-6430-443d-8104-073f02276328

# https://education.yandex.ru/ege/inf/task/48550711-264d-4ec6-920b-bdfe130304af











# Администратор/Грузоперевозки: =ЕСЛИ(B2<$E$1;1;"")
# Задачи: 24 2944 1275 1395 27636 1304 1207 788 225

# Коржи/Коробки: =ЕСЛИ(B1-A2>=8;A2;B1)
# Задачи: 27779 21910 16335 21424 15341 7096 4712 4604

# Магазин
# Задачи:

# Распределение мест  =ЕСЛИ(И(A2=A1;B2-B1=3);B2-2;"")
# Задачи: 1868, 2613, 7274, 3664, 3586, 3230

# Очередь в кассу
# Задачи:

# Организация сортировки
# Задачи:


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24.1, 25, 27]
# КЕГЭ = [6, 7, 9, 11, 14, 16, 25]
# на следующем уроке:  15 номера руками


# region 📖 Пробник (Вариант 2)

# Студент #Дарья
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 27
# ⛔️ Неверно: 3, 6, 7, 10, 24, 26
# ❔ Без ответа: Нет
# Итог: 22/29 первичных балла ~ 83 вторичных

# Студент #Маша
# Дата: #Четверг #05Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 21, 23
# ⛔️ Неверно: 10, 18
# ❔ Без ответа: 9, 17, 22, 24, 25, 26, 27
# Итог: 18/29 первичных балла ~ 72 вторичных

# Студент #Вика
# Дата: #Суббота #07Марта2026
# ✅ Верно: 1, 2, 6, 7, 8, 13, 14, 16, 17, 19, 20, 21, 25, 27
# ⛔️ Неверно: 5, 9, 12, 15, 23
# ❔ Без ответа: 3, 4, 10, 11, 18, 22, 24, 26
# Итог: 15/29 первичных балла ~ 65 вторичных

# endregion 📖 Пробник (Вариант 2)

