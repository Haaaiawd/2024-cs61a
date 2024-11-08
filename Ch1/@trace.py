def trace(fn):
    ##这里fn就是要装函数的,比如triple，来显示print里的信息
    def wrapped(x):
        print('-> ', fn, '(', x, ')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3 * x

##相当于
#def triple(x):
#    return 3 * x
#
#triple = trace(triple)

##装饰器符号@后面也可以跟一个调用表达式。
# @后面的表达式首先求值（就像上面的trace名称求值一样），
# 然后是def语句，最后将装饰器表达式的求值结果应用于新定义的函数，并将结果绑定到def语句中的名称。