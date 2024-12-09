def solution(n, k, data):
    from functools import lru_cache

    # 定义递归函数并添加缓存
    @lru_cache(None)
    def helper(day, food):
        # 如果食物不足，不合法路径
        if food < 0:
            return float('inf')
        # 递归出口：完成所有天数，无需再花费
        if day > n:
            return 0
        
        # 初始化最小花费
        min_cost = float('inf')
        
        # 尝试购买 0 到最多可以购买的食物量
        for x in range(min(k - food, n - day + 1) + 1):
            # 当前购买的花费
            cost = data[day - 1] * x
            # 递归计算后续天数的最小花费
            min_cost = min(min_cost, cost + helper(day + 1, food + x - 1))
        
        return min_cost

    # 从第 1 天开始，初始没有携带食物
    return helper(1, 0)

# 测试用例
if __name__ == "__main__":
    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)  # 测试通过
    print(solution(21, 8, [7, 25, 20, 16, 18, 7, 20, 15, 9, 3, 12, 3, 21, 3, 6, 1, 7, 11, 19, 1, 2]))  # 返回最小花费
