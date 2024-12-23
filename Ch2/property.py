from math import atan2

class ComplexRI(Complex):
    def __init__(self, real, imag):
        # 初始化复数的实部和虚部
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        """
        计算复数的幅度
        通过实部和虚部的平方和的平方根来计算
        """
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        """
        计算复数的角度
        使用反正切函数atan2来根据实部和虚部计算角度
        """
        return atan2(self.imag, self.real)

    def __repr__(self):
        # 定义复数的字符串表示形式
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

##@property 装饰器定义了 magnitude 和 angle 两个属性，它们分别根据实部和虚部计算复数的幅度和角度。
##这样，在访问 ComplexRI 类的实例的 magnitude 或 angle 属性时，就会自动调用相应的方法来计算并返回结果，而无需显式地调用方法，使代码更加简洁和直观。

# 创建一个复数实例
complex_num = ComplexRI(3, 4)
# 访问复数的实部
print(complex_num.real)  
# 访问复数的虚部
print(complex_num.imag)  
# 访问复数的幅度，自动调用magnitude属性的getter方法计算
print(complex_num.magnitude)  
# 访问复数的角度，自动调用angle属性的getter方法计算
print(complex_num.angle)  