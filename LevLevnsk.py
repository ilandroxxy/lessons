# region Домашка: ************************************************************


# endregion Домашка: ************************************************************
# #
# #
# region Урок: ************************************************************

'''
N2

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if (((x or (not (y))) and (not (y == z)) and (not (w))) == 1):
                    print(x,y,z,w)


res[x y z w
    0 0 1 0
    1 0 1 0           {x z y w}
    1 1 0 0]           1 1 0 0
                ===>   0 1 0 0
table[? ? ? ?          1 0 1 0
      1 1 ? ?
      ? 1 0 0
      1 ? 1 0]

'''
#5
'''
def toThird(n):
    t = ''
    while n > 0:
        t = str(n % 3) + t
        n = n//3
    return t

def f (n):
    t3=toThird(n)
    if(n%3==0):
        t3+=t3[-3:] #ВОПРОС- если строка состоить из 2 симаволов?
    else:
        t3+=toThird((n%3)*3)
    return int(t3,3)

m=[]
for i in range(9,100):
    temp=f(i)
    if(temp>150):
        m.append(i)
print(min(m)) #9
'''

'''
from string import *
alphabet = digits + ascii_uppercase
# alphabet = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')

def convert(n, b):
    t = ''
    while n > 0:
        t = alphabet[n % b] + t
        n = n // b
    return t

for n in range(1, 1000):
    t3 = convert(n, 3)
    if n % 3 == 0:
        t3 += t3[-3:]
    else:
        t3 += convert((n % 3) * 3, 3)
    r = int(t3, 3)
    if r > 150:
        print(n)
        break
'''



#8
'''
from itertools import *

abc = sorted(['С', 'Б', 'О', 'Р', 'Н', 'И', 'К'])

count = 0
m = []
p=list(product (abc,repeat=6))

for i in p:
    count += 1
    if ((i[0] != 'Р') and (i.count('Б') == 2) and (i.count('К') <= 1)):
        m.append(count)

print(max(m))  # 401
'''

# Номер 8
'''
from itertools import *
for n, p in enumerate(product(sorted('СБОРНИК'), repeat=6), 1):
    word = ''.join(p)
    if word[0] != 'Р' and word.count('Б') == 2 and word.count('К') <= 1:
        print(n, word)
'''


# Номер 9
'''
cnt = 0
for s in open('0. files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied2 = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(uncopied) == 3:
        if sum(copied2) / 4 < sum(uncopied) / 3:
            cnt += 1
print(cnt)
'''

# Номер 12
'''
for n in range(4, 10000):
    s = '5' + '2' * n

    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    summa = 0
    for x in s:
        summa += int(x)

    summa = sum([int(x) for x in s])

    summa = sum(map(int, s))

    if summa == 64:
        print(n)
        break
'''

#15
'''
from itertools import count

m = []


def f(a):
    count=0
    n=100
    for y in range(n):
        for x in range(n):
            if ( ( (x<a) or ((3*y + 2*x)>120) or (a>y) ) == 1):
                count+=1
    return count==(n**2)

for a in range(100):
    if(f(a)): m.append(a)

print(min(m))#25
'''

# Номер 15
'''
def F(x, y, A):
    return (x < A) or (3*y + 2*x > 120) or (A > y)

for A in range(1, 10000):
    if all(F(x, y, A) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''


# print(min([A for A in range(1, 10000) if all( ((x < A) or (3*y + 2*x > 120) or (A > y)) for x in range(1, 100) for y in range(1, 100)) ]))


#16
'''
from sys import *

setrecursionlimit(2500)


def f(n):
    if n == 1:
        return 1
    return n - 1 + f(n - 1)


print(f(2024) - f(2022))  # 4045
'''

#19-20-21
'''
def gameOver(pos):
    return pos>=473

def moves(pos):
    return pos+1,pos+5,pos*4

def win(pos,m):
    if(gameOver(pos)): return m%2==0
    if(m==0):return False
    r=[win(move,m-1)
       for move in moves(pos)]
    return any(r) if m%2 !=0 else \
        all(r)

for i in range(1,472):
    if(win(i,3)):print(i) #менять {m} в различных условиях
    #118;(113,117);113(???)
'''
#25
'''
from fnmatch import fnmatch

for i in range(2023, 10 ** 8, 2023):
    if fnmatch(str(i), "2*1?71"):
        print(i, i // 2023)
'''


#23
'''
def f(a, b):
    if (a >= b) or (a == 13): return a == b
    return f(a + 1, b) + f(a + 2, b) + f(a * 3, b)


print(f(3, 8) * f(8, 18))  # 200
'''


# Номер 14
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:19]:
    A = int(f'83{x}916', 19)
    B = int(f'123{x}45', 19)
    C = int(f'67{x}89', 19)
    if (A + B + C) % 17 == 0:
        print((A + B + C) // 17)
'''

# Тип 14 №48388
'''
from string import *
alphabet = digits + ascii_uppercase

for x in alphabet[:12]:
    for y in alphabet[:12]:
        A = int(f'{x}231{y}', 12)
        B = int(f'78{x}98{y}', 14)
        if (A + B) % 99 == 0:
            print((A + B) // 99)
'''


# Тип 14 №56542
'''
from string import *
alphabet = digits + ascii_uppercase

for p in range(10, 36+1):
    for x in alphabet[:p]:
        for y in alphabet[:p]:
            if int(x+x+x+'8', p) + int(f'43{x}9', p) == int(y+y+'04', p):
                print(int(y+y+x, p))
'''

# № 19484 (Уровень: Базовый)
'''
n = 5 * 729**2024 + 3 * 243**1413 - 7*81**169 - 2*9**107 + 3017
R = []
while n > 0:
    R.append(n % 27)
    n //= 27
R.reverse()

print(sum([x for x in R if x % 2 == 0 and x <= 25]))

# Вариант 2
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    t = ''
    while n > 0:
        t = alphabet[n % b] + t
        n = n // b
    return t

n = 5 * 729**2024 + 3 * 243**1413 - 7*81**169 - 2*9**107 + 3017
r = convert(n, 27)
print(sum([alphabet.index(x) for x in r if x in alphabet[::2] and x <= 'P']))
'''


# № 20808 Апробация 05.03.25 (Уровень: Средний)
'''
from string import *
alphabet = digits + ascii_uppercase

def convert(n, b):
    t = ''
    while n > 0:
        t = alphabet[n % b] + t
        n = n // b
    return t

maxi = 0
for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    r = convert(n, 7)
    if maxi <= r.count('0'):
        maxi = r.count('0')
        print(x, maxi)
'''

# № 18169 (Уровень: Сложный)
'''
for x in range(20000, 300000):
    n = 3**2000 + 3**10 - x

    R = []
    while n > 0:
        R.append(n % 3)
        n //= 3
    if R.count(2) == 2000:
        print(x)
        break
'''


# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [14]
# КЕГЭ = []
# на следующем уроке: 5, 8, 9, 12, 15, 23, 25, 26/27
