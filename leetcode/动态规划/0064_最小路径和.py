# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/minimum-path-sum/
'''


def minPathSum(grid):
    if not grid: return None
    if len(grid) == 1: return sum(grid[0])
    if len(grid[0]) == 1: return sum([l[0] for l in grid])

    # 状态定义
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # 初始化
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i - 1]
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]

    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

    return dp[-1][-1]
