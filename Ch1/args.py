def test(*args):
    for i in args:
        print(i)

test(1, 2, 3, 4)  # 输出: 1 2 3 4
##*args  可以接受任意数量的参数，这些参数将被打包成一个元组。