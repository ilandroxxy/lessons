# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
'''
# 1

def f(s, n):
    if s >= 25: return n % 2 == 0
    if n == 0: return 0
    h = [f(s+2, n-1), f(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(1, 25) if f(s, 2)] )
print( [s for s in range(1, 25) if not f(s, 1) and f(s, 3)] )
print( [s for s in range(1, 25) if not f(s, 2) and f(s, 4)] )


# 2

def f(s, n):
    if s >= 33: return n % 2 == 0
    if n == 0: return 0
    h = [f(s+3, n-1), f(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(1, 33) if f(s, 2)] )
print( [s for s in range(1, 33) if not f(s, 1) and f(s, 3)] )
print( [s for s in range(1, 33) if not f(s, 2) and f(s, 4)] )



# 3

def f(s, n):
    if s >= 1000: return n % 2 == 0
    if n == 0: return 0
    h = [f(s+100, n-1), f(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( len([s for s in range(1, 1000) if f(s, 2)]) )
print( len([s for s in range(1, 1000) if not f(s, 1) and f(s, 3)]) )
print( [s for s in range(1, 1000) if not f(s, 2) and f(s, 4)] )


# 5

def f(s, n):
    if s >= 34: return n % 2 == 0
    if n == 0: return 0
    h = [f(s+1, n-1), f(s+2, n-1), f(s+3, n-1), f(s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(1, 34) if f(s, 2)] )
print( [s for s in range(1, 34) if not f(s, 1) and f(s, 3)] )
print( [s for s in range(1, 34) if not f(s, 2) and f(s, 4)] )



# 10

def f(a, s, n):
    if s+a >= 69: return n % 2 == 0
    if n == 0: return 0
    h = [f(a+2, s, n-1), f(a, s+2, n-1), f(a*2, s, n-1), f(a, s*2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(1, 60) if f(9, s, 2)] )
print( [s for s in range(1, 60) if not f(9, s, 1) and f(9, s, 3)] )
print( [s for s in range(1, 60) if not f(9, s, 2) and f(9, s, 4)] )


# 11

def f(a, s, n):
    if s+a <= 20: return n % 2 == 0
    if n == 0: return 0
    h = [f(a-1, s, n-1), f(a, s-1, n-1), f((a+1)//2, s, n-1), f(a, (s+1)//2, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h)

print( [s for s in range(11, 60) if f(10, s, 2)] )
print( [s for s in range(11, 60) if not f(10, s, 1) and f(10, s, 3)] )
print( [s for s in range(11, 60) if not f(10, s, 2) and f(10, s, 4)] )
'''


# endregion Урок: *************************************************************
# #
# #
# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************
# #
# #
# ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:

