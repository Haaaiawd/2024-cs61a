def cascade(n):
    """打印n的前缀级联。"""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
cascade(int(input()))

#def cascade(n):
#    """打印n的前缀级联。"""
#    print(n)
#    if n >= 10:
#        cascade(n // 10)
#        print(n)

def count_partitions(n, m):
    """计算使用不超过m的部分划分n的方式数量。"""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n - m, m) + count_partitions(n, m - 1)
    