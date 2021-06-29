# -*- coding:UTF-8 -*-
'''
最少的硬币数量
硬币找零问题总结
https://blog.csdn.net/Dby_freedom/article/details/102144772

dp:看前 i 个物品，总价值是 j 的情况下的最小硬币数目
'''


def func_2(coins, m):
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for c in coins:  # 枚举硬币价值
        for j in range(m, c - 1, -1):  # 从大到小枚举金额，确保j-c >= 0.
            # print(j)
            f[j] = min(f[j], f[j - c] + 1)
            print(f)
    return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。


def nums_v2(coins, m):
    if not coins: return 0

    dp = [[m + 1] * (m + 1) for _ in range(len(coins) + 1)]
    col = len(dp[0])
    row = len(dp)

    for i in range(row):
        dp[i][0] = 0

    for i in range(1, row):
        for j in range(coins[i], col):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i]] + 1)

    return dp[-1][-1] if dp[-1][-1] != (m + 1) else -1


# def nums_v3(coins, m):


coins = [1, 1, 2, 3]
m = 5
print(func_2(coins, m))
