

# № 18287 (Уровень: Базовый)
# todo Номер 5: Интересная задача с ловушкой под списки и минимальный r
'''
sp = []
for n in range(3, 10000):
    bn = bin(n)[2:]
    if len(bn) % 2 == 0:
        bn = bn + '1'
    else:
        bn = '1' + bn + '0'
    r = int(bn, 2)
    if r > 666:
        print(r)
        sp.append(r)
print(min(sp))
'''


# № 12469 (Уровень: Базовый)
# todo Номер 15: Интересная задача с отрезками
'''
def F(x, a1, a2):
    D = 7 <= x <= 68  # x ∈ D
    C = 29 <= x <= 100
    A = a1 <= x <= a2
    return (D) <= (((not C) and (not A)) <= (not D))


R = []
M = [x / 10 for x in range(5 * 10, 110 * 10)]
print(M)
for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2 - a1)

print(min(R))  # 21.8 -> 21.75 -> 21.9 -> 22
'''

