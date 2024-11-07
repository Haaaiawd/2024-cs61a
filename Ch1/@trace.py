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