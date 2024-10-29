
# n = int(input())  # Ввод данных числа с клавиатуры
# print(f'Результат перевода: {r}') - Позволяет подставить значение переменной в строку


'''
from string import *  # Импортируем все содержимое библиотеки string
# Сочетание клавиш ctrl + B - показывает содержимое библиотеки
# alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
alphabet = digits + ascii_uppercase
print(alphabet[:2])  # 01 - Двоичный алфавит
print(alphabet[:8])  # 01234567 - Восьмеричный алфавит
print(alphabet[:16])  # 0123456789ABCDEF - hex алфавит

n = int(input('Введите число для перевода: '))  # 123456789
b = int(input('Введите b-ю систему счисления: '))  # 16
r = ''  # str
while n > 0:
    r += alphabet[n % b]  # (n % b) - int
    n //= b
r = r[::-1]  # Строка в обратном порядке
print(f'Результат перевода: {r}')  # 75BCD15
'''

# Универсальная функция перевода из 10-й в b-ю систему, где 2 <= b <= 36
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n: int, b: int) -> str:  # n - number, b - base
    r = ''
    while n > 0:
        r += alphabet[n % b]  # (n % b) - int
        n //= b
    r = r[::-1]  # Строка в обратном порядке
    return r


print(convert(123456789, 16))  # 75BCD15
'''

# А как делать перевод из b-й в 10-ю систему?
'''
print(int('1000', 2))  # 8
print(int('75BCD15', 16))  # 123456789
'''


# Бесконечные циклы и операторы break, continue, exit()
'''
k = 0
while True:
    k += 1
    if k % 2 != 0:
        continue  # Прерывает итерацию (шаг) цикла
    if k == 1_000_000:
        break  # Прерывает выполнение цикла в котором сейчас лежит
    if k == 2_000_000:
        exit()  # Прерывает выполнение всей программы
    print(k)

print('Продолжение программы')
'''

# Калькулятор перевода в различные системы счисления
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n: int, b: int) -> str:  # n - number, b - base
    r = ''
    while n > 0:
        r += alphabet[n % b]  # (n % b) - int
        n //= b
    r = r[::-1]  # Строка в обратном порядке
    return r


while True:
    case = input('\n'
                 'case 1: Перевод из 10-й в b-ю систему \n'
                 'case 2: Перевод из b-й в 10-ю систему \n'
                 'case 3: Перевод из b-й в k-ю систему \n'
                 'case 0: Выход из программы. \n'
                 'case: '
                 )

    if case == '1':
        n = int(input('Введите число в 10-й системе для перевода: '))
        b = int(input('Введите систему b-ю счисления: '))
        r = convert(n, b)
        print(f'Результат перевода числа {n} в систему {b}-ю: {r}')

    elif case == '2':
        b = int(input('Введите систему b-ю счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        print(f'Результат перевода числа {r} из {b}-й системы: {n}')

    elif case == '3':
        b = int(input('Введите систему b-ю счисления: '))
        k = int(input('Введите систему k-ю счисления: '))
        r = input(f'Введите число в {b}-й системе: ')
        n = int(r, b)
        new_r = convert(n, k)
        print(f'Результат перевода числа {r} из {b}-й системы в {k}-ю: {new_r}')

    elif case == '0':
        print('Спасибо, что вы пользовались нашим калькулятором!')
        exit()

    else:
        print('Я понимаю только команды: 1, 2, 3, 0.')
'''


'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n: int, b: int) -> str:  # n - number, b - base
    r = ''
    while n > 0:
        r += alphabet[n % b]  # (n % b) - int
        n //= b
    r = r[::-1]  # Строка в обратном порядке
    return r


n = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 -4*3**3024 - 2029
r = convert(n, 27)
print(r.count('0'))  # 1343
M = [x for x in r if x > '9']
print(len(M))  # 3368
'''

# Встроенные функции перевода 2, 8, 16
'''
n = 54
print(bin(n)[2:])  # 110110
print(f'{n:b}')  # 110110
print(int('36', 16))  # 54

n = 61
print(oct(n)[2:])  # 75
print(f'{n:o}')  # 75
print(int('75', 8))  # 61

n = 52
print(hex(n)[2:])  # 34
print(f'{n:x}')  # 34 - буквы малые
print(f'{n:X}')  # 34 - буквы большие
print(int('110100', 2))  # 52
'''