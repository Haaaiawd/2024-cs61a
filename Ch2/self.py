# 知识点：self 参数在 Python 类方法中的使用

# 1. self 参数是方法的第一个参数，代表类的实例对象本身
class Account:
    def __init__(self, balance):  # 构造方法，初始化对象的属性
        self.balance = balance  # self 用于访问和设置当前对象的属性

    def deposit(self, amount):  # deposit 方法，用于向账户存入金额
        # 对象本身与 self 绑定，这里的 self 代表当前的 Account 对象
        self.balance += amount  # 通过 self 访问和操作对象的属性（修改账户余额）
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def display_balance(self):
        # 同样通过 self 访问对象的 balance 属性，打印当前余额
        print(f"Current balance: {self.balance}")
        
# 创建一个 Account 对象
my_account = Account(1000)
# 调用 deposit 方法向账户存入金额
my_account.deposit(500)
# 调用 display_balance 方法查看当前余额
my_account.display_balance()