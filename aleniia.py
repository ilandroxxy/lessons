


# x = 5 - переменная нужна для хранения и использования данных удобным способом

# - однострочный комментарий

'''
- многострочный комментарий
'''


# Типы данных переменных
'''
a = 5  # int (integer) - целочисленные значения
print(type(a))  # <class 'int'>
print(type(2 + 2))  # <class 'int'>


b = 5.0  # float (число с плавающей точкой) - вещественное значние/дробь
print(7 / 2)  # 3.5
print(4 / 2, type(4 / 2))  # 2.0 <class 'float'>


c = '5'  # str (string) - строковый тип данных для хранения текста
print(a * 4, c * 4)  # 20 5555
print('hello ' * 4)  # hello hello hello hello

c1 = 'Hello, '
c2 = 'world!'
print(c1 + c2)  # Hello, world! - операция конкатенации (склеивание строк)


d1 = True  # bool (Boolean) - элементы математической логики
d0 = False
print(4 < 10)  # True
'''


# Конвертация типов данных
'''
a = 5
print(a, type(a))  # 5 <class 'int'>

a = str(a)
print(a, type(a))  # 5 <class 'str'>
# ValueError: invalid literal for int() with base 10: '5.0'

a = float(a)
print(a, type(a))  # 5.0 <class 'float'>

a = int(a)
print(a, type(a))  # 5 <class 'int'>
'''

# Ввод данных с клавиатуры
'''
n = int(input('Введите целое число: '))
print(n, type(n))  # 45 <class 'int'>

s = input('Введите строку: ')  # Ввод данных с клавиатуры
print(s, type(s))
'''


# Работа с f-строками
'''
name = input('Введите имя пользователя: ')
weather = 'облачно'
temperature = int(input('Введите температуру: '))

print('Привет, Алена! Сегодня облачно, а температура 25 градусов.')
print('Привет, ', name, '! Сегодня облачно, а температура ', temperature,' градусов.')
print('Привет, ' + name + '! Сегодня облачно, а температура ' + str(temperature) + ' градусов.')
print('Привет, {}! Сегодня облачно, а температура {} градусов.'.format(name, temperature))
print(f'Привет, {name}! Сегодня облачно, а температура {temperature} градусов.')
'''


















