def make_withdraw(balance):
        """Return a withdraw function that draws down balance with each call."""
        def withdraw(amount):
            nonlocal balance                 # Declare the name "balance" nonlocal
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount       # Re-bind the existing balance name(在已改变的名称上重新绑定)
            return balance
        return withdraw
##nonlocal 语句声明，每当我们将名称 balance 的绑定更改时，绑定将在 balance 已经绑定的第一个框架中更改。
##nonlocal 用于在嵌套函数中修改外部非全局作用域中的变量。
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
	        return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw
	
wd = make_withdraw(20)
wd2 = make_withdraw(7)
wd2(6)
wd(8)
####不同的函数实例可以通过nonlocal维护各自独立的状态。
##如文档中第二次调用make_withdraw返回的wd2函数，
##它与wd函数虽然都基于make_withdraw定义，但各自拥有独立的balance绑定，彼此互不干扰。
# 定义连接器类，用来存储值以及关联相关约束
class Connector:
    def __init__(self):
        self.value = None
        self.constraints = []

    def set_value(self, value):
        if self.value is None:
            self.value = value
            self.notify_all()
        else:
            assert self.value == value, "Value already set and inconsistent"

    def connect(self, constraint):
        self.constraints.append(constraint)

    def notify_all(self):
        for c in self.constraints:
            c()

# 乘法约束函数，实现乘法运算相关的约束逻辑
def multiplier(a, b, result):
    def constraint():
        if a.value is not None and b.value is not None:
            result.set_value(a.value * b.value)
    a.connect(constraint)
    b.connect(constraint)
    result.connect(constraint)
    return constraint

# 加法约束函数，实现加法运算相关的约束逻辑
def adder(a, b, result):
    def constraint():
        if a.value is not None and b.value is not None:
            result.set_value(a.value + b.value)
    a.connect(constraint)
    b.connect(constraint)
    result.connect(constraint)
    return constraint

# 常数约束函数，用于设置固定的常数值
def constant(x, value):
    x.set_value(value)
    return x

####我们将使用消息传递系统来协调约束和连接器。
##约束是不持有自身局部状态的字典。它们对消息的响应是非纯函数，会改变它们所约束的连接器。

celsius['forget']('user')
Celsius is forgotten
Fahrenheit is forgotten

##连接器 celsius 发现最初设置其值的 user 现在正在撤回该值，
# 因此 celsius 同意放弃其值，并通知网络这一事实。此信息最终传播到 fahrenheit ，
# 现在它发现没有理由继续相信自己的值是 77。因此，它也放弃了其值

connector['set_val'](source, value) #indicates that the source is requesting the connector to set its current value to value.
connector['has_val']() #returns whether the connector already has a value.
connector['val'] #is the current value of the connector.
connector['forget'](source) #tells the connector that the source is requesting it to forget its value.
connector['connect'](source) #tells the connector to participate in a new constraint, the source.

def make_ternary_constraint(a, b, c, ab, ca, cb):
        """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
        def new_value():
            av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
            if av and bv:
                c['set_val'](constraint, ab(a['val'], b['val']))
            elif av and cv:
                b['set_val'](constraint, ca(c['val'], a['val']))
            elif bv and cv:
                a['set_val'](constraint, cb(c['val'], b['val']))
        def forget_value():
            for connector in (a, b, c):
                connector['forget'](constraint)
        constraint = {'new_val': new_value, 'forget': forget_value}
        for connector in (a, b, c):
            connector['connect'](constraint)
        return constraint
    ##该名为 constraint 的字典是一个调度字典，同时也是约束对象本身。
    ##它响应约束接收到的两条消息，同时也是在调用其连接器时作为 source 参数传递的。
