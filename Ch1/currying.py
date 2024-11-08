def curried_pow(x):
    def h(y):
        ##这里设了一个新的y，因此使用时就有两个参数了
        return pow(x, y)
    return h
##相当于f(x)成了底为x,指数为y的函数，并可以使用函数格式表达

assert curried_pow(2)(3) == 8, "看看对不对"

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
        
map_to_range(0, 10, curried_pow(2))

#>>> def curry2(f):
#        """Return a curried version of the given two-argument function."""
#        def g(x):
#            def h(y):
#                return f(x, y)
#            return h
#        return g
####这个将参数式转为柯里式，可以领f =pow,就可以一次用两至多个参数了

#>>> def uncurry2(g):
#        """Return a two-argument version of the given curried function."""
#        def f(x, y):
#           return g(x)(y)
#        return f
####反过来，将转为两个参数版本