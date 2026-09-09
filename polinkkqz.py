
# Условные операторы или ветвление: if, elif, else

'''
n = int(input('n: '))
if n > 0:  # если
    print('Число положительное')
elif n < 0: # иначе если
    print('Число отрицательное')
else:  # иначе
    print('Число равно нулю')
'''

'''
x, y = 5, -4

if x > 0 and y > 0:
    print('Первая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
else:
    print('Лежит на осях')
print('Продолжение программы')
'''

# https://stepik.org/lesson/1309432/step/5?unit=1324548
'''
n = int(input())
a = n // 10000
b = (n // 1000) % 10
c = (n % 1000) // 100
d = (n % 100) // 10
e = n % 10
if a * c == b + d + e:
    print('Да')
# if a * c != b + d + e:
#     print('Нет')
else:
    print('Нет')
'''


# Логические связки: and, or, not, not in, in, ==, != и тд

# a = 5 - присваивание значения переменной
# a == 5 - сравнение значений переменных (равны ли они)
# a != 5 - сравнение значений переменных (не равны ли они)
# a > 5 - проверяем, что а больше 5
# a >= 5 - проверяем, что а больше или равно 5
'''
flag = True
print(not flag)  # False
print(not not flag)  # True
'''

'''
s = '329487234'

for x in s:
    if x in '02468':
        print(x, end=' ')  # 2 4 8 2 4     
print()


for x in s:
    if x not in '02468':
        print(x, end=' ')  # 3 9 7 3 
print()
'''

'''
s = '329487234'

for x in s:
    if x in '02468':
        print(f'{x} - число четное')
    else:
        print(f'{x} - число нечетное')
print()
'''

'''
a, b, c = -4, -5, -6
if a > 0 and b > 0 and c > 0:
    print('AND')  # - это связка, которая проверяет, что ВСЕ условия выполняются
if a > 0 or b > 0 or c > 0:
    print('OR')  # - хотя бы одно условие доложно быть верное (выполняться)
'''