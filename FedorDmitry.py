# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************

'''
from itertools import*
otv = []
for i in product('012345678', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('3') == 2:
            for x in '1357':
                s = s.replace(x, '*')
            if '2*' not in s and '*2' not in s:
                otv.append(s)
print(len(otv))

from itertools import product
cnt=0
for i in product("012345678",repeat=5):
    i= ''.join(i)
    if i[0] != '0' and i.count('3')==2:
        i=i.replace('1','3')
        i=i.replace('5', '3')
        i=i.replace('7', '3')
        if i.count('32')==0 and i.count('23')==0 :
            cnt+=1
print(cnt)


from itertools import*
cnt = 0
for i in product('012345678', repeat = 5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('3') == 2:
            if all(pair not in s for pair in '23 32 21 12 52 25 27 72'.split()):
                cnt += 1
print(cnt)
'''


# Номер 13
# Для узла с IP-адресом 195.23.86.50, адрес сети равен 195.23.80.0.
# Для скольких различных значений маски это возможно?
'''
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f'195.23.86.50/{mask}', 0)
    if '195.23.80.0' in str(net):
        print(net, net.netmask)


# № 18955 (Уровень: Средний)
# Два узла, находящиеся в одной сети, имеют IP-адреса 200.154.190.12 и 200.154.184.0.
# Укажите наибольшее возможное количество единиц в маске этой сети

from ipaddress import *
for mask in range(1, 32+1):
    net1 = ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ip_network(f'200.154.184.0/{mask}', 0)
    if net1 == net2:
        print(mask, 32-mask)
'''


def G(S, h):
    if S >= 184:
        return 1
    elif S < 184 and h > 1:
        return 0
    if h % 2 == 0:
        return G(S + 1, h + 1) * G(S + 5, h + 1) * G(S * 4, h + 1)
    else:
        return G(S + 1, h + 1) + G(S + 5, h + 1) + G(S * 4, h + 1)


for S in range(1, 184):
    if G(S, 0):
        print(S)
        break

'''
def F(s, h):
    if s >= 184:
        return h % 2 == 0
    if h == 0:
        return 0
    M = [F(s + 1, h - 1), F(s + 5, h - 1), F(s * 4, h - 1)]
    return any(M) if (h - 1) % 2 == 0 else all(M)
    return any(M) if (h - 1) % 2 == 0 else any(M)

print([s for s in range(1, 184) if F(s, h=2)])
print([s for s in range(1, 184) if F(s, h=3) and not F(s, h=1)])
print([s for s in range(1, 184) if F(s, h=4) and not F(s, h=2)])
'''

# № 28704 (Уровень: Базовый)
'''
def F(a, s, h):
    if a * s >= 516:
        return h % 2 == 0
    if h == 0:
        return 0
    M = [F(a + 3, s, h - 1), F(a, s + 3, h - 1), F(a + 13, s, h - 1), F(a, s + 13, h - 1)]
    return any(M) if (h - 1) % 2 == 0 else all(M)
    return any(M) if (h - 1) % 2 == 0 else any(M)

print(len([s for s in range(1, 74) if F(7, s, h=2)]))
print(sorted([s for s in range(1, 74) if F(7, s, h=3) and not F(7, s, h=1)])[:2])
print(max([s for s in range(1, 74) if F(7, s, h=4) and not F(7, s, h=2)]))
'''



# endregion Урок: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25, 27]
# КЕГЭ = [8, 15, 16, 23, 25]
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



