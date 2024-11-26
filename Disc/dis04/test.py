def multiply_list(lst):
    if not lst:
        return 1
    else:
        return lst[0] * multiply_list(lst[1:])

# 测试
print(multiply_list([1, 2, 3, 4]))  