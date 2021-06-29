# -*- coding:UTF-8 -*-
'''
https://zhuanlan.zhihu.com/p/93857890

// 完全背包问题思路二伪代码(空间优化版)
dp[0,...,W] = 0
for i = 1,...,N
    for j = W,...,w[i] // 必须逆向枚举!!!
        for k = [0, 1,..., min(n[i], j/w[i])]
            dp[j] = max(dp[j], dp[j−k*w[i]]+k*v[i])
'''


def knapsack(W, N, nums, weights, values):
    dp = [0] * (W + 1)

    for i in range(1, N + 1):
        for j in range(W, weights[i - 1] - 1, -1):
            for k in range(1, min(nums[i - 1], j / weights[i - 1])):
                dp[j] = max(
                    dp[j],
                    dp[j - weights[i - 1] * k] + values[i - 1] * k
                )
    return dp[-1]
