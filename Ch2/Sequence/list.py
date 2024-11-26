#1. >>> [2, 7] + digits * 2
[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
##这个是list的加与乘运算

#2. >>> pairs = [[10, 20], [30, 40]]
#>>> pairs[1]
[30, 40]
#>>> pairs[1][0]
30

#3. >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
#>>> same_count = 0
#>>> for x, y in pairs:
#        if x == y:
#            same_count = same_count + 1
#
#>>> same_count
2
####分别把每个名称 x 和 y 绑定到每对中的第一个和第二个元素,
####多个名称绑定到固定长度序列中的多个值的模式称为序列解包。
######意思就是执行的时候自动拆开了序列，解包了每个序列的这两个值出来。

#4. 一种常见的约定是，如果在语句块中不使用名称，则在 for 头部使用单个下划线字符作为名称：
# >>> for _ in range(3):
#        print('加油，熊队！')
#加油，熊队！
#加油，熊队！
#加油，熊队！

#5. 列表推导式
#>>> nums = [12, 8, 13, 10, 44, 2, 1, 9]
#>>> [x*x for x in nums]
[144, 64, 169, 100, 1936, 4, 1, 81]

#6. map&filter在List里的应用
##>>> def apply_to_all(map_fn, s):
##        return [map_fn(x) for x in s]
##
##>>> def keep_if(filter_fn, s):
##        return [x for x in s if filter_fn(x)]
##
####下面是用了真map和filter来表示list.
####>>> apply_to_all = lambda map_fn, s: list(map(map_fn, s))
####>>> keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

#7. not in/ in 的用法
# >>> digits
[1, 8, 2, 8]
#>>> 2 in digits
True
#>>> 1828 not in digits
True

#8. 切片
#>>> digits[0:2]
[1, 8]
#>>> digits[1:]
[8, 2, 8]
####不加东西取到底，用-1表示倒数第一位(不取最后一个)