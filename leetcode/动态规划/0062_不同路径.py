# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/unique-paths/
'''


def uniquePaths(m, n):
    if m == 1 or n == 1: return 1

    # 状态定义：dp[i][j]为第i行第j列的走法
    dp = [[0] * n for _ in range(m)]
    # 初始化
    for i in range(n):
        dp[0][i] = 1
    for i in range(m):
        dp[i][0] = 1

    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


m = 7
n = 3
print(uniquePaths(m, n))
