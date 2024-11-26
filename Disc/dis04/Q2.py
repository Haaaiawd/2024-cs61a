def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    def helper(s, index, result):
        ##要对无法赋值的result进行 *等处理，就在定义时声明一下
        if index >= len(s):
            return result
        else:
            include = helper(s, index + 2, result * s[index])
            exclude = helper(s, index + 1, result)
            return max(include, exclude)
    return helper(s, 0, 1)
####我之前太局限于连续处理后直接return结果的递归了
####不直接return,将将要的return值作为一个输入的变量处理后输出也挺好，甚至逻辑更清晰
####解决想要给result一个初始值无法定义的问题