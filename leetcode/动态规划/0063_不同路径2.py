# -*- coding:UTF-8 -*-
'''
题目
https://leetcode-cn.com/problems/unique-paths-ii/

解题
https://leetcode-cn.com/problems/unique-paths-ii/solution/si-chong-shi-xian-xiang-xi-tu-jie-63-bu-0qyz7/
'''


def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid: return 0
    # 头尾是障碍
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0

    # 状态定义:dp[i][j]为第i行第j列的路径之和
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # 初始化
    dp[0][0] = 1
    for i in range(1, n):
        if obstacleGrid[0][i - 1] != 1:
            dp[0][i] = 1
        else:
            break

    for i in range(1, m):
        if obstacleGrid[i - 1][0] != 1:
            dp[i][0] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i - 1][j] != 1:
                up_num = dp[i - 1][j]
            else:
                up_num = 0

            if obstacleGrid[i][j - 1] != 1:
                left_num = dp[i][j - 1]
            else:
                left_num = 0

            dp[i][j] = up_num + left_num

    return dp[-1][-1]


def uniquePathsWithObstacles_v2(obstacleGrid):
    if not obstacleGrid: return 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0

    # 状态定义：dp[i][j]第i行第j列的路径之和
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # 初始化
    dp[0][0] = 1
    for i in range(1, n):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = 1
        else:
            break
    for i in range(1, m):
        if obstacleGrid[i][0] != 1:
            dp[i][0] = 1
        else:
            break

    # 状态转移
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles_v2(obstacleGrid))
