
# region Работа над курсом

'''

Отлично! По ссылке ты найдешь наш Сборник задач по 23 номерам: https://stepik.org/lesson/1228672/step/1?unit=1242205

Переходи в наш Телеграм канал и ищи во вкладке "Разборы" похожие номера!
Разборов там очень много 👉 https://t.me/+0z70ARRnvChlMTky

'''
import reprlib
import xml.sax

# endregion Работа над курсом

# region Планирование бюджета:
'''
pairs = 8800 * 5 + 4800
groups = 9600 * 4
individual = 14400 * 3 + 12800 + 8000 * 10
print(pairs + groups + individual)
'''
# endregion Планирование бюджета:


# todo сделать разбор: 8. 11616
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(alphabet[3:17:2])
from itertools import *
cnt = 0
for s in product(alphabet[:17], repeat=5):
    num = ''.join(s)
    if num[0] != '0':
        if num.count('1') <= 2:
            for a in alphabet[3:17:2]:
                num = num.replace(a, '*')
            if '1*' not in num and '*1' not in num and '11' not in num:
                cnt += 1

print(cnt)
'''

# 9. 11617
# 13. 11791
# 14. 11622
# 18. 11626
# 23. 11629
# 24. 11630
# 25. 11718


# todo Сделать разбор: 9 №11228
'''
from itertools import *
summa = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    copied_2 = [x for x in M if M.count(x) == 2]
    copied_3 = [x for x in M if M.count(x) == 3]
    if len(copied_3) == 3 and len(copied_2) == 4:
        if any(sum(p[:2]) % 2 != 0 and sum(p[2:]) % 2 != 0 for p in permutations(M[:4])):
            summa += sum(M)
print(summa)
'''


# todo: Сделать разбор № 8960 Джобс 02.06.2023 (Уровень: Базовый)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

k = 0
for x in range(500_001, 10**10):
    summa = sum(divisors(x))
    if fnmatch(str(summa), '*7?'):
        print(x, summa)
        k += 1
        if k == 5:
            break
'''
# Ответ:
# 500001 666672
# 500048 968874
# 500069 500070
# 500079 666776
# 500114 750174



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



# todo Собрать пост с тремя способами решения 8 номера

# Тип 8 №3700
# Все 5-буквенные слова, составленные из букв Б, К, Ф, Ц, записаны
# в алфавитном порядке и пронумерованы. Вот начало списка:
# 1. БББББ
# 2. ББББК
# 3. ББББФ
# 4. ББББЦ
# 5. БББКБ
#
# Запишите слово, которое стоит на 486-м месте от начала списка.

# Вариант 1
'''
s = sorted('БКФЦ')
print(s)  # ['Б', 'К', 'Ф', 'Ц']
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    n += 1
                    if n == 486:
                        print(n, slovo)
'''

# Вариант 2
'''
from itertools import *
n = 0
for p in product(sorted('БКФЦ'), repeat=5):
    slovo = ''.join(p)
    n += 1
    if n == 486:
        print(n, slovo)
'''


# Вариант 3
'''
from itertools import *
for n, p in enumerate(product(sorted('БКФЦ'), repeat=5), 1):
    slovo = ''.join(p)
    if n == 486:
        print(n, slovo)
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


# todo Разобрать № 4333 Пробный 06.2022 /dev/inf advanced (Уровень: Средний)
# У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавить 1
# 2. Прибавить 3
# 3. Возвести в квадрат

# Известно, что исполнитель не может повторить команду,
# выполненную на предыдущем шаге.
#
# Сколько существует программ, для которых при исходном числе 1 результатом
# является число 25, и при этом траектория вычислений содержит число 5,
# но не содержит число 6?
'''
def F(a, b, c):
    if a >= b or a == 6:
        return a == b
    if c == '1':
        return F(a + 3, b, '2') + F(a ** 2, b, '3')
    if c == '2':
        return F(a + 1, b, '1') + F(a ** 2, b, '3')
    if c == '3':
        return F(a + 1, b, '1') + F(a + 3, b, '2')
    return F(a + 1, b, '1') + F(a + 3, b, '2') + F(a ** 2, b, '3')


print(F(1, 5, '') * F(5, 25, ''))
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


# todo Разбор на канал № 11953 (Уровень: Средний)
'''
from functools import lru_cache


@lru_cache(None)
def F(a, b):

    if a >= b or a == 100:
        return a == b

    count = 0

    x = a % 10  # Команда A: Прибавить последнюю цифру
    if x != 0:
        count += F(a + x, b)

    x = a % 68   # Команда B: Добавить остаток от деления на 68
    if x != 0:
        count += F(a + x, b)

    x = a ** 2   # Команда C: Возвести в квадрат
    if x != a:
        count += F(x, b)

    return count


print(F(2, 68) * F(68, 680))
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


# todo сделать пост https://education.yandex.ru/ege/task/2f0244ec-e26c-4ebe-a8dd-7b32e94d30e4
# Поиск чисел с полными квадратами
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


cnt = 0
for x in range(10**7+1, 10**10):
    # d = [j for j in divisors(x) if (j**0.5) == int(j**0.5)]
    d = [j for j in divisors(x) if (j**0.5).is_integer()]
    if len(d) == 3:
        print(x, max(d))
        cnt += 1
        if cnt == 5:
            break
'''

# todo Сделать разбор Задание 25 https://education.yandex.ru/ege/task/2135bad3-5844-4cbd-8a72-93751f24130f
'''
from fnmatch import *
d = [14, 24, 34, 44, 54, 64, 74, 84, 94]
for x in range(124, 10**10, 124):
    if fnmatch(str(x), '1*28?64'):
        D = [j for j in d if x % j == 0]
        if len(D) == 5:
            print(x, x // 124)
'''
# t.me/informatika_kege_itpy



# todo сделать разбор Задание 13  https://education.yandex.ru/ege/task/c76b728d-6c5e-40c8-a212-acafbcdcbd0c
'''
from ipaddress import *
net = ip_network('192.168.160.0/255.255.224.0', 0)
# print(f'{mask:b}')  # 11111111111111111110000000000000
mask = f'{net.netmask:b}'.count('1')
cnt = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') == mask:
        cnt += 1
print(cnt)
'''


# todo Задание 13  https://education.yandex.ru/ege/task/8cabd46a-2193-441f-b07b-64a2bdf117a5
# Отличная задача превого прототипа
'''
from ipaddress import *
net = ip_network('95.112.224.0/255.255.255.128', 0)
cnt = 0
for ip in net:
    b = f'{ip:b}'[24:]  # правый байт - последние 8 бит
    if b == b[::-1]:
        cnt += 1
print(cnt)
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


# todo сделать разбор Задание 12 https://education.yandex.ru/ege/task/ebd5c150-9b1a-44f5-99f9-b0c6adfa95d9
# Определите, сколько различных строк может получиться в результате её работы.
'''
my_set = set()
for n in range(4, 1000):
    s = '4' + '9' * n

    while '44' in s or '9299' in s or '49' in s:
        s = s.replace('49', '944', 1)
        s = s.replace('44', '2', 1)
        s = s.replace('9299', '4', 1)
    my_set.add(s)
print(len(my_set))
'''

# todo сделать разбор https://education.yandex.ru/ege/task/e327b270-8faa-450f-a350-e313a28bbee9
'''
from itertools import *
cnt = 0
for p in product('0123', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if any(num.count(x) >= 2 for x in num):
            cnt += 1
print(cnt)
'''
# Ответ: 174


# Сделать разбор задачи с канала
'''
def my_int(num, base):
    return sum(x*base**i for i, x in enumerate(num[::-1]))


for x in range(1, 39):
    for y in range(1, 39):
        A = my_int([5, 8, x, 7, 2, 3, y, 4, 9], 39)
        B = my_int([y, x], 39)
        if A % 38 == 0:
            if (B ** 0.5).is_integer():
                print(B)
'''

# Ответ: 50


# todo сделать пост # 16 https://education.yandex.ru/ege/task/e6698118-3eea-44a7-9649-652cc0eb183a

# RecursionError: maximum recursion depth exceeded
'''
import sys
sys.setrecursionlimit(1000)

def F(n):
    if n <= 1:
        return 0
    if n > 1 and n % 6 == 0:
        return n + F(n/6 - 2)
    if n > 1 and n % 6 != 0:
        return n + F(n + 6)


for n in range(1000, 10000):
    try:
        if F(n) > 4242:
            print(n)
            break
    except RecursionError:
        continue
'''


'''
s1 = 8000 + 14400 + 14400 + 5700 + 8800 + 8800 + 8800 + 8000 + 7000 + 8000 + 14400 + 8000
s2 = 14400 + 8000 + 14400 + 4800 + 8800 + 8000 + 4800 + 4800 + 12000
print(s1)
print(s2)
print(s1 + s2)
'''
# RecursionError: maximum recursion depth exceeded

# todo сделать разбор 7 https://education.yandex.ru/ege/task/2640303f-cc77-424f-989c-f142e11c46f6
'''
i = 24  # 2**24 - цветов
i2 = 8  # 2**8 - прозрачности
pixels = 1024 * 768
# bit = pixels * (i + i2)
bit = pixels * (24 + 8)
print(bit / 2**13)
'''
# Ответ: 3072

'''
from itertools import *


def f(a, b, c, d):
    return ((a <= b) == c) or d


for p in permutations('abcd'):
    for q1, q2, q3, q4 in product([0, 1], repeat=4):
        table = [(1, 0, 1, q1),
                 (1, 0, q2, 1),
                 (q3, q4, 1, 0)]
        if len(set(table)) == len(table):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)



from itertools import *

def F(x, y, z, w):
    return ((w <= y) <= x) or (not z)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    table = [(a1, a2, 1, a3),
             (a4, 0, a5, a6),
             (a7, 1, 0, 0)]
    if len(set(table)) != len(table):
        for i in permutations('xyzw'):
            if [F(**dict(zip(i, r))) for r in table] == [0, 0, 0]:
                print(*i, sep='')

# Ответ: zywx
'''


# todo Сделать разбор # № 17799 (Уровень: Средний)
'''
from itertools import *
n = 0
for p in product(sorted('АРГУМЕНТ'), repeat=4):
    word = ''.join(p)
    n += 1
    if len(word) == len(set(word)):
        if list(word) == sorted(word):
            print(n)


from itertools import *
s = sorted('АРГУМЕНТ')
for n, p in enumerate(product(s, repeat=4), 1):
    word = ''.join(p)
    if len(word) == len(set(word)):
        if list(word) == sorted(word):
            print(n)
'''




# todo сделать разбор 19254
'''
s = open('0. files/24.txt').readline()
s = s.split('FSRQ')
maxi = 0
for i in range(len(s)-80):
    r = 'SRQ' + 'FSRQ'.join(s[i:i+81]) + 'FSR'
    maxi = max(maxi, len(r))
print(maxi)
'''


# todo сделать разбора № 18258 (Уровень: Сложный)



# todo № 15413 (Уровень: Средний)

'''from itertools import *
cnt = 0
for i in product('012345678', repeat=4):
    s = ''.join(i)
    if s[0] not in '0':
        if s.count('8') == 1:
            v = s.index('8')
            if sum(map(int, s[:v])) == sum(map(int, s[v+1:])):
                cnt += 1
print(cnt)'''


'''
s = open('0. files/IlonaValerya.txt').readline()
maxi = 0
for x in 'KLMN':
    s = s.replace(x, 'K')
for x in '123':
    s = s.replace(x, '2')
for i in range(len(s)):
    cnt1 = 0
    cnt2 = 0
    for j in range(i+1, len(s)):
        if s[j] == '2':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt2 == cnt1 * 2:
            maxi = max(maxi, len(s[i:j]))
print(maxi)
'''

'''
s = open('0. files/24.txt').readline()
maxi = 0
for x in 'KLMN':
    s = s.replace(x, 'K')
for x in '123':
    s = s.replace(x, '2')
for i in range(len(s)):
    for j in range(i+1, len(s)):
        r = s[i + 1:j + 1]
        if r.count('K') == r.count('2') * 2:
            # print(maxi, r.count('K'), r.count('2'), r)
            maxi = max(maxi, len(r))
print(maxi)
'''


# todo будто можно добавить в практику № 12779 (Уровень: Средний)
# № 12779 (Уровень: Средний)
'''
def F(n, x):
    if n >= 3000:
        return n
    if n < 3000:
        return n + x + F(n+2, x)


for x in range(-100, 100):
    if F(2984, x) - F(2988, x) == 5916:
        print(x)
'''


# todo Разобрать номер: # № 15413 (Уровень: Средний)
# (А. Вдовин) Найдите количество четырехзначных чисел в девятеричной системе счисления,
# в которых есть ровна одна цифра 8, а сумма цифр слева от нее равна сумме цифр справа от нее.
# Примечание: если слева или справа от 8 цифр нет, то сумма считается равной нулю
'''
from itertools import *
cnt = 0
for p in product('012345678', repeat=4):
    num = ''.join(p)
    if num[0] != '0':
        if num.count('8') == 1:
            i = num.index('8')
            summa_left = sum(map(int, num[:i]))
            summa_right = sum(map(int, num[i+1:]))
            if summa_left == summa_right:
                cnt += 1
print(cnt)
            # print(summa_left, num, summa_right)
            # i 0123
            #   2840  i = num.index('8') == 1
            # num[:i] num[i+1:]
'''

# todo сделать подробный разбор
'''
from itertools import permutations

table = '12 16 18 21 23 24 26 27 28 32 35 37 42 47 53 58 61 62 72 73 74 81 82 85'
graph = 'АВ ВА АГ ГА ВГ ГВ ВЕ ЕВ ЕГ ГЕ ЕЖ ЖЕ ЖИ ИЖ ИД ДИ ИГ ГИ ГБ БГ БД ДБ ДГ ГД'

for per in permutations('АБВГДЖИЕ'):
    new_table = table
    for i in range(1, 8+1):
        new_table = new_table.replace(str(i), per[i-1])
    if set(new_table.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)


Получаем две подходящие перестановки:

1 2 3 4 5 6 7 8
В Г И Б Ж А Д Е

1 2 3 4 5 6 7 8
Д Г Е А Ж Б В И

Отсюда находим, что первая перестановка не подходит так как: ЕЖ(58) = 28, а БГ(42) = 20

Берем вторую перестановку: ЕЖ(35) = 16, а БГ(62) = 26.
Тогда ВГ(72) = 25, а ГБ(26) = 26 -> 25 + 26 = 51

Ответ: 51'
'''


# todo Разбор на канал № 6093 /dev/inf 02.2023 (Уровень: Средний)
'''
def F(a, c):
    global cnt
    if c > 3:
        return 0
    else:
        if a % 2 == 0:
            cnt += 1
    return F(a+1, c+1) + F(a+2, c+1) + F(a*3, c+1)


cnt = 0
F(4, 0)
print(cnt)

# Вариант 2
def F(a, c):
    if c > 3:
        return 0
    return (a % 2 == 0) + (F(a+1, c+1) + F(a+2, c+1) + F(a*3, c+1))

cnt = F(4, 0)
print(cnt)
'''


# todo Разобрать № 5838 (Уровень: Средний)
'''
def F(a, b, c):
    if a > b:
        return 0
    elif a == b:
        if len(c) % 2 != 0 and all(x == 'B' for x in c[1::2]):
            return 1
        else:
            return 0

    else:
        return F(a+3, b, c+'A') + F(a+2, b, c+'B') + F(a*2, b, c+'C')


print(F(1, 50, ''))

# Вариант 2
def F(a, b, c):
    if a >= b:
        return a == b and len(c) % 2 != 0 and all(x == 'B' for x in c[1::2])

    return F(a+3, b, c+'A') + F(a+2, b, c+'B') + F(a*2, b, c+'C')


print(F(1, 50, ''))
'''


# todo сделать разбор номера 9 № 18258 (Уровень: Сложный)
'''
R = []
for n, s in enumerate(open('0. files/9.csv'), 1):
    M = [int(x) for x in s.split(';')]
    if M == sorted(M):
        if any(M.count(x) > 1 and sum(map(int, str(x))) % 2 == 0 for x in M):
            R.append(n)
print(max(R))
'''


# todo сделать разбор номера 14 № 18265 (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase

for i in range(len(alphabet)):
    print(i, alphabet[i])

for p in range(30, 37):
    for s in range(10, 35):
        A = int(f'R4', p-1)
        B = int(f'B0', s+2)
        C = int(f'T3NK4', p)
        if (A + B + C) == 23593399:
            print(p * s)
'''

# todo сделать разбор номера 17 № 18257 (Уровень: Средний)
'''
R = []
M = [int(x) for x in open('0. files/17.txt')]
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    i, j = i+1, i+2
    if (i + j) % 10 == max(M) % 10:
        R.append(abs((x+y) - (i+j)))
print(len(R), min(R))
'''


# todo сделать разбор 17 https://education.yandex.ru/ege/task/6488e44b-c19d-41be-a53f-3877c2d12728
'''
M = [int(s) for s in open('0. files/17.txt')]
R = []
for i in range(len(M)-5):
    x, y, z, w, r, t = M[i:i+6]
    if (z + w) > (x + y) and (z + w) > (r + t):
        if z + w > 0 and x + y > 0 and r + t > 0:
            R.append(z * w)
print(len(R), min(R))
'''


# todo сделать разбор 25 https://education.yandex.ru/ege/task/e9239096-46bf-4dab-a19b-ad07eed75bb4
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div.append(j)
            div.append(x // j)
    return sorted(set(div))


for x in range(106732567, 152673836+1):
    if (x**0.5).is_integer():
        d = divisors(x)
        if len(d) == 3:
            print(x, max(d))
'''


# todo сделать разбор https://education.yandex.ru/ege/task/ebbc8b9f-d709-47ff-b8f4-2c2e99ccb13b
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = sorted([int(x) for x in s.split(',')])
    if (M[-1] ** 3) >= 2 * (M[0] * M[1] * M[2]):
        if all(x > 10 for x in M):
            cnt += 1
print(cnt)
'''


# todo Разобрать на канал 17 номер № 16264 Джобс 03.05.24 (Уровень: Базовый)
'''
M = [int(x) for x in open('0. files/17.txt')]
D = [x for x in M if len(str(abs(x))) == 2 and x % sum(map(int, str(x))) == 0]
R = []
for i in range(len(M) - 1):
    x, y = M[i], M[i + 1]
    if (x % min(D) == 0) + (y % min(D) == 0) >= 1:
        R.append(x + y)
print(len(R), max(R))
'''


# todo Сделать разбор 8 номера № 7029 Danov2303 (Уровень: Базовый)
'''
from itertools import *

for n, p in enumerate(product(sorted('МАРИН'), repeat=8), 1):
    word = ''.join(p)
    if word == 'МАРИАННА':
        print(n)
        break
'''


# todo Сделать разбор 9 номер https://education.yandex.ru/ege/task/342217d2-3e89-4933-a422-940d9668bfa3
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(not_copied) == 3:
        if sum(copied3) ** 2 > sum(not_copied) ** 2:
            cnt += 1
print(cnt)
'''



# todo сделать разбор https://education.yandex.ru/ege/task/82c97d22-18da-44ce-aafa-9e25f9e55301
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied_2 = [x for x in M if M.count(x) == 2]
    if len(copied_2) == 6:
        a, b, c = sorted(set(copied_2))
        if a**2 + b**2 == c**2:
            cnt += 1
print(cnt)
'''

# todo сделать разбор

'''
from fnmatch import *
for x in range(124, 10**10, 124):
    if fnmatch(str(x), '1*28?64'):
        divisors = [x % j == 0 for j in (14, 24, 34, 44, 54, 64, 74, 84, 94)]
        if sum(divisors) == 5:
            print(x, x // 124)
'''


# todo Разобрать Даше
#  https://education.yandex.ru/ege/task/ebdb9a1e-1e94-4af0-8ce6-003009385c7d
'''
from ipaddress import *
net = ip_network('172.16.8.0/255.255.252.0', 0)
cnt = 0
for ip in net:
    cnt += 1
print(cnt)  # 1022 (минус широковещательного адреса)

print(cnt / 33)
'''


# todo Сделать разбор
'''
from ipaddress import *
R = []
for mask in range(0, 33):
    net = ip_network(f'218.48.192.56/{mask}', 0)
    if '218.48.192.0' in str(net):
        if len(list(net.hosts())) >= 500:
            R.append(str(net.netmask).split('.')[2])
print(len(set(R)))
'''


# todo Сделать разбор 24 номера № 14512 (Уровень: Средний)
'''
s = open('0. files/24.txt').readline()
s = s.replace('1', '1 1').replace('8', '8 8')
maxi = 0
for x in s.split():
    if x.count('1') == 1:
        if x.count('B') == x.count('C'):
            maxi = max(maxi, len(x))
print(maxi)
# print(max([len(x) for x in s.split() if x.count('1') == 1 and x.count('B') == x.count('C')]))
'''



# todo сделать разборы № 19719 (Уровень: Базовый)
'''
s = open('0. files/24.txt').readline()
while any(p in s for p in ('**', '--', '-*', '*-')):
    for x in ('**', '--', '-*', '*-'):
        s = s.replace(x, ' ')


maxi = 0
s = s.split()
for x in s:
    try:
        eval(x) 
        maxi = max(maxi, len(x))
    except Exception as e:
        continue
print(maxi)
'''
