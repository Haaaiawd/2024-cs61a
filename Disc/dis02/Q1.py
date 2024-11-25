def team(work):
    # 返回t(work) - 1，此时t未确定具体值，在后续代码中会被赋值
    return t(work) - 1

def dream(work, s):
    # 如果work(s - 2)为真
    if work(s - 2):
        # 将t赋值为not s，这里会改变全局变量t的值
        t = not s
    # 返回not t
    return not t

# 给work赋值为3，给t赋值为abs函数(**abs**是关键)
work, t = 3, abs
# 调用dream函数，传入team函数和work + 1（即4），然后与t进行逻辑与运算，结果赋值给team
team = dream(team, work + 1) and t