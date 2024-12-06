def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))
    
def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)
##以上是分数的各个运算法则

from fractions import gcd
def rational(n, d):
    g = gcd(n, d)
    return (n//g, d//g)
##gcd最大公约数化简分数

