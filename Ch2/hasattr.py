# 定义一个简单的类
class MyClass:
    def __init__(self):
        self.attribute1 = "This is attribute 1"
        self.attribute2 = 42

    def method1(self):
        return "This is method 1"
# 创建类的实例
obj = MyClass()

# 检查对象是否具有指定的属性
print(hasattr(obj, 'attribute1'))  
# 输出：True
print(hasattr(obj, 'attribute3'))  
# 输出：False