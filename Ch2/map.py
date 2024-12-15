# `map` 函数基础概念与示例解释
# `map` 函数的基本特点
# `map` 函数是 Python 内置的高阶函数，接受一个函数和一个可迭代对象作为参数，返回一个迭代器对象。
# 具有惰性求值特性，调用时不会立刻执行传入函数对可迭代对象元素的操作，
# 而是等到通过**迭代请求**结果时，才逐个对元素应用传入函数进行计算并返回相应结果。

# 示例代码及执行过程分析
def double_and_print(x):
    print('***', x, '=>', 2 * x, '***')
    return 2 * x

s = range(3, 7)
doubled = map(double_and_print, s)

# 下面是逐步获取迭代器元素的操作及对应解释
# 调用 `next` 函数获取 `doubled` 迭代器的下一个元素
next(doubled)
# 此时 `map` 函数取出 `s` 中的第一个元素（3）传递给 `double_and_print` 函数，
# 会执行函数内代码，先打印 `*** 3 => 6 ***`，然后返回 6 作为 `next` 函数获取到的结果。

next(doubled)
# 再次调用 `next` 函数，`map` 函数取出 `s` 中的第二个元素（4）传递给 `double_and_print` 函数，
# 会打印 `*** 4 => 8 ***` 并返回 8。

list(doubled)
# 使用 `list` 函数将 `doubled` 迭代器转换为列表，触发对剩余元素（5 和 6）的处理。
# `map` 函数依次取出这些元素传递给 `double_and_print` 函数，
# 分别打印 `*** 5 => 10 ***` 和 `*** 6 => 12 ***`，
# 并最终将所有返回的翻倍后的结果收集起来，组成列表 `[10, 12]` 返回。


# `map` 函数的其他常见用法

# 对列表元素进行简单运算
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))
# 解释：定义 `numbers` 列表，使用 `map` 函数结合 `lambda` 表达式将列表元素进行平方运算。
# `lambda x: x ** 2` 是匿名函数，接受 `x` 并返回其平方。
# `map` 函数将此匿名函数应用到 `numbers` 每个元素上，最后转换为列表得到元素平方组成的新列表 `[1, 4, 9, 16, 25]`。


# 对多个列表对应元素进行操作
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))
# 解释：有 `list1` 和 `list2` 两个列表，使用 `map` 函数结合 `lambda` 表达式同时操作对应元素。
# `lambda x, y: x + y` 匿名函数接受 `x`、`y`（分别来自两列表对应位置元素）并返回相加结果。
# `map` 函数依次取对应元素传递给匿名函数相加，得到 `[5, 7, 9]` 即对应元素相加后的结果列表。


# 处理字符串列表
words = ["hello", "world", "python"]
lengths = map(len, words)
print(list(lengths))
# 解释：定义字符串列表 `words`，想获取各字符串长度。
# 通过 `map` 函数将内置 `len` 函数应用到 `words` 每个字符串元素上，
# `map` 函数依次传递字符串给 `len` 函数计算长度，
# 最后将各字符串长度组成的迭代器转换为列表，输出 `[5, 5, 6]`，即各字符串长度组成的列表。

# 总之，`map` 函数在 Python 中是方便进行批量数据处理的工具，
# 适合对可迭代对象元素进行统一、有规律操作，利用惰性求值特点可优化性能和内存使用情况。