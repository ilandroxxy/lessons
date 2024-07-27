# region Домашка: ************************************************************

'''
my_list = [4, 5, 6, 9]

# del my_list[1]
# my_list.insert (1, 14)
my_list[1] = 14


# my_list.append(1)
# my_list.append(2)
# my_list.append(5)
my_list += [1, 2, 5]


del my_list[0]
my_list = (my_list * 3)
my_list.insert(4, 45)
print(my_list)
'''

'''
my_list = [3, 7, 1, 4, 9, 2]
my_list = [my_list[5]] + my_list[1:5] + [my_list[0]]
# TypeError: unsupported operand type(s) for +: 'int' and 'list'

# del my_list[0]
# my_list.insert(0, 2)
# del my_list[5]
# my_list.insert(5, 3)
print(my_list)
'''


'''
n = int(input())
my_list = [int(input()) for _ in range(n)]
my_list = sorted(my_list)
print(my_list[-2])
'''

'''
n = int(input())
my_list = [int(input()) for _ in range(n)]
print(my_list[0::2])  # Это все элементы стоящие на четных индексах 
# i        0  1  2  3   4   5  6   7  8
my_list = [3, 4, 2, 3, 42, 34, 2, 34, 2]
# [4, 2, 42, 34, 2, 34, 2]
# [3, 2, 42, 2, 2]


n = int(input())
my_list = [int(input()) for _ in range(n)]
print([x for x in my_list if x % 2 == 0]) 
'''

n = int(input())
my_list = [int(input()) for _ in range(n)]
A = [x for x in my_list if x < 0]  # x < 0
B = [x for x in my_list if x == 0]  # x == 0
C = [x for x in my_list if x > 0]  # x > 0
for x in A:
    print(x)
for x in B:
    print(x)
for x in C:
    print(x)

# endregion Домашка: *********************************************************
#
# #
# region Урок: ************************************************************



# endregion Урок: ************************************************************
# #
# #
# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************
# #
# ФИПИ = [2, 6]
# КЕГЭ = []
# на следующем уроке:
