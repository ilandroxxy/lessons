




# Условные операторы: if, elif, else
'''
n = int(input('n: '))
if n > 0:  # если
    print('Положительное число')
elif n == 0:  # иначе если
    print('Равно нулю')
else:  # иначе
    print('Отрицательное число')
'''

'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = 5, 6

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Число лежит на осях')
print('Конец выполнения программы')
'''


# Логические связки: and, or, not, in, not in, ==, !=
'''
print(4 == 4)  # True
print(4 != 4)  # False

print(4 == 10)  # False
print(4 != 10)  # True

print(72 % 2 == 0)  # True - число делится на 2
print(73 % 2 == 0)  # False - число не делится на 2


print(True + True + False + True)  # 3

a, b, c = 4, 5, 6

if a > 0 and b > 0 and c > 0:
    print('AND - все условия выполняются')
if a > 0 or b > 0 or c > 0:
    print('OR - хотя бы одно условие выполняется')

if (a > 0) + (b > 0) + (c > 0) == 3:
    print('все условия выполняются')
if (a > 0) + (b > 0) + (c > 0) == 1:
    print('Выполняется только одно из условий')
if (a > 0) + (b > 0) + (c > 0) >= 1:
    print('хотя бы одно условие выполняется')
if (a > 0) + (b > 0) + (c > 0) <= 2:
    print('Не более двух выполняется')


flag = True
print(not flag)  # False
print(not(not flag))  # True


s = '334sf165sf561e2'
for x in s:
    print(x, end=' ')  # 3 3 4 s f 1 6 5 s f 5 6 1 e 2
print()

for x in s:
    if x in '0123456789':
        print(x, end=' ')  # 3 3 4 1 6 5 5 6 1 2
print()


for x in s:
    if x not in '0123456789':
        print(x, end=' ')  # s f s f e
print()


s = '3209482390'
print([x for x in s])  # ['3', '2', '0', '9', '4', '8', '2', '3', '9', '0']
# print(sum([x for x in s]))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([int(x) for x in s])   # [3, 2, 0, 9, 4, 8, 2, 3, 9, 0]
print(sum([int(x) for x in s]))  # 40


s = '320f94s8w23f90'
# print(sum([int(x) for x in s]))  # ValueError: invalid literal for int() with base 10: 'f'
print(sum([int(x) for x in s if x in '0123456789']))  # 40
'''

