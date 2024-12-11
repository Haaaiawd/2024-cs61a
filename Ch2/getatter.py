# 导入模块和定义类，用于后续演示
import datetime

class MyClass:
    def __init__(self):
        self.attribute1 = "This is attribute 1"
        self.attribute2 = 42

    def method1(self):
        return "This is method 1"
# 创建类的实例
obj = MyClass()
# 获取对象的已有属性
attr1_value = getattr(obj, 'attribute1')
print(attr1_value)  
# 输出：This is attribute 1
    
# 使用点标记法获取属性
dot_attr1_value = obj.attribute1
print(dot_attr1_value)  
# 输出：This is attribute 1
