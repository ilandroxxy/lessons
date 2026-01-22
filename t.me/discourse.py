

# Условные операторы (ветвление)
# if - если
# elif - иначе если
# else - иначе

'''
n = int(input('n: '))
if n > 0:
    print('Положительное')
elif n < 0:
    print('Отрицательное')
else:
    print('Число равно 0')



n = int(input('n: '))
if n > 0:
    print('Положительное')
if n < 0:
    print('Отрицательное')
if n == 0:
    print('Число равно 0')
'''


# Зачем необходим elif
'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, 6    # Вторая четверть
if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Точка лежит на осях')
print('Продолжение программы')
'''


# Каскадные условные операторы (каскады условий)
'''
x, y = -5, 6
if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('Первая четверть')
    else:  # x > 0 and y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0 and y > 0
        print('Вторая четверть')
    else:  # x <= 0 and y <= 0
        print('Третья четверть')
'''


# Пример считывания данных из файла и обработка
'''
clusters1 = []
clusters2 = []
clusters3 = []

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    if y > 23:
        clusters1.append([x, y])
    elif 16 < y < 23:
        clusters2.append([x, y])
    elif 10 < y < 16 and x > 23:
        clusters3.append([x, y])
'''


# Логические связки and, or, not, in, not in

flag = True
print(not flag)  # False
print(not(not flag))  # True

a, b, c = 3, 4, -5
if a > 0 and b > 0 and c > 0:
    print('and - все условия верные')
if a > 0 or b > 0 or c > 0:
    print('or - хотя бы одно из условий')

#   True   +  True   +  False  == 2
if (a > 0) + (b > 0) + (c > 0) == 2:
    print('Только лишь два выполняются')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Только один выполняются')
if (a > 0) + (b > 0) + (c > 0) == 3:
    print('Все условия выполняются')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('Хотя бы одно выполняется')


M = [1, 2, 1, 3, 2, 3, 3, 3, 2, 3, 4, 2, 3, 5, 4]

for x in M:
    if x in [0, 2, 4, 6, 8]:
        print(x, end=' ')  # 2 2 2 4 2 4
print()

for x in M:
    if x not in [0, 2, 4, 6, 8]:
        print(x, end=' ')  # 1 1 3 3 3 3 3 3 5
print()






