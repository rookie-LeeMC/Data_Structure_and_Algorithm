# -*- coding:UTF-8 -*-
'''
解题
https://blog.csdn.net/qq_30057549/article/details/107992093
https://zhuanlan.zhihu.com/p/377231783
https://zhuanlan.zhihu.com/p/99926549

有N件物品和一个最多能背重量为W的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品都有无限个（也就是可以放入背包多次），求解将哪些物品装入背包里物品价值总和最大。
'''


def knapsack(W, N, weights, values):
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if j < weights[i - 1]:
                # 背包容量不足
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],  # 不放入
                    dp[i][j - weights[i - 1]] + values[i - 1]
                )

    return dp[-1][-1]


# 优化
def knapsack_space_optimize(W, N, weights, values):
    dp = [0] * (W + 1)

    for i in range(1, N + 1):
        for j in range(weights[i - 1], W + 1):
            dp[j] = max(
                dp[j],
                dp[j - weights[i - 1]] + values[i - 1]
            )

    return dp[-1]
