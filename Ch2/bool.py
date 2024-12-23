'''
**用户定义类的真值判断** :
    - **默认情况**：默认情况下，用户定义类的对象被认为是真值。
    - **使用__bool__方法**：若类中定义了`__bool__`方法，Python会调用该方法来确定对象的真值。例如，对于一个表示银行账户的`Account`类，若希望余额为0的账户对象为假值，可以这样定义`__bool__`方法：
  python
##Account.__bool__ = lambda self: self.balance!= 0
'''
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __bool__(self):
        return self.balance!= 0
acc1 = Account("John", 100)
acc2 = Account("Alice", 0)
print(bool(acc1))  # 输出True，因为余额不为0
print(bool(acc2))  # 输出False，因为余额为0