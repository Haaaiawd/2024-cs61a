# 典型的强制函数，将有理数转换为虚部为零的复数
def rational_to_complex(r):
    """将有理数转换为复数"""
    return ComplexRI(r.numer/r.denom, 0)

class Number:
    # 通过尝试将两个参数强制转换为相同类型来执行交叉类型操作
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        # 如果两个参数类型相同，直接返回
        if self.type_tag == other.type_tag:
            return self, other
        # 如果(self.type_tag, other.type_tag)在coercions字典中，将self转换为other的类型
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
        # 如果(other.type_tag, self.type_tag)在coercions字典中，将other转换为self的类型
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))

    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)

    # coercions字典通过一对类型标签索引，存储将第一种类型转换为第二种类型的强制函数
    coercions = {('rat', 'com'): rational_to_complex}

