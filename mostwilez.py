




# Условыне операторы: if, elif, else (ветвеление)
'''
n = int(input('n: '))
if n > 0:  # если
      print('Число положительное')
elif n < 0:  # иначе если
      print('Число отрицательное')
else:  # иначе
      print('Число равно нулю')
'''


# Зачем нужен elif
'''
# x = int(input('x: '))
# y = int(input('y: '))
x, y = -5, -6
if x > 0 and y > 0:
      print('Первая четверть')
elif x < 0 and y < 0:
      print('Третья четверть')
elif x > 0 and y < 0:
      print('Четвертая четверть')
elif x < 0 and y > 0:
      print('Вторая четверть')
else:
      print('Лежит на осях')
print('Конец программы.')
'''


# Логические связкеи: and, or, not, in, not in, ==, !=
'''
a, b, c = 4, 5, 4

# = - присваивание значения переменной
# == - сравнение значений (равны ли они?)
# != - сравнение значений (не равны ли они?)

print(a == c)  # True
print(a == b)  # False

print(a != b)  # True
print(c != b)  # True


#       1      1      0       1
print(True + True + False + True)  # 3

a, b, c = 4, 5, 4

if a > 0 and b > 0 and c > 0:
      print('AND - выполняются все условия')
if a > 0 or b > 0 or c > 0:
      print('OR - выполняются хотя бы одно условие')

if (a > 0) + (b > 0) + (c > 0) == 0:
      print('Не выполнилось ни одного условия')
if (a > 0) + (b > 0) + (c > 0) == 3:
      print('Выполнились все условия')
if (a > 0) + (b > 0) + (c > 0) == 1:
      print('Выполнилось только одно условие')
if (a > 0) + (b > 0) + (c > 0) >= 1:
      print('Выполнится хотя бы одно условие')
if ((a > 0) + (b > 0) + (c > 0)) in (1, 2, 3):
      print('Выполнится хотя бы одно условие')




flag = True
print(not flag)  # False
print(not(not flag))  # True

# Сумму цифр строки

s = '230sdf94823sf9084egd72'
for x in s:
      print(x, end=' ')  # 2 3 0 s d f 9 4 8 2 3 s f 9 0 8 4 e g d 7 2
print()


for x in s:
      if x in '0123456789':
            print(x, end=' ')  # 2 3 0 9 4 8 2 3 9 0 8 4 7 2
print()


for x in s:
      if x not in '0123456789':
            print(x, end=' ')  # s d f s f e g d
print()




s = '92103821903812'
summa = 0
for x in s:
      summa += int(x)  # 49
print(summa)


s = '92103sdf8219038dsf12'
summa = 0
for x in s:
      if x in '0123456789':
            summa += int(x)  # 49
print(summa)
'''




