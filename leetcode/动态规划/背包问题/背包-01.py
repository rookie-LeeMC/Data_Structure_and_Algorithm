# -*- coding:UTF-8 -*-
'''
背包装下的最大价值
0-1 背包问题 (0-1 knapsack problem)：每种物品只有一个
完全背包问题 (UKP, unbounded knapsack problem)：每种物品都有无限个可用
多重背包问题 (BKP, bounded knapsack problem)：第 i 种物品有 n[i] 个可用

解题：
DP-背包问题系列python
https://www.pythonheidong.com/blog/article/559891/e7a9721744f22cdc92f2/
'''


# W背包总量
# N件物品
# weights每件物品的重量
# values每件物品的价值
def knapsack(W, N, weights, values):
    # 状态定义
    # dp[i][j]为挑选前i个商品，在背包总量为j情况下的最大价值
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):  # 遍历每一件物品，注意weight[i-1]
        for j in range(1, W + 1):  # 遍历背包总量
            if j < weights[i - 1]:
                # 背包总量不足，放不下第i个
                dp[i][j] = dp[i - 1][j]
            else:
                # 背包充足
                # I. 当第n个物品不选时，dp值与第n-1次的dp值相同
                # II.当第n个物品选择时，dp值为第n-1次中背包剩余容量为【w - wts[n-1]】的dp值
                #    加上第n个物品的价值
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i - 1][j - weights[i - 1]] + values[i + 1]
                )

    return dp[-1][-1]


def knapsack_space_optimize(N, W, wts, val):
    dp = [0] * (W + 1)
    for n in range(N):
        # 限制下界，防数组越界
        # 逆序是防止覆盖n-1次的结果
        for w in range(W, wts[n] - 1, -1):
            dp[w] = max(dp[w], dp[w - wts[n]] + val[n])
    return dp[W]
