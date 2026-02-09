
# Генераторы списков, про строки и практиковаться.
'''
# i  0   1    2   3  4
M = [2, 'a', 5.3, 5, 8]

print(len(M))  # 5


# range(0, STOP-1, 1)
for i in range(len(M)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # 2 a 5.3 5 8
print()

for x in M:
    print(x, end=' ')  # 2 a 5.3 5 8
print()

for x in M:
    if x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(x, end=' ')  # 2 5 8
print()


n = 345
if n % 2 == 0:
    print('Кратно 2 | Делится на 2 | Четные')
if n % 5 == 0:
    print('Кратно 5 | Делится на 5')
'''



# Создать список из 5 целых элементов c клавиатуры
'''
n = int(input('Введите кол-во элементов: '))
M = []  # M = list()
for i in range(n):  # повтори n раз
    x = int(input('x: '))
    M.append(x)  # Добавляем x в конец списка M
print(M)
'''

'''
M = [int(input('x: ')) for x in range(int(input('n: ')))]
print(M)
# n: 4
# x: 7
# x: 8
# x: 234
# x: 9
# [7, 8, 234, 9]
'''

# Генератор - это способность создавать списки в одну строчку

# генератор[что_кладем откуда_берем]
# генератор[что_кладем откуда_берем при_каком_условии]
'''
M = [i for i in range(5)]  # [0, 1, 2, 3, 4]

M = [i for i in range(10) if i % 2 == 0]  # [0, 2, 4, 6, 8]

M = [i**2 for i in range(10) if i % 2 == 0]  # [0, 4, 16, 36, 64]
'''


# Открываем последовательность целых чисел из текстового файла
'''
M = [int(s) for s in open('files/17.txt')]
print(f'Кол-во элементов в списке М: {len(M)}')

print([x for x in M if x > 0])  # [74975, 27470, 71321, 78494, 57313, 16861, 82229,
print([x for x in M if x < 0])  # [-46704, -51825, -94329, -70014, -16227, -19635,

print(f'Кол-во четных элементов: {len([x for x in M if x % 2 == 0])}')
print(f'Кол-во нечетных элементов: {len([x for x in M if x % 2 != 0])}')

print([x for x in M if len(str(abs(x))) == 4])  # [1843, -2390, 1080, -1511, 9481, -4241, -6842,

print([x for x in M if abs(x) % 10 == 2])  # [-67892, 48842, -29032, 52602, -6842, 97622,
print([x for x in M if abs(x) % 100 == 42])  # [48842, -6842, 83342, 19042, -86642, 65242,
print([x for x in M if abs(x) % 1000 == 342])  # [83342, 45342, -56342, 67342, -29342,

print([x for x in M if x % 5 == 0])  # [74975, -51825, 27470, -19635, -43205, 51135,

print([x for x in M if len(str(abs(x))) == 4 and abs(x) % 100 == 42 and x > 0])  # [8842, 8242, 2142]
'''

for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]

    copied1 = [x for x in M if M.count(x) == 1]  # Числа без повторений
    copied2 = [x for x in M if M.count(x) == 2]  # Числа встречаются два раза
    copide3 = [x for x in M if M.count(x) == 3]  # Числа встречаются три раза
    if len(copide3) == 3 and len(copied2) == 2 and len(copied1) == 1:
        print(M)  # [22, 49, 22, 22, 32, 49]


for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
    print(x, y, type(x))































