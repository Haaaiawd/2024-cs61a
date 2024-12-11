# 定义一个Account类，模拟账户相关操作，用于演示相关知识点
class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """
        定义withdraw方法，用于从账户中取款操作
        参数amount表示取款的金额
        """
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

# 创建Account类的一个实例对象spock_account，初始余额为1000
spock_account = Account(1000)

# 通过点标记（dot notation）调用withdraw方法，此时对象spock_account起到双重作用
# 1. 确定withdraw这个名称对应的是Account类中定义的方法
# 2. 自身被绑定到withdraw方法的第一个参数self上
spock_account.withdraw(300) 

# 以下是对相关知识点的详细解释说明
# 1. 关于点标记（dot notation）
#    格式为 <对象>.<方法名>(<参数列表>)，这里spock_account就是对象，withdraw是方法名
#    通过这种方式可以清晰地调用对象所属类中定义的方法

# 2. 对象的双重作用体现
#    首先，Python解释器根据对象spock_account找到其所属的Account类，进而确定withdraw是Account类内部定义的方法名称，
#    而不是其他地方随意定义的同名变量或函数等，这就确定了名称含义的唯一性和所属范围。
#    其次，在实际调用withdraw方法时，Python会自动将spock_account这个对象绑定到withdraw方法的self参数上，
#    这样在withdraw方法内部，就可以通过self来访问和操作spock_account这个对象的属性了，
#    比如在withdraw方法中通过self.balance来获取和修改账户余额。
# 总结来说，点标记调用方法这种方式以及对象所起的双重作用，是Python面向对象编程中很重要的机制，
# 方便对不同对象的操作进行区分和管理，同时也让方法能够准确地作用于对应的对象实例上，保持对象状态的独立性和可操作性。