
# region Работа над курсом

'''

Отлично! По ссылке ты найдешь наш Сборник задач по 23 номерам: https://stepik.org/lesson/1228672/step/1?unit=1242205

Переходи в наш Телеграм канал и ищи во вкладке "Разборы" похожие номера!
Разборов там очень много 👉 https://t.me/+0z70ARRnvChlMTky

'''
import turtle
from os.path import split
from traceback import print_tb
from zoneinfo import reset_tzpath

# endregion Работа над курсом

# region Планирование бюджета:
'''
pairs = 8800 * 5 + 4800
groups = 9600 * 4
individual = 14400 * 3 + 12800 + 8000 * 10
print(pairs + groups + individual)
'''
# endregion Планирование бюджета:


# 9. 11617
# 13. 11791
# 14. 11622
# 18. 11626
# 23. 11629
# 24. 11630
# 25. 11718


# todo сделать разбор Тип 14 №63030
'''
def my_int(num: list, base: int):
    return sum([x*base**i for i, x in enumerate(num[::-1])])

for x in range(40):
    for y in range(40):
        A = my_int([5, 7, x, 6, 9, 2, y, 1, 9], 40)
        B = my_int([y, x], 40)
        if A % 39 == 0 and (B**0.5 == int(B ** 0.5)):
            print(x, y, B)
'''


# todo сделать разбор
# № 15413 (Уровень: Средний)
# (А. Вдовин) Найдите количество четырехзначных чисел в девятеричной
# системе счисления, в которых есть ровна одна цифра 8,
# а сумма цифр слева от нее равна сумме цифр справа от нее.
#
# Примечание: если слева или справа от 8 цифр нет,
# то сумма считается равной нулю
'''
s = '012345678'
cnt = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                num = a + b + c + d
                if num[0] != '0':
                    if num.count('8') == 1:
                        i = num.index('8')
                        num = [int(x) for x in num]
                        if sum(num[:i]) == sum(num[i+1:]):
                            cnt += 1
print(cnt)
'''


# todo: Разобрать № 12451 (Уровень: Средний) (у всех узлов)
# Сеть, в которой содержится узел с IP-адресом 246.81.65.A, задана маской сети 255.255.255.224,
# где A - некоторое допустимое для записи IP-адреса число.
# Определите количество значений A, для которых у всех узлов в этой сети
# в двоичной записи количество нулей в третьем байте больше, чем в четвертом.
'''
from ipaddress import *
cnt = 0
for A in range(0, 255+1):
    net = ip_network(f'246.81.65.{A}/255.255.255.224', 0)
    # у всех узлов # for ip in net.hosts() - вернет все узлы сети
    if ip_address(f'246.81.65.{A}') not in (net.network_address, net.broadcast_address):
            if all(f'{ip:b}'[16:24].count('0') > f'{ip:b}'[24:].count('0') for ip in net.hosts()):
                cnt += 1
print(cnt)
'''

# todo Разобрать Тип 13 №68246
'''
from ipaddress import *

ipu = '147.222.199.75'
ipu_m = ipu[0:8] + ipu[4:8] + ipu[0:3]
for mask in range(32, 0, -1):
    try:
        net = ip_network(f'147.222.199.75/{mask}', 0)
        c = 0
        if ip_address(f'{ipu_m}') in net:
            for ip in net:
                ipb = f'{ip:b}'
                if ipb.count('1') == 14:
                    c += 1
        if c > 0:
            print(c)
            break

    except:
        break
'''


'''
x: int = 5
b: float = 5.5

z = True  # bool

M = [1, '2', 3.0, True, [1, 2, 3]]  # список list() - массив
print(M)  # [1, '2', 3.0, True, [1, 2, 3]]

M = [1, 2, 3]  # list - список
L = (1, 2, 3)  # tuple - кортеж
C = {1, 2, 3, 3}  # set - множество
D = {'один': 'one', 'два': 'two'}
print(D['один'])  # one

from random import randint
L = [randint(0, 100) for _ in range(10)]
print(L)

# .split(), ''.join(), all(), any(), product(), permutations()
'''

# ПОКА нашлось (333) ИЛИ нашлось (777)
# ЕСЛИ нашлось (333)
# ТО заменить (333, 7)
# ИНАЧЕ заменить (777, 3)
'''
s = '7' * 85
while '333' in s or '777' in s:
    if '333' in s:
        s = s.replace('333', '7', 1)
    else:
        s = s.replace('777', '3', 1)
print(s)
'''

'''
s = '0' + '1' * 12 + '3' * 17 + '2' * 15
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '103', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '210', 1)
print(s.count('2'))
'''

'''
from ipaddress import *
net = ip_network('32.64.208.224/255.255.128.0', 0)
print(net)  # 32.64.128.0/17
'''

# **********


# todo Сделать разбор на канал Тип 5 №51974
'''
R = []
for n in range(1, 10000):
    s = f'{n:b}'
    for _ in range(3):
        summa = sum([int(x) for x in str(int(s, 2))])
        if summa % 2 != 0:
            s += '1'
        else:
            s += '0'
    r = int(s, 2)
    if r > 1028:
        R.append(r)
print(min(R))
'''

'''
R = []
for n in range(1, 10000):
    s = f'{n:b}'
    for _ in range(3):
        s += str(sum([int(x) for x in str(int(s, 2))]) % 2)
    r = int(s, 2)
    if r > 1028:
        R.append(r)
print(min(R))
'''

'''
Прибор автоматической фиксации нарушений правил дорожного движения делает цветные фотографии размером 1024×768 пикселей, 
используя палитру из 4096 цветов. Снимки сохраняются в памяти камеры, группируются в пакеты по несколько штук,
а затем передаются в центр обработки информации со скоростью передачи данных 1 310 720 бит/с.
Каково максимально возможное количество снимков в одном пакете, если на передачу одного пакета отводится не более 300 секунд?
'''

'''
from math import floor

pixels = 1024 * 768
colors = 4096

# Ищем сколько бит уходит на один пиксель:
i = 12   # 2**11 < colors <= 2 ** 12  ->  i = 12

speed = 1_310_720  # бит/сек
time = 300  # сек

one_picture_bit = pixels * i
all_bit = speed * time
pictures = all_bit / one_picture_bit
print(floor(pictures))  # 41

# Без округления мы получаем 41.6666 фотографий,
# следовательно получится 41 цельная фотография.
'''
'''
def F(x, a1, a2):
    P = 15 <= x <= 40
    Q = 21 <= x <= 63
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


R = []
M = [x / 4 for x in range(10 * 4, 80 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))
'''


'''
Какая строка получится в результате применения приведённой ниже программы к строке, 
состоящей из 81 идущей подряд цифре 1? В ответе запишите полученную строку.

  ПОКА нашлось (11111) ИЛИ нашлось (888)
    ЕСЛИ нашлось (11111)
      ТО заменить (11111, 88)
    ИНАЧЕ заменить (888, 8)
'''


# 1
'''
n = input()
cnt = 0
for i in n:
    if i == ' ':
        cnt += 1
print(cnt)
'''

# 2
'''
n = input()
cnt = 1
for i in range(len(n) - 1):
    x, y = n[i], n[i + 1]
    if x == y:
        cnt += 1
    else:
        cnt = 1
print(cnt)
'''


# 3
'''
n = input()

c = []
for i in n:
    if i not in c:
        c.append(i)
print(len(c))
'''

# 3.2 еще один вариант
'''
n = input()
print(len(set(n)))
'''

# 4
'''
s = input()
copied = [x for x in s if s.count(x) == 3]
print(copied[0])
'''

# 5
'''
print(True + True + False)  # 2

a = input()
b = input()
c = input()
r = ''
s = set(a + b + c)
for x in s:
    if (x in a) + (x in b) + (x in c) == 1:
        r += x
print(r)
'''

# 6
'''
n = input()
print(n[::-1])  # срез с шагом в обратном порядке 
'''


# 7
'''
n = input()
word_list = n.split()
C = []
for word in word_list:
    c = len(word)
    C.append(c)

print(min(C))

# Вариант 2
print(min([len(word) for word in input().split()]))
'''

# 8
'''
n = input()
word_list = n.split()
sorted_words = sorted(word_list, key=len)
print(sorted_words)
'''

# 9
'''
n = input()
word_list = n.split()
copied = [word for word in word_list if word_list.count(word) == 2]
print(copied)
'''

# 10
'''
n = input()
word_list = n.split()
for word in word_list:
    if word != word_list[0] and len(word) == len(set(word)):
        print(word)
'''

# todo Посмотреть задачку 11
'''
n = input()
word_list = n.split()

player = True
for i in range(10**10):
    x, y = word_list[i], word_list[i + 1]
    player = not player
    if x[-1] == y[0]:
        continue
    else:
        print(f'победа {int(player) + 1} игрока')
        break
'''

# 12
'''
import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation.replace('_', ' ')
alphabet = lowercase + uppercase

n = input()
if n[0] in alphabet and all(p not in n for p in punctuation):
    print('Переменная корректна')
else:
    print('Переменная не корректна')
'''

# 13
'''
num = 0
while True:
    ticket = input()
    num += 1
    if len(ticket) % 2 == 0:
        l = len(ticket)
        if sum(map(int, ticket[:l // 2])) == sum(map(int, ticket[l // 2:])):
            print(f'Cчастливый билет найден {ticket}! Его порядковый номер {num}')
            break
'''

'''
from ipaddress import *  # Подключаем библиотеку

for mask in range(32 + 1):  # Перебираем все маски
    for A in range(0, 255 + 1):  # Перебираем допустимое число А
        net1 = ip_network(f'201. {A}. 240.33/{mask}', 0)
        net2 = ip_network(f'201. {A}. 240.107/{mask}', 0)
        if net1 == net2:  # Два узла находятся в одной сети
            for ip in net1:  # Пробегаем IP-адреса сети
                print(net1)  # Адрес сети / кол-во единиц в маске
                print(net1.network_address)  # Адрес сети
                print(mask)  # Кол-во единиц в маске
                print(32 - mask)  # Кол-во нулей в маске
                print(net1.netmask)  # Маска сети в десятичном виде
                print(f' {net1.netmask:b}')  # Маска сети в двоичном виде
                print(net1.num_addresses)  # Кол-во адресов в сети
                print(f' {ip:b}')  # IP-адреса в двоичном

'''


# todo найти ошибку и сделать разбор на канал Тип 8 №46966
# Светлана составляет коды из букв слова РОСОМАХА.
# Код должен состоять из 8 букв, и каждая буква в нём должна
# встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
# Сколько кодов может составить Светлана?
'''
from itertools import *
# M = []
# for pair in permutations('РСМХ', 2):
#     M.append(''.join(pair))
# print(M)
R = []
for p in permutations('РОСОМАХА'):
    slovo = ''.join(p)
    if all(pair not in slovo for pair in ['РС', 'РМ', 'РХ', 'СР', 'СМ', 'СХ', 'МР', 'МС', 'МХ', 'ХР', 'ХС', 'ХМ']):
        if 'АА' not in slovo and 'ОО' not in slovo:
            R.append(slovo)
print(set(R))
print(len(set(R)))
'''
'''
g = ['О', 'А', ]
sog = ['Р', 'С', 'М', 'Х']
n = 0
for b1 in g:
    for b2 in sog:
        for b3 in g:
            for b4 in sog:
                for b5 in g:
                    for b6 in sog:
                        for b7 in g:
                            for b8 in sog:
                                s = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8

                                if s.count('Р') == 1 and s.count('О') == 2 and s.count('С') == 1 and s.count(
                                        'М') == 1 and s.count('А') == 2 and s.count('Х') == 1:
                                    print(s)
                                    n += 1
print(n * 2)
'''

'''
money_week = 2000 * 8 + 1800 * 14 + 2300 * 5
group = 5100 * 4

test1 = ((money_week + group) / 4) * 18
print(test1)  # 328950.0

money_week = 2000 * 8 + 1800 * 14 + 2300 * 10
test2 = (money_week / 4) * 18
print(test2)  # 288900.0
'''


# 16
'''
from string import *


alphabet = printable.replace('()', '')


def valid_parentheses(x):
    for elem in alphabet:
        x = x.replace(elem, '')

    while '()' in x:
        x = x.replace('()', '')
    return x == ''


s = input('Введите строку для проверки: ')
print(valid_parentheses(s))
'''


# 17
# подается текстовая строка с арифметическим выражением, нужно
# посчитать значение арифметического выражения не используя eval()
'''
def evaluate_expression(expr):
    def apply_operator(op, right, left):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left // right  # целочисленное деление

    def precedence(op):
        return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

    expr = expr.replace(' ', '')
    operators, values = [], []
    i = 0

    while i < len(expr):
        char = expr[i]
        if char.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            values.append(num)
            continue
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators[-1] != '(':
                right = values.pop()
                left = values.pop()
                op = operators.pop()
                values.append(apply_operator(op, right, left))
            operators.pop()  # Удаляем '('
        elif char in "+-*/":
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(char)):
                right = values.pop()
                left = values.pop()
                op = operators.pop()
                values.append(apply_operator(op, right, left))
            operators.append(char)
        i += 1

    while operators:
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        values.append(apply_operator(op, right, left))

    return values[0]

# Примеры использования
expressions = [
    "3 + 5 * 2",
    "(10 - 2) * 3 + 5",
    "2 * (3 + 4) / 2",
    "(2 + 3) * (5 - 2)"
]

for expr in expressions:
    print(f"Результат '{expr}': {evaluate_expression(expr)}")
'''



# № 18

'''
Дан текст. По указанному количеству символов в одной строке колонки, получите такую колонку текста с 
выравниванием по ширине, перенося слова в следующеую строку и расставляя равномерно нужное количество пробелов между словами
'''

'''
text = (
    "Это пример текста, который необходимо отформатировать в колонки. "
    "Каждое слово должно быть выровнено по ширине, и переноситься на новую строку, "
    "если не помещается в одну строку."
        )

max_width = 30
length_text = len(text) // max_width

message_text = text.split()
new_message = ''
R = []
for elem in message_text:
    R.append(elem + ' ')
    if len(''.join(R)) > 30:
        del R[-1]
        new_message += ''.join(R) + '\n'
        R = []
new_message += ''.join(R)
print(new_message)

new_message_v2 = ''
for s in new_message.split('\n'):
    if len(s) < 30:
        count_probel = s.count(' ')
        n = ((30 - len(s)) // count_probel) + 1
        s = s.replace(' ', ' ' * n)
        new_message_v2 += s + '\n'
        # print(s, 30 - len(s), count_probel, n)
print(new_message_v2)
'''


# № 20
# Дано натуральное число не превосходящее 900000000.
# Напишите программу, которая выводит на экран это число русскими словами.
'''
def number_to_words(n):
    if n == 0:
        return "ноль"

    units = [
        "", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    ]

    tens = [
        "", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят",
        "семьдесят", "восемьдесят", "девяносто"
    ]

    hundreds = [
        "", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот",
        "семьсот", "восемьсот", "девятьсот"
    ]

    thousands = [
        "", "одна", "две"
    ]

    def convert_hundreds(num):
        result = ""
        if num >= 100:
            result += hundreds[num // 100] + " "
            num %= 100
        if 10 <= num < 20:
            result += units[num] + " "
        else:
            if num >= 20:
                result += tens[num // 10] + " "
            if num % 10 > 0:
                result += units[num % 10] + " "
        return result.strip()

    parts = []

    if n >= 1_000_000:
        millions = n // 1_000_000
        parts.append(convert_hundreds(millions) + " миллионов")
        n %= 1_000_000

    if n >= 1000:
        thousands_part = n // 1000
        if thousands_part == 1:
            parts.append("одна тысяча")
        elif thousands_part == 2:
            parts.append("две тысячи")
        else:
            parts.append(convert_hundreds(thousands_part) + " тысячи")
        n %= 1000

    if n > 0:
        parts.append(convert_hundreds(n))

    return ' '.join(parts).strip()


# Пример использования
number = int(input("Введите натуральное число: "))
print(number_to_words(number))
'''

'''
s = 0
for k in range(5, 19):  # не включая 19
    s += 8
    print(k, s)
    # 5 8
    # 6 16
    # 7 24
    # 8 32
    # 9 40
    # 10 48
    # 11 56
    # 12 64
    # 13 72
    # 14 80
    # 15 88
    # 16 96
    # 17 104
    # 18 112
print(s)  # Ответ: 112
'''

'''
def IsPrime(x):  # 24
    if x <= 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


n = 8
print(IsPrime(n))  # False

print([x for x in range(0, 100) if not IsPrime(x)])
'''


# 1
'''
def F(s):
    glas = [x for x in s.lower() if x in 'ауоиэыяюеё']
    sogl = [x for x in s.lower() if x in 'йцкнгшщзхъфвпрлджчсмтбь']
    print(len(sogl), len(glas))


F(input())
'''

# 2
'''
def fib(n):
    a, b = 1, 1
    R = [a, b]
    for i in range(n-2):
        a, b = b, a + b
        R.append(b)
    return R

n = int(input("Введите значение N: "))
print(*fib(n))
'''

# 4
'''
def make_payment(P):
    if P < 20:
        print('Повторите попытку')
    else:
        print('Успех')


P = int(input())
make_payment(P)
'''

# 5
'''
def sim(P):
    if P in (5, 10):
        return P
    elif P == 25:
        return P + 3
    elif P == 50:
        return P + 8
    elif P == 100:
        return P + 20
    else:
        return 'Нет таких тарифов.'


P = int(input())
print(sim(P))
'''


# 7
'''
def F(A, B, N):
    for j in range(1, N+1):
        if A % j == 0 and B % j == 0:
            print(j, end=' ')

A = int(input()) 
B = int(input())
N = int(input())
F(A, B, N)
'''


# todo Сделать примеры на канал
'''
a = int(input())
h = 0
while a > 0:
    n = a % 10
    print(n)
    a = a // 10


def IsPrime(n):  # 8
    if n <= 1:
        return False
    for j in range(2, n):  # исключил 1 и n
        if n % j == 0:
            return False
    return True
'''

# Срезы строк
'''
print(s[2:4])  # cd -
print(s[:4])  # abcd - все, что слева до 4, не включая 4-ый
print(s[2:])  # cde - все, что справа начиная с 2
print(s[::])  # abcde - от левого края до правого края
print(s[0::2])  # ace - Взяли все четные индексы
print(s[1::2])  # bd - Взяли все нечетные индексы
print(s[::-1])  # edcba - Все в обратном порядке
print(s[:-1])  # abcd - Все, кроме последнего
print(s[1:-1])  # bcd - Все, кроме первого и последнего
'''


# todo  Сделать пост про eval
'''
s = '12321231212321'

s = s.replace('2', '*')  # Заменили сразу все '2' на '*'
print(s)  # 1*3*1*31*1*3*1

s = s.replace('*', '+', 2)  # Заменили первые две "*" на '+'
print(s)  # 1+3+1*31*1*3*1

print(eval('1+3+1*31*1*3*1'))  # 97
n = 3 * 216**4 + 2 * 36**6 - 648
print(n)  # 10883911032

n = eval('3 * 216**4 + 2 * 36**6 - 648')
print(n)  # 10883911032
'''

# todo СДЕЛАТЬ РАЗБОР

# Тип 23 №56523
# У исполнителя есть четыре команды, которым присвоены номера.
# 1. Прибавить 1.
# 2. Прибавить 2.
# 3. Умножить на 2.
# 4. Умножить на 3.
#
# Сколько существует программ, которые преобразуют исходное число 1 в число 11
# и при этом содержат ровно одну команду умножения?
'''
def F(a, b, c):
    if a >= b:
        return a == b and c.count('3') + c.count('4') == 1
    return F(a+1, b, c+'1') + F(a+2, b, c+'2') + F(a*2, b, c+'3') + F(a * 3, b, c+'4')


print(F(1, 11, ''))




Переходи в наш Телеграм канал и ищи во вкладке "Разборы" похожие номера!
Разборов там очень много 👉 https://t.me/+0z70ARRnvChlMTky


'''



# todo Сделать пост  .is_integer()
'''
# Тип 25 №33104
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(289123456, 389123456+1):
    if (x ** 0.5).is_integer():
        div = divisors(x)
        if len(div) == 3:
            print(x)
'''


# s = open('24.txt').readline()

# while any(p in s for p in ('++', '**', '*+', '+*')):
#     for p in ('++', '**', '*+', '+*'):
#         s = s.replace(p, f'{p[0]} {p[1]}')

'''
s = s .replace('++', ' ').replace('**', ' ').replace('+*', ' ').replace('*+', ' ')

M = []
for elem in s.split():
    if len(elem) > 1:
        if elem[0] in '*+':
            elem = elem[1:]
        if elem[-1] in '*+':
            elem = elem[:-1]
        M.append(elem)
print(M)

maxi = 0
for x in M:
    if eval(x):

        if maxi < len(x):

            maxi = len(x)
            #print(len(x), x)
print(maxi)
'''


# todo Нужно ли сделать разбор на задачу? Тип 17 №57424
# Определите количество пар последовательности,
# в которых только один из элементов является двузначным
# числом, а сумма элементов пары кратна максимальному
# двузначному элементу последовательности.
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in D) != (y in D):
        if (x + y) % max(D) == 0:
            R.append(x + y)
print(len(R), max(R))
'''


# todo: Решить номер с урока Дмитрий
# https://stepik.org/lesson/1228672/step/15?unit=1242205
'''
from functools import *

@lru_cache(None)
def F(a, b, c, f):
    if a >= b or a == 23:
        return a == b and '11' not in c and '13' in f
    return F(a + 1, b, c + '1', f+f'.{a}.') + F(a + 2, b, c + '2', f+f'.{a}.') + F(a * 2, b, c + '3', f+f'.{a}.')


print(F(3, 79, '', ''))
'''


# todo: Сделать разбор № 18166 (Уровень: Средний)
# (К. Багдасарян) Значение арифметического выражения,
#  где х – натуральное число в диапазоне от 2 до 2025,
#  записали в системе счисления с основанием 5.
#  Определите максимальное значение x, при котором данная
#  запись содержит наибольшее количество цифр «4».
'''
from string import *
alphabet = digits + ascii_uppercase


def convert(n, b):
    r = ''
    while n > 0:
        r = alphabet[n % b] + r
        n //= b
    return r


maxi = 0
R = []
for x in range(2, 2025+1):
    n = 5**2025 + 5**200 - x
    s = convert(n, 5)


    if maxi <= s.count('4'):
        print(x, s.count('4'))
        maxi = s.count('4')
        R.append(x)
print(max(R))
'''

# todo: сделать пост про my_int
# № 13096 (Уровень: Средний)
# В числе 58x723y49_39 x и y обозначают некоторые цифры из алфавита системы счисления с основанием 39.
# Определите такие значения x и y, при которых приведённое число кратно 38,
# а число yx_39 является полным квадратом натурального числа.
# В ответе запишите значение числа yx_39 в десятичной системе счисления.

'''
def my_int(num: list, base):
    return sum([x*base**i for i, x in enumerate(num[::-1], 0)])


for x in range(39):
    for y in range(39):
        A = my_int([5, 8, x, 7, 2, 3, y, 4, 9], 39)
        if A % 38 == 0:
            R = my_int([y, x], 39)
            # if int(R ** 0.5) == R ** 0.5:
            if (R ** 0.5).is_integer():  # число является полным квадратом
                print(R)  # 1444
'''


# todo: Сделать пост № 17781 (Уровень: Сложный)
# A. Прибавить 1
# B. Прибавить сумму всех делителей
#
# Первая команда увеличивает число на 1, вторая – увеличивает
# число на сумму всех его натуральных делителей (включая 1 и само число).
# Сколько существует программ, для которых при исходном числе
# 2 результатом является число 62?

'''
def sumdiv(n):
    return sum([j for j in range(1, n + 1) if n % j == 0])


def F(a, b):
    if a >= b:
        return a == b
    return F(a + 1, b) + F(a + sumdiv(a), b)


print(F(2, 62))
'''


# todo: Сделать разбор # № 10027 (Уровень: Базовый)
# У исполнителя есть три команды, которым присвоены номера:
# A. Прибавить 2
# B. Прибавить 3
# C. Умножить на 2
# Сколько существует программ, для которых при исходном числе 5
# результатом является число 30, а первая в них команда - A или B?
'''
def F(a, b, c):
    if a >= b:
        return a == b and c[0] in 'AB'
    return F(a+2, b, c+'A') + F(a+3, b, c+'B') + F(a*2, b, c+'C')


print(F(5, 30, ''))
# '''


# todo сделать викторинку:
# Крайний символ среза не учитывается
'''
s = '01234'
print(s[1:4])
print(s[1:8])


M = [0, 1, 2, 3, 4]
print(M[1:4])
print(M[1:8])
'''


# todo сделать разбор № 18191 (Уровень: Средний)
'''
pixels = 1920 * 1080
i = 8
I_p = ((pixels * i) * 60) * 60  # бит

a = 2
b = 24000
c = 6
t = 60
I_v = a * b * c * t  # бит

print(((I_v + I_p) * 50) / 2**13)
'''

'''
s = '19823478129'
s = s.replace('1', '*', 4)

id = '1234.354.234.'
print(id.split('.'))
# ['1234', '354', '234', '']


import random
M = [random.randint(0, 100) for i in range(10)]
print(M)  # [23, 55, 62, 75, 57, 67, 73, 73, 81, 94]

copied = [x for x in M if M.count(x) > 1]
print(copied)  # [73, 73]

chet = [x for x in M if x % 2 == 0]

s = '728234987234'
chet = [x for x in s if int(x) % 2 == 0 or x in '02468']
'''
'''
k = 0
while True:
    k += 1
    if k % 2 == 0:
        continue
    if k == 100_000:
        break
    print(k)
'''

# todo продумать шпаргалку
'''
A = True
B = False

if A and B:
    print('Выполняются оба условия')
if A or B:
    print(' Выполняется хотя бы один')
if (A) != (B):  
    print('Выполняется либо 1, либо 2 (только один)')
'''


# todo Сделать разбор Задание 14 https://education.yandex.ru/ege/task/39991489-2021-4ee7-96a1-f45152dbfcd2
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    s = ''
    while n > 0:
        s += alphabet[n % b]
        n //= b
    return s[::-1]


for x in range(1, 10000):
    n = 9**1942 + 9*6**971 + 214 - x
    s = convert(n, 9)
    if abs(s.count('2') - s.count('8')) == 471:
        print(x)
        break
'''

# todo сделать разбора Задание 13 https://education.yandex.ru/ege/task/08aade2d-7fa5-40ae-ab7e-c85bd6f7e570
'''
from ipaddress import *
net1 = ip_network('192.168.56.192/255.255.255.192', 0)
net2 = ip_network('192.168.56.208/255.255.255.240', 0)
cnt = 0
R = []
for ip in net1:
    R.append(ip)
for ip in net2:
    R.append(ip)

for ip in R:
    if (ip in net1) != (ip in net2):
        cnt += 1
print(cnt)
'''


# todo Разобрать на канале почему в 5 номере не надо делать второй if № 18119 (Уровень: Базовый)
'''
def convert(n, base):
    r = ''
    while n > 0:
        r = str(n % base) + r
        n //= base
    return r


R = []
for N in range(1, 1000):
    s = convert(N, 3)
    if sum([int(x) for x in s]) % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    r = int(s, 3)
    if r > 100:
        R.append(r)
print(min(R))
'''


# todo придумать оптимизацию
'''
import time
start = time.time()

cnt = 0
for x in range(100000000, 1000000000):
    if len(set(str(x))) >= 3:
        cnt += 1
print(cnt)

print(time.time() - start)


from itertools import permutations

R = []
for p in permutations('ХАЧАНАБАДЖАТ'):
    word = ''.join(p)
    if word.count('ААААА') == 0:
        R.append(word)
print(len(set(R)))
'''






# mask:

# 255.255.248.0
#  1   1   1  1   байт

# '11111111.11111111.11111000.00000000'
#     8        8        8        8       бит

# Первый байт: mask[:8]
# Второй байт: mask[8:16]
# Третий байт: mask[16:24]
# Четвертый байт: mask[24:]
# Первые два байта: mask[:16]
# Правые два байта: mask[16:]


# todo Тут складируем разборы задач:
#  1. Cделать разбора № 18258 (Уровень: Сложный)
#  2. Интересный 9 номер https://education.yandex.ru/ege/task/3c10485a-aca0-427e-8464-c7669e3315f9







# todo сделать разбор https://education.yandex.ru/ege/task/1fba1cbc-57aa-4874-b06d-1b434166e30c
'''
M = []
for n in range(1, 10000):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '1' + s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)
    if n >= 33:
        M.append(r)
print(min(M))
'''


# todo розбор 5 номера https://education.yandex.ru/ege/task/71189626-0f31-4380-b790-94a173acd59a
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 7)
    z = ''
    for x in s:
        if x in '13579':
            z += str(int(x) + 1)
        else:
            z += x
    summa = sum([int(x) for x in z])
    # summa = sum(map(int, z))
    z = convert(summa, 7) + z
    if z[0] in '13579':
        z = z[0] + z
    r = int(z, 7)
    if r > 2000:
        M.append(r)
print(min(M))
'''


# Пару вступительных слов по системы счисления
'''
from string import *
alp36 = digits + ascii_uppercase
print(alp36)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alp2 = alp36[:2]  # '01'
alp8 = alp36[:8]  # '01234567'
alp16 = alp36[:16]  # '0123456789ABCDEF'
'''

# Универсальная функция перевода в различные системы счисления
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLXZCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b]+ r
        n //= b
    return r


n = 8

# Перевод в двоичную систему:
print(bin(n)[2:])  # 1000
print(f'{n:b}')  # 1000
print(convert(n, 2))  # 1000

# Перевод из 2-й обратно в 10-ю:
print(int('1000', 2))  # 8


# Перевод в восьмеричную систему:
print(oct(n)[2:])  # 10
print(f'{n:o}')  # 10
print(convert(n, 8))  # 10

# Перевод из 8-й обратно в 10-ю:
print(int('10', 8))  # 8


# Перевод в шестнадцатеричную систему:
print(hex(n)[2:])  # 8
print(f'{n:x}')  # 8
print(convert(n, 16))  # 8

# Перевод из 16-й обратно в 10-ю:
print(int('8', 16))  # 8


# Перевод в троичную систему:
print(convert(n, 3))  # 22
print(int('22', 3))  # 8
'''

# Ограничение до 36 символьного алфавита
'''
print(int('234532', 37))
# ValueError: int() base must be >= 2 and <= 36, or 0
'''

# Варианты маски сети:
# [Единиц: 0, Нулей: 32] 000000....000
# [Единиц: 1, Нулей: 31] 100000....000
# [Единиц: 2, Нулей: 30] 110000....000
# [Единиц: 3, Нулей: 29] 111000....000
# [Единиц: 4, Нулей: 28] 111100....000
# [Единиц: 5, Нулей: 27] 111110....000
# ....
# [Единиц: 31, Нулей: 1] 111111....110
# [Единиц: 32, Нулей: 0] 111111....111

# for mask in range(0, 32+1):
#     print(mask)

# todo Правки по Степик курсам Python
#  1. Добавить примечение из математики https://stepik.org/lesson/1309433/step/10?auth=login&unit=1324549
#  2. Эта задача для строк https://stepik.org/lesson/1309453/step/9?unit=1324569
#  3. Убрать insert https://stepik.org/lesson/1309452/step/6?unit=1324568
#  4. Убрать задачу с ''.join() https://stepik.org/lesson/1309453/step/9?unit=1324569
#  5. Перенести задачу в строки https://stepik.org/lesson/1309453/step/10?unit=1324569
#  2. Убрать слова про абсолютную сумму https://stepik.org/lesson/1038775/step/12?unit=1062778
#  3. Полностью убрать все содержимое ДОМАШЕК по 12 номеру и "форум ответов" почистить, затем заменить не задачами с КОМПЕГЭ  https://stepik.org/lesson/1038682/step/1?unit=1062773
#  4. Полностью убрать все содержимое ПРАКТИК по 12 номеру и "форум ответов" почистить, затем заменить не задачами с КОМПЕГЭ  https://stepik.org/lesson/1038682/step/1?unit=1062773





# todo Правки по Степик курсам ЕГЭ (домашки)
#  1. +
#  2.1 Удалить задачу: (https://stepik.org/lesson/1038536/step/5?unit=1062771 заменить на: 23548
#  2.2 Удалить задачу: (https://stepik.org/lesson/1038536/step/9?unit=1062771) заменить на: 23261
#  2.3 Удалить задачу: (https://stepik.org/lesson/1038536/step/15?unit=1062771) заменить на: 23186
#  3. +
#  4. +
#  5.1 Удалить задачу: (https://stepik.org/lesson/1038432/step/8?unit=1060804) заменить на: № 6885 (done)
#  6. +
#  7. +
#  8.1 Удалить задачу: (https://stepik.org/lesson/1038667/step/15?unit=1062772) заменить на: 23746
#  9.1 Удалить задачу: (https://stepik.org/lesson/1038670/step/5?unit=1062777) заменить на: 23747
#  9.2 Удалить задачу: (https://stepik.org/lesson/1038670/step/10?unit=1062777) заменить на: 23555
#  9.3 Удалить задачу: (https://stepik.org/lesson/1038670/step/10?unit=1062777) заменить на: 23368
#  10. +
#  11.1 Удалить задачу: (https://stepik.org/lesson/1038676/step/3?unit=1062784) заменить на: 23557
#  11.2 Удалить задачу: (https://stepik.org/lesson/1038676/step/9?unit=1062784) заменить на: 23370
#  11.3 Удалить задачу: (https://stepik.org/lesson/1038676/step/13?unit=1062784) заменить на: 23195
#  12. -
#  13.1 Удалить задачу: (https://stepik.org/lesson/1038700/step/7?unit=1062785) заменить на: 23559
#  13.2 Удалить задачу: (https://stepik.org/lesson/1038700/step/12?unit=1062785) заменить на: 23372
#  13.3 Удалить задачу: (https://stepik.org/lesson/1038700/step/2?unit=1062785) заменить на: 23272
#  14. +
#  15. +
#  16.1 Удалить задачу: (https://stepik.org/lesson/1038709/step/4?unit=1062775) заменить на: 23756
#  16.2 Удалить задачу: (https://stepik.org/lesson/1038709/step/12?unit=1062775) заменить на: 20906
#  17.1 Удалить задачу: (https://stepik.org/lesson/1038775/step/10?unit=1062778) заменить на: 23276
#  18. +
#  19-21.1 Удалить задачу: (https://stepik.org/lesson/1038794/step/10?unit=1062789) заменить на: 23759
#  19-21.2 Добавить задачу: 22066
#  19-21.3 Добавить задачу: 23565
#  19-21.4 Добавить задачу: 20825
#  22. +
#  23. +
#  24. +
#  25.1 Удалить задачу: (https://stepik.org/lesson/1038816/step/3?unit=1062780) заменить на: 21909
#  25.2 Удалить задачу: (https://stepik.org/lesson/1038816/step/8?unit=1062780) заменить на: 23282
#  25.3 Удалить задачу: (https://stepik.org/lesson/1038816/step/12?unit=1062780) заменить на: 23382
#  25.4 Удалить задачу: (https://stepik.org/lesson/1038816/step/15?unit=1062780) заменить на: 23569
#  26. +
#  27. +




# todo Рассмотреть 9964 (даниил)
'''
from functools import *

@lru_cache(None)
def f(c, e, step):
    if c >= e:
        print(step)
        return c == e and "CAC" in step
    return f(c + 1, e, step+"A") + f(c * 3, e, step + "B") + f(c + 5, e, step + "C")


print(f(3, 69, ""))
'''




# todo глянуть № 9370 Джобс 10.06.23 (Уровень: Сложный)

'''
# Открыли и считали данные для 17 номера:
M = [int(s) for s in open('0. files/17.txt')]

# Открыли и считали данные для 24 номера:
s = open('0. files/24.txt').readline()

# Открыли и считали данные для 9 номера:

for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]

# Открыли и считали данные для 27 номера:

for s in open('0. files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(i) for i in s.split()]
'''


'''

from functools import *

def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    else:
        return 6 * (G(n - 7) - 36)

@lru_cache()
def G(n):
    if n >= 248045:
        return n / 20 + 28
    else:
        return G(n + 9) - 4

for i in range(248045, 0, -1):
    G(i)

print(F(673))



print((5 + 5 + 5 + 5 + 5 + 0) / 6)
# Алгоритм вычисления функций F(n) и G(n), где n - целое число, задан следующими соотношениями:
# F(n) = F(n−4)+3580, если n ≥ 19;
# F(n) = 6×(G(n−7)−36), если n < 19;
#
# G(n) = n/20+28, если n ≥ 248045;
# G(n) = G(n+9)−4, если n < 248045.
# Чему равно значение функции F(673)?
'''


'''
summa = 23904
print(f'Итог: {summa}')
print(summa * 0.4)
print(summa * 0.3)
print(summa * 0.2)
print(summa * 0.1)
'''





'''
G = [0] * 250000

for n in range(250000-1, 0, -1):
    if n >= 248045:
        G[n] = n / 20 + 28
    if n < 248045:
        G[n] = G[n + 9] - 4

F = [0] * 1000
for n in range(8 , 1000):
    if n >= 19:
        F[n] = F[n - 4] + 3580
    if n < 19:
        F[n] = 6 * (G[n - 7] - 36)

print(F[673])
'''





# todo разбор https://education.yandex.ru/ege/inf/task/4a521e4c-c1ac-440a-8fb2-3aa0bc59172c
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    A = [x for x in M if abs(x) % 10 == 3]
    if len(A) == 3:
        L = [x for x in M if x > 0]
        K = [x for x in M if x < 0]
        if sum(L) ** 2 < sum(K) ** 2:
            cnt += 1
print(cnt)
'''

'''
# [wkiejrf] - только один символ из набора
# [wkiejrf]* - набор любой длины в том числе пустой
# [wkiejrf]+ - набор любой длины, но непустой
# (www) - ищем конкретную последовательность именно этих символом 
# (www)* - ищем последовательности именно этих символом (в том числе пустую)
# (www)+ - ищем последовательности именно этих символом (но непустую)
# | - или 
'''




'''
from itertools import permutations
table = '13 16 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87'
graph = 'HD DH HF FH HB BH BC CB FE EF DA AD EG GE GA AG GC CG AC CA'

print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFGH'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), p[i-1])
    if sorted(new_table.split()) == sorted(graph.split()):
        print(*p)
        # 1 2 3 4 5 6 7 8
        # A E G F B C H D
        # C E G F D A H B
'''

# 32  47
# GE  FH  -> 15 + 13 = 28

    #   1    2    3    4    5    6    7    8
    # ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    # i 0    1    2    3    4    5    6    7

    # 13 15 18 23 24 31 32 36 42 47 56 57 61 63 65 74 75 78 81 87
    # A3 A5 A8 23 24 3A 32 36 42 47 56 57 6A 63 65 74 75 78 8A 87
    # A3 A5 A8 B3 B4 3A 3B 36 4B 47 56 57 6A 63 65 74 75 78 8A 87
    # AC A5 A8 BC B4 CA CB C6 4B 47 56 57 6A 6C 65 74 75 78 8A 87
    # AC A5 A8 BC BD CA CB C6 DB D7 56 57 6A 6C 65 7D 75 78 8A 87
    # AC AE A8 BC BD CA CB C6 DB D7 E6 E7 6A 6C 6E 7D 7E 78 8A 87
    # AC AE A8 BC BD CA CB CF DB D7 EF E7 FA FC FE 7D 7E 78 8A 87
    # AC AE A8 BC BD CA CB CF DB DG EF EG FA FC FE GD GE G8 8A 8G
    # AC AE AH BC BD CA CB CF DB DG EF EG FA FC FE GD GE GH HA HG


'''
i = 7
print(f'Максимально мощность алфавита: {2 ** 7}')  # 128
alp = 128  # i = 7

alp = 100  # i = 7

print(f'Минимальная мощность алфавита: {2 ** 6 + 1}')  # 65
alp = 65  # i = 7
alp = 64  # i = 6
'''


'''
def F(x, y, A):
    return (78_125 != y + 4*x) or (A > x) and (A > y)

for A in range(1, 10**10):
    if all(F(x, 78_125 - 4*x, A) for x in range(1, 78_125 // 4)):
        print(A)
        break


def F(x, y, A):
    return (y < A) and (x < A) or (89_241 < 5 * y + x)

for A in range(0, 100000):
    if all(F(89_241 - 5*y, y, A) for y in range(0, 10000)):
        print(A)
        break
'''




# 📖 Пробник (Вариант 2)
# Студент #Анна сдал ответы на пробник, вот результаты:
#
# Пробник №2
# Дата: #Суббота #28Февраля2026
# ✅ Верно: 1, 2, 4, 7, 8, 11, 12, 14, 15, 16, 17, 18, 23, 25
# ⛔️ Неверно: 3, 5, 6, 10, 19, 20, 21, 27
# ❔ Без ответа: 9, 13, 22, 24, 26
#
# Итог: 14/29 первичных балла ~ 59 вторичных

# 1. 25
# 2. xzyw
# 3. 2000
# 4. 7
# 5. 17
# 6. 4
# 7. 512
# 8. 117601
# 9.
# 10. 9
# 11. 256
# 12. 999
# 13.
# 14. 1405686
# 15. 25
# 16. 4045
# 17. 2089 99343
# 18. 2292 524
# 19. 30
# 20. 8 9
# 21. 2
# 23. 200
# 24.
# 25. 2381071 1177
# 21801871 10777
# 22611071 11177
# 24431771 12077
# 27061671 13377
# 29691571 14677
# 26.
# 27. -95076 -52743
# -27190 -47251



'''
s = open('files/24.txt').readline()
cnt = 3
maxi = 0

for i in range(0, len(s)-3, 2):
    x, y, z, w = s[i:i+4]
    if int(x + y) < int(z + w):
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 3

for i in range(1, len(s)-3, 2):
    x, y, z, w = s[i:i+4]
    if int(x + y) < int(z + w):
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 3
print(maxi)
'''



# todo глянуть Задание 27
'''
from math import dist
clustersA = [[], []]
clustersB = [[], [], []]

for s in open('files/27A.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if 5 < y < 15:
        clustersA[0].append([x, y])
    if 15 < y < 25:
        clustersA[1].append([x, y])

for s in open('files/27B.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if 25 < x < 35 and 13 < y < 18:
        clustersB[0].append([x, y])
    if 18 < x < 23 and 14 < y < 20:
        clustersB[1].append([x, y])
    if 15 < x < 21 and 25 < y < 31:
        clustersB[2].append([x, y])


def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
            R.append([summa, p])
    return min(R)[1]

centersA = [center(cl) for cl in clustersA]
print(centersA) # [[6.412136, 10.106562], [8.82346, 21.840848]]
print(len(clustersA[0])) # 301
print(len(clustersA[1])) # 344 - максимальное количество точек

# print(dist([1.0, 1.5], [6.412136, 10.106562]))
A2 = dist([1.0, 1.5], centersA[0]) + dist([1.0, 1.5], centersA[1])
print(int(A2 * 10000))


centersB = [center(cl) for cl in clustersB]
print(centersB) # [[28.939202, 14.512709], [20.757817, 15.787054], [18.749613, 28.956072]]
print(len(clustersB[0])) # 148
print(len(clustersB[1])) # 200
print(len(clustersB[2])) # 902


def B1(cl, center, lenght):
    cnt = 0
    for p in cl:
        if p == center:
            continue
        if dist(center, p) <= lenght:
            cnt += 1
    return cnt

print(B1(clustersB[1], centersB[1], 1.2) )  # Ответ: 38


def B2(cl, center):
    R = []
    for p in cl:
        if p == center:
            continue
        R.append(dist(p, center))
    return min(R)

print(int(B2(clustersB[2], centersB[2]) * 10000))  # Ответ: 1116
'''

# Для файла A определите координаты центра каждого кластера, затем
# найдите два числа: A1 — максимальное количество точек в кластере и A2 —
# сумму расстояний от центров кластеров до точки с координатами (1,0; 1,5).

# 344	294354
# 152	528


# № 25354 ЕГКР 13.12.25 (Уровень: Средний)
# Для какого наименьшего целого неотрицательного числа А логическое выражение
# (78125 !=y+4x)∨(A>x)∧(A>y)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (78125 != y + 4*x) or (A > x) and (A > y)

for A in range(0, 100000):
    if all(F(x, 78125 - 4 * x, A) for x in range(1, 78125 // 4)):
        print(A)
        break
'''
# Ответ: 78122


# № 15 ЕГКР 13.12.25 (Вариант 3)
# Для какого наименьшего целого неотрицательного числа А логическое выражение
# (x * y < A) or (x < 7 * y) or (343 < x)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (x * y < A) or (x < 7 * y) or (343 < x)

for A in range(0, 100000):
    if all(F(7*y, y, A) for y in range(1, 10000)):
        print(A)
        break
'''
# Ответ: 16808


# № 15 Статград 27.01.26 вариант 1 (https://disk.yandex.ru/i/vixdXzmtK3ZqhA)
# Для какого наименьшего целого неотрицательного числа А логическое выражение
# (y < A) and (x < A) or (89241 < 5*y + x)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (y < A) and (x < A) or (89241 < 5*y + x)

for A in range(0, 100000):
    if all(F(89241 - 5*y, y, A) for y in range(1, 89241 // 5)):
        print(A)
        break
'''
# Ответ: 89237


# № 15 Статград 27.01.26 вариант 2 (https://disk.yandex.ru/i/p1_jpoG32GlsYg)
# Для какого наименьшего целого неотрицательного числа А логическое выражение
# (y < A) and (x < A) or (93147 < 6*y + x)
# истинно (т.е. принимает значение 1) при любых целых положительных х и у?
'''
def F(x, y, A):
    return (y < A) and (x < A) or (93147 < 6*y + x)

for A in range(0, 100000):
    if all(F(93147 - 6*y, y, A) for y in range(1, 93147 // 6)):
        print(A)
        break
'''
# Ответ: 93142


# № 27137 (Уровень: Сложный)
# (В. Лашин) Для какого наименьшего целого неотрицательного числа А логическое выражение
# (1241651 !=5∗x+y)∧(413184 != x+2 * y)∨(A>x)∨(A>y)
# истинно (т.е. принимает значение 1) при любых целых положительных х, у?
'''
def F(x, y, A):
    return (1241651 != 5*x+y) and (413184 != x+2 * y) or (A>x) or (A>y)

for A in range(0, 100000):
    if all(F(7*y, y, A) for y in range(1, 10000)):
        print(A)
        break
'''

'''
Обратите внимание, что сервис должен подстроиться под ваш локальный часовой пояс ☝️
После записи сервис предложит перейти и запустить Телеграм и написать мне, сделайте это 🙏

Не забывайте заглядывать в мой ТГК: Информатика ЕГЭ | itpy 🧑‍💻
Там всё, что нужно для подготовки: новости, разборы, видео, шпаргалки и теория 📚

Материалы, которые помогут вам подготовиться к ЕГЭ:
📌 Бесплатный Python-курс с нуля
📌 Шпаргалка по всем заданиям ЕГЭ
📌 Сборник задач для практики
📌 Официальные варианты ЕГЭ 2026


👾 Ссылка на видеовстречи в zoom (https://clc.li/ilandroxxy-zoom)

s/venv/bin/python3 /Users/ilandroxxy/PycharmProjects/lessons/2. Workspace.py 
Traceback (most recent call last):
  File "/Users/ilandroxxy/PycharmProjects/lessons/2. Workspace.py", line 1912, in <module>
    print((f[257487] / 683 + f[257477] / 67) / f[257472])
           ~~~~~~~~~~^~~~~
OverflowError: integer division result too large for a float


С условиями и правилами проведения уроков ознакомился(лась) и согласен(на): https://clc.li/ilandroxxy-rules

'''



# ⛔️ Неверно: 6, 11, 12, 14, 18, 21
'''
1. 17
2. wxyz
3. 1164
4. 16
5. 11
6. 165   801
7. 10
8. 
9.
10. 10
11. 14  12
12. 111  583
13. 2
14. 729927743  729929407
15. 17
16. 8102
17. 720 87094
18. 2569 1101  2407 1101
19. 45
20. 4044
21. 394345  3943
22. 18
23. 200
24.
25.54648 9
     5064048 834
     5974848 984
     50604048 8334
     51514848 8484
     53184648 8759
     54854448 9034
     56524248 9309
     58194048 9584
     59104848 9734
26.
27.
'''








# ЕГЭ: 1, 2, 4, 13, 11, 7, 14, 15, 6, 5, 8
#      1, 2, 3, 10, 8,  6, 11, 12, 5, 4, 7

'''
sym = 64
alp = 26 * 2  # alp = 2 ** i
i = 6  # 2**6 >= alp
# i - это кол-во бит на один символ

bit = sym * i  # кол-во бит на один пароль
print(bit / 8)
byte = 48  # кол-во байт на один пароль (всегда округялется вверх)

byte = byte + 64
print((byte * 768) / 2**10)
'''
'''
# sym - ?
alp = 10 + 52 + 964  # 1026
i = 11

byte = 1.5 * 2**20 / 3000
print(byte)  # 524.288
bit = 524 * 8

# bit = sym * i
sym = bit / i
print(sym)  # 381.09090
'''

'''
pixels = 3614 * 4972
colors = 2**16
i = 16
I = pixels * i  # вес одной фотки в бит

pack = 8 * 2**33 / I
print(pack)  # 239

print(4096 / 239)  # 17.1380 -> 18
print(4096 - 239 * 17)  # 33
'''







'''
# i  0123456
s = '2893712'
print(s[4])  # '7'

print(s[::2])  #'2972'
'''


'''
from itertools import permutations
print('1 2 3 4 5 6 7 8')  # тут 
graph = 'АБ БА АГ ГА АВ ВА ВЕ ЕВ ЕГ ГЕ ЕЖ ЖЕ ЖИ ИЖ ЖД ДЖ ДИ ИД ДГ ГД ГБ БГ'   # тут 
table = '14 17 23 24 25 32 37 41 42 46 47 52 56 58 64 65 68 71 73 74 85 86'   # тут 
for p in permutations('АБВГДЕЖИ'):   # тут 
    new_table = table
    for i in range(1, 8+1):   # тут 
        new_table = new_table.replace(str(i), p[i-1])
    if sorted(new_table.split()) == sorted(graph.split()):
        print(*p)
'''



'''
ip = '123.123.43.32'
print(ip.split('.'))  # ['123', '123', '43', '32']
'''


'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
                if F == 1:
                    print(x, y, z, w)

'''

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0])  # - первый элемент
print(M[-1]) # - последний элемент


from ipaddress import *
net = ip_network('79.128.86.0/255.255.224.0', 0)
cnt = 0
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('1') % 7 != 0:
        # if ip2[-3] == '1' and ip[-2] == '0'  and ip[-1] == '0':
        if ip2[-3:] == '100':
            cnt += 1
print(cnt)
'''




'''
print(f'{192:b}.{168:b}.{112:b}.{140:b}')
print(f'{255:b}.{255:b}.{255:b}.{224:b}')

# 1 and 1 == 1, иначе 0

# 11000000.10101000.01110000.10001100
# 11111111.11111111.11111111.11100000
# 11000000.10101000.01110000.10000000

# 12

print(f'{140:b}')
print(f'{255-224:b}')  # 255 - 224 это обратная маска

# 10001100
# 00011111
# 00001100

print(int('1100', 2))  # 12
'''








# Два оснонвых прототипа 13 номеров

# Сеть задана IP-адресом 172.16.160.0 и маской сети 255.255.240.0.
# Сколько в этой сети IP-адресов,
# для которых количество единиц в их двоичной записи кратно 2?
'''
from ipaddress import *  # Подключение всего содержимого библиотеки
net = ip_network('172.16.160.0/255.255.240.0', 0)  # Находим адрес сети
cnt = 0
for ip in net:  # Перебираем айпи адреса сети
    ip2 = f'{ip:b}'  # Перевод в двоичную систему счисления
    if ip2.count('1') % 2 == 0:  # Находим кол-во единиц в двоичной записи и проверяем кратно ли оно двум
        cnt += 1
print(cnt)
'''
# Сеть, в которой содержится узел с IP-адресом 203.111.195.0,
# задана маской сети 255.255.240.0. Сколько в этой сети IP-адресов,
# в двоичной записи которых количество нулей кратно трём,
# а также содержатся три подряд идущие единицы
# и три подряд идущих нуля одновременно?
'''
from ipaddress import *  # Подключение всего содержимого библиотеки
net = ip_network('203.111.195.0/255.255.240.0', 0)  # Находим адрес сети
cnt = 0
for ip in net:  # Перебираем айпи адреса сети
    ip2 = f'{ip:b}'  # Перевод в двоичную систему счисления
    if ip2.count('0') % 3 == 0:  # Находим кол-во единиц в двоичной записи и проверяем кратно ли оно двум
        if '000' in ip2 and '111' in ip2:
            cnt += 1
print(cnt)
'''

# Адрес сети и широковещательный адрес не могут быть использованы для адресации сетевых устройств.
# Сеть задана IP-адресом одного из входящих в неё узлов 146.180.173.153
# и сетевой маской 255.192.0.0. Найдите наибольший в данной сети
# IP-адрес, который может быть назначен компьютеру. В ответе укажите
# найденный IP-адрес без разделителей.
'''
from ipaddress import *  # Подключение всего содержимого библиотеки
net = ip_network('146.180.173.153/255.192.0.0', 0)  # Находим адрес сети
for ip in net:
    print(ip)
    # 146.191.255.254 -> 146191255254
    # 146.191.255.254 -> 146 + 191 + 255 + 254
    # 146.191.255.254 -> 146 + 191
'''





# ¬x       |   (not x)
# ¬(w≡z)   |   (not(w == z))
# x ∧ y    |    x and y
# x ∨ x    |    x or y
# x → w    |    x <= w
# w ≡ z    |    w == z

# № 29334 Открытый вариант 2026 (Уровень: Базовый)
'''
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= x) <= (x == y)) or (not w)
                if F == 0:
                    print(x, y, z, w)
'''

'''
from math import prod
for n in range(4, 10000):
    s = '2' + '7' * n
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
        if '377' in s:
            s = s.replace('377', '72', 1)
    M = prod([int(x) for x in s])
    if M % 3 == 0 and M % 10 == 1:
        print(n)

for n in range(4, 10000):
    s = '5' + n * '7'
    while '577' in s or '677' in s or '657' in s:
        if '577' in s:
            s = s.replace('577', '76', 1)
        if '677' in s:
            s = s.replace('677', '75', 1)
        if '657' in s:
            s = s.replace('657', '56', 1)
    summ = sum([int(i) for i in s])
    if summ == 76:
        print(n)
'''
# Ответ: 19


# https://education.yandex.ru/ege/inf/task/b931a5bf-94b1-4fb8-86ec-e452222a1723

# При регистрации в компьютерной системе каждому объекту присваивается идентификатор,
# состоящий из 11 символов и содержащий только символы из 9540-символьного специального
# алфавита. В базе данных для хранения каждого идентификатора отведено одинаковое и
# минимально возможное целое число байт. Все символы идентификаторов кодируются одинаковым
# и минимально возможным количеством бит.





# 6, 12, 19-21, 18, 24, 25

'''
from functools import lru_cache

TARGET = 73


@lru_cache(None)
def game(s):
    if s >= TARGET: return 0
    moves = [s + 1, s * 2]

    win_moves = [game(next_s) for next_s in moves if game(next_s) % 2 != 0]
    if win_moves: return min(win_moves) + 1
    return max([game(next_s) for next_s in moves]) + 1


print("Ответ 19:", [s for s in range(1, 73) if game(s) == 2])
'''



# № 29353 Открытый вариант 2026 (Уровень: Базовый)
# A. Прибавить 1
# B. Умножить на 2
# C. Умножить на 3
# Сколько существует программ, для которых при исходном числе 2 результатом
# является 39 и при этом траектория вычислений не содержит числа 14?
'''
def F(a, b):
    if a >= b or a == 14:
        return a == b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)

print(F(2, 39))


def F(a, b):
    if a > b or a == 14:
        return 0
    elif a == b:
        return 1
    else:
        h = [F(a+1, b), F(a*2, b), F(a*3, b)]
        return sum(h)

print(F(2, 39))
'''

# № 28940 ЕГКР 18.04.26 (Уровень: Базовый)
# 1 куча: +1, +5, *3 | s >= 124 | 1 <= s <= 123

# s - это кол-во камней в куче, которое мы ищем

# n - это шаг нашей игры
# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
def F(s, n):
    if s >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 5, n - 1), F(s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 123+1) if F(s, n=2)])
print(20, [s for s in range(1, 123+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 123+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 25358 ЕГКР 13.12.25 (Уровень: Базовый)
# 1 куча: +2, +4, *2 | s >= 125 | 1 <= x <= 124
'''
def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 124+1) if F(s, n=2)])
print(20, [s for s in range(1, 124+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 124+1) if F(s, n=4) and not F(s, n=2)])
'''

# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 меньшего | s <= 30 | s >= 31
'''
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(31, 1000) if F(s, n=2)])
print(20, [s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
'''


# T = ((2,2), (5,9), (7,-12), (5,5), (2,12), (-10,-13), (-11,11), (1,4), (2, 6))  # tuple (кортеж)

'''
L = [(2,2), (5,9), (7,-12), (5,5), (2,12), (-10,-13), (-11,11), (1,4), (2, 6)]  # list (список)

cnt = 0
for p in L:
    s, k = p
    # s = int(input())
    # k = int(input())
    if s < 5 or k < 5:
        print("ДА")
        cnt += 1
    else:
        print("НЕТ")
print(cnt)
'''

'''
L = [(13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13)]

for A in range(-20, 20):
    cnt = 0
    for p in L:
        s, t = p
        if (s > A) or t > 12:
            # print("YES")
            cnt += 1
        else:
            # print("NO")
            pass
    if cnt == 4:
        print(A)
        break
'''




# Напишите программу, которая в последовательности целых чисел определяет
# количество нечетных чисел, кратных 3. Программа получает на вход целые
# числа, количество введенных чисел неизвестно, последовательность чисел
# заканчивается числом 0 (0—признак окончания ввода, не входит в последовательность).
# Количество чисел не превышает 1000. Введенные числа по модулю не превышают 30 000.
# Программа должна вывести два числа: длину последовательности (завершающий 0 не учитывается)
# и количество нечетных чисел, кратных 3.
'''
print(123 % 10)  # 3
print(123 % 100)  # 23

print(-123 % 10)  # 7
print(-123 % 100)  # 7

n = 7
print(n % 4 == 3)  # True
print(-n % 4 == 3)  # False

A = int(input())
cnt = 0
k = 0
while A != 0:
    k += 1
    if abs(A) % 3 == 0 and abs(A) % 2 != 0:
        cnt += 1
    A = int(input())

print(k, cnt)
'''

'''
name = input('Введите имя: ')
print(f'Привет, {name}')
'''

'''
s = '3324234'
print(s[0])  # 3
print(s[-1])  # 4
print(s[2:5])  # 242


n = 8
print(bin(n)[2:])  # 1000 - двоичная система
print(oct(n)[2:])  # 10 - восмеричная система
print(hex(n)[2:])  # 8 - шестнадцатеричная система

print(f'{n:b}')  # 1000 - двоичная система
print(f'{n:o}')  # 10 - восмеричная система
print(f'{n:x}')  # 8 - шестнадцатеричная система


# Встроенная функция для перевода в 10-ную систему
print(int('1000', 2))  # 8
print(int('10', 8))  # 8
print(int('8', 16))  # 8
print(int('1000', 3))  # 8
print(int('1000', 5))  # 8
# ValueError: int() base must be >= 2 and <= 36, or 0
'''

'''
n = 10**8
print(hex(n)[2:].upper())  # 5F5E100
print(f'{n:X}')  # 5F5E100
print(f'{n:x}')  # 5f5e100


A = int(input())
cnt = 0
while A != 0:
    A16 = f'{A:X}'
    if len(A16) == 3:
        if A16[-1] == 'C':
            cnt += 1
    A = int(input())
print(cnt)
'''

'''
summa = 0
n = int(input())
for _ in range(n):
    x = int(input())
    if x % 7 == 1:
        summa += x
print(summa)
'''
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 10**8
print(hex(n)[2:].upper())  # 5F5E100
print(f'{n:X}')  # 5F5E100
print(f'{n:x}')  # 5f5e100
print(convert(n, 16))  # 5F5E100

summa = 0
n = int(input())
for _ in range(n):
    x = int(input())
    x7 = convert(x, 7)
    if x7[-1] == '1':
        summa += x
print(summa)
'''

# Екатеренбург
# Бердск
# Томск
# Омск
# Барнаул
# Иркутск
# Карсноярск



# 23, 22, 19-21, 18, 16, 15, 14, 13, 12, 11, 10, 7, 6, 4, 3, 2, 1


# № 29974 Апробация 14.05.26 (Уровень: Базовый)
# 1 куча: -3, -7, /4 до меньшего | s <= 15 | s > 15

# s - это кол-во камней в куче, то есть то, что мы ищем
# n - это шаг нашей игры

# n = 1: Петя первый ход
# n = 2: Ваня первый ход
# n = 3: Петя второй ход
# n = 4: Ваня второй ход
'''
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 7, n - 1), F(floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(16, 1000) if F(s, n=2)])
print(20, [s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])
'''
# 1 куча: -3, -7, /4 до меньшего | s <= 15 | s > 15


# № 28940 ЕГКР 18.04.26 (Уровень: Базовый)
# 1 куча: +1, +5, *3 | s >= 124 | 1 <= s <= 123
'''
def F(s, n):
    if s >= 124:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 5, n - 1), F(s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 123+1) if F(s, n=2)])
print(20, [s for s in range(1, 123+1) if F(s, n=3) and not F(s, n=1)])
print(21, [s for s in range(1, 123+1) if F(s, n=4) and not F(s, n=2)])
'''


# № 29351 Открытый вариант 2026 (Уровень: Базовый)
# 2 кучи: a+4, s+4, a*3, s*3 | a + s >= 154 | a = 11 | 1 <= s <= 142
'''
def F(a, s, n):
    if a + s >= 154:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+4, s, n - 1), F(a, s+4, n - 1), F(a*3, s, n - 1), F(a, s*3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print(19, [s for s in range(1, 142+1) if F(11, s, n=2)])
print(20, [s for s in range(1, 142+1) if F(11, s, n=3) and not F(11, s, n=1)])
print(21, [s for s in range(1, 142+1) if F(11, s, n=4) and not F(11, s, n=2)])
'''



# № 9778 Основная волна 20.06.23 (Уровень: Средний)
'''
n = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    n += 1
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied2) == 2 and len(copied1) == 4:
        if copied2[0] >= sum(copied1) / len(copied1):
            print(n)
            break
'''






# x - ?
'''
alp = 510 + 10
i = 10

# bit = x * i


byte = 9379 * 2**20 / 18_982_657
print(byte)  # 518.08312 -> 519

bit = 519 * 8

x = bit / i
print(x)  # 415.2
'''


'''
i = 9
print(2 ** 9)  # - максимальная мощность при i = 9

print(2 ** 8 + 1)  # - минимальная мощность при i = 9


alp = 256  # i = 8  # - максимальная мощность при i = 8

alp = 200  # i = 8

alp = 129 # i = 8  # - минимальная мощность при i = 8
alp = 128  # i = 7
'''

'''
def F(x, a1, a2):
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))

R = []
M = [x / 10 for x in range(5 * 10, 120 * 10)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''

'''
def F(x, a1, a2):
    D = 290 <= x <= 575
    C = 130 <= x <= 480
    B = 32 <= x <= 425
    A = a1 <= x <= a2
    return (C <= ((not D))) and A and ((not B))

R = []
M = [x / 4 for x in range(30 * 4, 600 * 4)]
for a1 in M:
    for a2 in M:
        if all(not F(x, a1, a2) for x in M):
            R.append(a2 - a1)
print(min(R))  # 21.75 -> 21.8 -> 21.9 -> 22
'''


'''
from math import ceil, floor
def F(s, k):
    if s <= 15:
        return k % 2 == 0
    if k == 0:
        return 0
    q = [F(s - 3, k-1), F(s - 7, k-1), F(floor(s / 4), k-1)]
    return any(q) if (k-1) % 2 == 0 else all(q)


print([s for s in range(16, 1000) if F(s, 2)])
print([s for s in range(16, 1000) if F(s, 3) and not F(s, 1)])
print([s for s in range(16, 1000) if F(s, 4) and not F(s, 2)])
'''



# № 31227 Резерв 22.06.26 (Уровень: Базовый)
# 2 кучи: a-3, s-3, a/3, s/3 | a + s <= 53 | a = 19 | s >= 35
'''
from math import ceil, floor
def F(a, s, k):
    if a + s <= 53:
        return k % 2 == 0
    if k == 0:
        return 0
    q = [F(a-3, s, k-1), F(a, s-3, k-1), F(a // 3, s, k-1), F(a, s // 3, k-1)]
    return any(q) if (k-1) % 2 == 0 else all(q)
    return any(q) if (k-1) % 2 == 0 else any(q)

print([s for s in range(35, 1000) if F(19, s, 2)])
print([s for s in range(35, 1000) if F(19, s, 3) and not F(19, s, 1)])
print([s for s in range(35, 1000) if F(19, s, 4) and not F(19, s, 2)])
'''

# Вариант номер 1: ака 17 номер
'''
s = open('files/24.txt').readline()
cnt = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] not in 'AE' and s[i+1] not in 'AE':
        cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 1
print(maxi)

# Вариант номер 2: через замены .replace() и .split() разбиение

s = open('files/24.txt').readline()
s = s.replace('A', ' ').replace('E', ' ')
print(max([len(x) for x in s.split()]))


# Вариант номер 3:

from re import *
s = open('files/24.txt').readline()
pat = '[0-9BCDF]+'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''


# № 17563 Основная волна 08.06.24 (Уровень: Сложный)
'''
from re import *
s = open('files/24.txt').readline()
pat = '[789][0789]*([-*]([789][0789]*|[0]))*'
M = [x.group(0) for x in finditer(pat, s)]
print(M)
print(max([len(x) for x in M]))
'''

# '709*9*8-8'
# '709*9*0-8'





def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))

print(divisors(24))

# 9 = 3 * 3
cnt = 0
from itertools import product
for x in range(800_000+1, 10**10):
    d = [j for j in divisors(x) if len(divisors(j)) == 0]
    if len(d) > 0:
        #        3  *   3  == 9
        if any(p[0] * p[1] == x for p in product(d, repeat=2)):
            M = min(d) + max(d)
            if M % 10 == 4:
                print(x, M)
                cnt += 1
                if cnt == 5:
                    break

# for p in product('123', repeat=5):
#     print(p)

# for p in permutations('123', r=3):
#     print(p)