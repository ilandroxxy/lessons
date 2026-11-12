



# Цикла for отвечает на запросы: "повтори n раз", "пробеги от А до В"

# range(0, STOP-1, 1)
# range(START, STOP-1, 1)
# range(START, STOP-1, STEP)

'''
for i in range(10):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()


for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(1, 10+1, 2):
    print(i, end=' ')  # 1 3 5 7 9
print()


for i in range(10-1, 0-1, -1):  # Перебери числа меньше 10
    print(i, end=' ')  # 9 8 7 6 5 4 3 2 1 0
print()


s = '12478924'

for x in s:
    print(x, end=' ')  # 1 2 4 7 8 9 2 4
print()

summa = 0
for x in s:
    summa += int(x)
print(summa)  # 37


s = '124sdfsdf .8924'
for x in s:
    if x in '0123456789':
        summa += int(x)
print(summa)  # 67
'''


# Цикл while: "ПОКА условие верное делаем действие", "бесконечный цикл"
'''
for i in range(2, 10+1, 2):
    print(i, end=' ')  # 2 4 6 8 10
print()


n = 2
while n <= 10:
    print(n, end=' ')  # 2 4 6 8 10 
    n += 2
print()
'''


# Бескончные циклы и операторы break continue и функция exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итеррцию (шаг) цикла 
    if k == 100_000:
        break  # Выполнгение цикла в котором находится
    if k == 50_000:
        exit()  # Полностью прервал выполнение программы
    print(k)
print('Выход из цикла')
'''









