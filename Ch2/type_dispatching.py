'''
类型分派并不局限于使用isinstance函数来实现。
在处理算术运算时，我们可以为有理数（Rational）和复数（Complex）实例添加一个type_tag属性，
该属性值为字符串 。通过比较两个值的type_tag，我们可以决定如何进行组合操作。

>>> Rational.type_tag = 'rat'
>>> Complex.type_tag = 'com'
##相同类型_tag 的实例操作,直接x.add()
>>> Rational(2, 5).type_tag == Rational(1, 2).type_tag
True
>>> ComplexRI(1, 1).type_tag == ComplexMA(2, pi/2).type_tag
True

不同类型_tag 的跨类型操作
'''
def add_complex_and_rational(c, r):
    """将复数和有理数相加"""
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

def add_rational_and_complex(r, c):
    """交换参数顺序的加法跨类型操作，利用加法的交换律"""
    return add_complex_and_rational(c, r)

##示例##
'''
>>> c = ComplexRI(1, 1)
>>> r = Rational(2, 5)
>>> add_complex_and_rational(c, r)
ComplexRI(1.4, 1)
>>> add_rational_and_complex(r, c)
ComplexRI(1.4, 1)
'''
def mul_complex_and_rational(c, r):
    """将复数和有理数相乘"""
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def mul_rational_and_complex(r, c):
    """交换参数顺序的乘法跨类型操作，利用乘法的交换律"""
    return mul_complex_and_rational(c, r)

##示例##
'''
>>> c = ComplexMA(2, pi/2)
>>> r = Rational(-2, 5)
>>> mul_complex_and_rational(c, r)
ComplexMA(0.8, 1.5707963267948966)
>>> mul_rational_and_complex(r, c)
ComplexMA(0.8, 1.5707963267948966)
'''