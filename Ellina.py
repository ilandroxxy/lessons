
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************


# Задание 13 Апробация 04.03.26 вариант 2 (https://disk.yandex.ru/i/olGf9MsK09aN4g)
'''
from ipaddress import*
cnt=0
net=ip_network('172.16.160.0/255.255.240.0',0)
for ip in net:
   if f'{ip:b}'.count('1') % 2 == 0:
       cnt+=1
print(cnt)

ip = 8
print(f'{ip:b}')  # 1000
print(f'{ip}:b')  # 8:b
print('f{ip}:b')  # f{ip}:b
'''

# Задание 15 Апробация 04.03.26 вариант 2 (https://disk.yandex.ru/i/olGf9MsK09aN4g)
'''
def F(x, A):
    return (x % 21 == 0) <= ((x % A != 0) <= (x % 77 != 0))

for A in range(10000, 1, -1):
    if all(F(x, A) for x in range(1000000)):
        print(A)
        break

for a in range(10000, 1, -1):
    if all(  ((x % 21 == 0) <= ((x % a != 0) <= (x % 77 != 0))) for x in range(1000000)):
        print(a)
        break
'''


# Задание 17 Апробация 04.03.26 вариант 2 (https://disk.yandex.ru/i/olGf9MsK09aN4g)
'''
m=[int(x) for x in open('files/17.txt')]
max43=(max([x for x in m if 999<abs(x)<10000 and abs(x)%100==43]))**2
R = []
def f(n):
   if 999<abs(n)<10000: return 1
   else: return 0

for i in range(len(m)-1):
   a1=m[i]
   a2=m[i+1]
   a=(a1+a2)**2
   if (f(a1)+f(a2))!=0 and a<max43:
       R.append(a)
print(len(R), max(R))

M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if 999 < abs(x) < 10000]
B = [x for x in A if abs(x) % 100 == 43]
R = []
for i in range(len(m)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) >= 1:
        if (x + y) ** 2 < max(B) ** 2:
            R.append((x + y) ** 2)
print(len(R), max(R))
'''



# Задание 19-21 Апробация 04.03.26 вариант 2 (https://disk.yandex.ru/i/olGf9MsK09aN4g)
# 2 кучи: a+1, b+1, a*2, b*2 | a + b >= 207 | a = 17 | 1 < b <= 189
'''
def f(a, s, m):
    if (a + s) >= 207:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 1, s, m - 1), f(a, s + 1, m - 1), f(a * 2, s, m - 1), f(a, s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
    return any(h) if (m - 1) % 2 == 0 else any(h)


print([s for s in range(2, 190) if f(17, s, 2)])
print([s for s in range(2, 190) if f(17, s, 3) and not f(17, s, 1)])
print([s for s in range(2, 190) if f(17, s, 4) and not f(17, s, 2)])
'''


# Задание 16 Апробация 04.03.26 вариант 2 (https://disk.yandex.ru/i/olGf9MsK09aN4g)
'''
# F(257487) = (257487 + 4) * F(257482)
# F(257482) = (257482 + 4) * F(257477)
# F(257477) = (257477 + 4) + F(257472) / F(257472)

print(((257487 + 4) * (257482 + 4) * (257477 + 4)) / 683)
print((257477 + 4) / 67)
print(24994252792782 + 3843)
'''


# № 28761 Досрочная волна 2026 (Уровень: Средний)
'''
M = [int(x) for x in open('files/17.txt')]
B = [x for x in M if abs(x) % 23 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x%min(B)==0) + (y% min(B)==0) >= 1:
        R.append(x+y)
print(len(R), max(R))
'''

# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [12, 13, 19-21, 24.1, 27]
# КЕГЭ = []
# на следующем уроке: 27 номер с досрока

# Получаются: 1, 2, 3, 4, 6, 10, 11, 15, 17, 18, 23
# 50 / 50: 5, 7, 9, 16,
# Не получаются: 8, 14, 22, 25
# Не разбирали: 24, 26


# region 📖 Пробник (Вариант 2)

# Студент #Эллина
# Дата: #Понедельник #16Марта2026
# ✅ Верно: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 23, 25
# ⛔️ Неверно: 17, 18, 22, 27
# ❔ Без ответа: 6, 14, 24, 26
# Итог: 20/29 первичных балла ~ 78 вторичных

# endregion 📖 Пробник (Вариант 2)



