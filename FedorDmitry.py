# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


#5
'''
def R(N):
    t = N
    y = ''
    while t > 0:
        y += str(t % 3)
        t = t // 3
    y = y[::-1]
    if N % 3 == 0:
        y += y[-3:]
    else:
        y += str(N % 3) + '0'
    return int(y, 3)

for N in range(1, 100):
    if R(N) > 150:
        print(N)
        break
'''



#8
'''
def R(N):
    t=''
    while N>0:
        t+=str(N%7)
        N=N//7
    while len(t)<6:
        t+='0'
    t=t[::-1]

    return t
for N in range(7**6-1,0,-1):
    if  (R(N)[0]!='5' and R(N).count('0')==2 and R(N).count('2')<2 ):
        print(N+1)
        break

RES = []
s = sorted('СБОРНИК')
n = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        n += 1
                        if a != 'Р' or word[0] != 'Р':
                            if word.count('Б') == 2:
                                if word.count('К') <= 1:
                                    RES.append(n)
print(max(RES))


from itertools import product
n = 0
RES = []
for p in product(sorted('СБОРНИК'), repeat=6):
    word = ''.join(p)
    n += 1
    if word[0] != 'Р':
        if word.count('Б') == 2:
            if word.count('К') <= 1:
                RES.append(n)
print(max(RES))


RES = []
from itertools import product
for n, p in enumerate(product(sorted('СБОРНИК'), repeat=6), 1):
    word = ''.join(p)
    if word[0] != 'Р':
        if word.count('Б') == 2:
            if word.count('К') <= 1:
                RES.append(n)
print(max(RES))
'''


#9
'''
r=0
for s in open('files/9.csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied2 = [x for x in M if M.count(x) == 2]  # [9 9 8 8]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 4 and len(copied1) == 3:
        if (sum(copied2) / 4) < (sum(copied1) / 3):
            r+=1
print(r)
'''


#24
'''
t=open('files/24.txt').read()
y=[]
o=[]
for i in range(len(t)):
    if t[i]=='T':
        y.append(i)
o.append(y[209])
o.append(len(t)-y[-209])
for r in range(len(y[:-209])):
    o.append(y[r+209]-y[r])
print(min(o)+1)
'''


# № 28694 (Уровень: Базовый)
# Сколько существует чисел, двенадцатеричная запись
# которых содержит пять цифр, среди которых есть только
# две чётные цифры, причём они равны между собой и стоят рядом.
'''
cnt = 0
from itertools import product
for p in product('0123456789AB', repeat=5):
    num = ''.join(p)
    if num[0] != '0':
        chet = [x for x in num if x in '02468A']
        if len(chet) == 2:
            if chet[0] == chet[1]:
                if chet[0] * 2 in num:
                    cnt += 1
print(cnt)
'''


# № 24614 (Уровень: Средний)
'''
R = []
from itertools import permutations
for p in permutations('КОНФЕТЫ ИЛИ ЖИЗНЬ', r=7):
    word = ''.join(p)
    if '  ' in word:
        R.append(word)
print(len(set(R)))
'''


'''
R = []
from itertools import permutations
for p in permutations('МОЛОКО'):
    word = ''.join(p)
    R.append(word)
print(len(set(R)))
'''
# МОЛОКО
# МОЛОКО

'''
ip = '233.43.0.89'
print(ip.split('.'))  # ['233', '43', '0', '89']

P = ['233', '43', '0', '89']
T = ('233', '43', '0', '89')

s = ''.join(T)
print(s)  # 23343089

s = '**'.join(P)
print(s)  # 233**43**0**89
'''



# № 21407 Досрочная волна 2025 (Уровень: Базовый)
# Виктор составляет таблицу кодовых слов для передачи сообщений,
# каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов Виктор использует 5-буквенные слова,
# в которых могут быть только буквы Д, Г, И, А, Ш, Э, причём
# слово не должно начинаться с гласной и не должно заканчиваться согласной.
# Сколько различных кодовых слов может использовать Виктор?

'''
from itertools import product
cnt=0
for p in product(sorted('ДГИАШЭ'),repeat=5):
    word=''.join(p)
    if word[0] not in 'ИАЭ':
        if word[-1] not in 'ДШГ':
            cnt+=1
print(cnt)
'''


# № 19240 ЕГКР 21.12.24 (Уровень: Базовый)
# Все пятибуквенные слова, в составе которых могут быть только русские буквы Я, Н, В, А, Р, Ь,
# записаны в алфавитном порядке и пронумерованы, начиная с 1. Ниже приведено начало списка.
# 1. ААААА
# 2. ААААВ
# 3. ААААН
# 4. ААААР
# 5. ААААЬ
# 6. ААААЯ
# 7. АААВА
# …
# Под каким номером в списке идёт последнее слово, которое не начинается с буквы Я,
# содержит не более одной буквы Ь и не содержит букв Я, стоящих рядом?
'''
from itertools import product
W=[]
for n, p in enumerate(product(sorted('ЯНВАРЬ'),repeat=5), 1):
    word=''.join(p)
    if word[0] !='Я':
        if word.count('Ь')<=1:
            if 'ЯЯ' not in word:
                W.append(n)
print(max(W))
'''


# № 20270 (Уровень: Средний)
# (О. Лысенков) Сколько существует пятизначных семеричных чисел, в которых не менее 2-х
# раз четные цифры стоят рядом, при этом всем никакие три четные цифры не стоят рядом.
'''
from itertools import*
otv = 0
for i in product('0123456', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        ch = ''.join([str(int(x in '0246')) for x in s])
        if ch.count('11') >= 2:
            if '111' not in ch:
                otv += 1
print(otv)
'''


# № 19480 (Уровень: Средний)
# (Л. Шастин) Леонид составляет коды перестановкой букв слова ПАРИЖАНКА.
# При этом в этих кодах ровно один раз встречаются две идущие подряд гласные буквы.
# Сколько различных кодов может составить Леонид?
'''
r=[]
from itertools import permutations
for p in permutations(sorted('ПАРИЖАНКА')):
    word=''.join(p)
    slovo = word
    slovo = slovo.replace('И', 'А')
    if slovo.count('АА') == 1 and 'ААА' not in slovo:
        r.append(word)
print(len(set(r)))


s = 'АААА'
print(s.count('АА'))  # 2
s = 'ААА'
print(s.count('АА'))  # 1
'''


# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 27]
# КЕГЭ = [8, 15, 23]
# на следующем уроке:


# region 📖 Пробник (Вариант 2)

# Студент #Федор
# Дата: #Вторник #03Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 25
# ⛔️ Неверно: 6, 8, 10, 17, 22, 24, 27
# ❔ Без ответа: 26
# Итог: 19/29 первичных балла ~ 75 вторичных

# Студент #Вадим
# Дата: #Суббота #04Апреля2026
# ✅ Верно: 1, 2, 7, 10, 11, 12, 13, 14, 15, 16, 19, 20, 23, 25
# ⛔️ Неверно: 3, 4, 5, 6, 8, 9, 18, 21, 22, 24
# ❔ Без ответа: 17, 26, 27
# Итог: 14/29 первичных балла ~ 62 вторичных


# endregion 📖 Пробник (Вариант 2)



