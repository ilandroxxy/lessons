


# Самописные функции def в python
'''
import math as m
print(m.sqrt(16))  # 4.0
r = m.sqrt(16)
print(r)

def my_sqrt(x):
    result = x ** 0.5
    return result




def text_for_parents_ticets(name, count):
    text = (f'Доброго времени суток, {name}! \n'
            f'Кол-во занятий в абонементе: {count}')
    return text

print(text_for_parents_ticets('Илья', 3))
print(text_for_parents_ticets('Маша', 7))
'''


# Функция поиска простого числа и проверки
'''
def is_prime(n):
    """
    Функция проверка простого числа.
    :param n - число, которое будем проверять на простоту
    :return - функция возвращает True, если число прсостое, иначе возвращает False
    """
    if n <= 1:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


print(is_prime(7))  # True
print(is_prime(4))  # False

print([n for n in range(1, 100) if is_prime(n) == True])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# print(help(is_prime))
'''



# Функция поиска делителей числа

import time
start = time.time()


def divisors(n):
    d = []
    for j in range(1, int(n ** 0.5)+1):
        if n % j == 0:
            d.append(j)
            d.append(n // j)
    return sorted(set(d))

print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24] - четное кол-во делителей
print(divisors(16))  # [1, 2, 4, 8, 16] - нечетное кол-во делителей
print(divisors(1_000_000_000))

end = time.time()
print(end - start)  # 15.900 -> 0.00069



'''
print()
sum()
max()
min()
len()
range()


import math as m
m.floor()
m.dist()
m.sqrt()
'''

































