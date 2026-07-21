





# № 31221 Резерв 22.06.26 (Уровень: Базовый)
# Адрес сети и широковещательный адрес не могут быть использованы
# для адресации сетевых устройств.
'''
from ipaddress import *
net = ip_network('64.237.228.143/255.255.248.0', 0)
for ip in net:
    print(ip)  # 64.237.224.0
print(64 + 237 + 224)
'''

'''
def get_moves(p1, p2):
    moves = []
    moves.append((max(0, p1 - 3), p2))
    moves.append((p1, max(0, p2 - 3)))
    moves.append((p1 // 3, p2))
    moves.append((p1, p2 // 3))
    return list(set(moves))


def is_win(p1, p2):
    return (p1 + p2) <= 53


for S in range(35, 200):
    p1, p2 = 19, S
    found = False

    for p_move in get_moves(p1, p2):
        if not is_win(*p_move):

            for v_move in get_moves(*p_move):
                if is_win(*v_move):
                    print(S)
                    found = True
                    break
            if found:
                break

    if found:
        break


# n = 1: Петя 1
# n = 2: Ваня 1
# n = 3: Петя 2
# n = 4: Ваня 2

# № 29974 Апробация 14.05.26 (Уровень: Базовый)

from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n-1), F(s - 7, n-1), F(floor(s / 4), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(16, 1000) if F(s, n=2)])
print([s for s in range(16, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(16, 1000) if F(s, n=4) and not F(s, n=2)])


# № 31227 Резерв 22.06.26 (Уровень: Базовый)

from math import ceil, floor
def F(a, s, n):
    if a + s <= 53:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a - 3, s, n-1), F(a, s - 3, n-1), F(floor(a / 3), s, n-1), F(a, floor(s / 3), n-1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(35, 1000) if F(19, s, n=2)])
print([s for s in range(35, 1000) if F(19, s, n=3) and not F(19, s, n=1)])
print([s for s in range(35, 1000) if F(19, s, n=4) and not F(19, s, n=2)])


# № 31227 Резерв 22.06.26 (Уровень: Базовый)


def F(a, s, n):
    if a + s >= 171:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 1, s, n-1), F(a, s + 1, n-1), F(a * 2, s, n-1), F(a, s * 2, n-1)]
    # return any(h) if (n - 1) % 2 == 0 else all(h)
    return any(h) if (n - 1) % 2 == 0 else any(h)

print([s for s in range(1, 145+1) if F(25, s, n=2)])
print([s for s in range(1, 145+1) if F(25, s, n=3) and not F(25, s, n=1)])
print([s for s in range(1, 145+1) if F(25, s, n=4) and not F(25, s, n=2)])
'''


def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        if str(a).count('1') > 0:
            return F(a + 1, b) + F(a, b)
        else:
            return F(a + 1, b)





