# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/maximal-square/
'''


def maximalSquare(matrix):
    if not matrix: return 0

    # 状态定义

    # 初始化
    row, col = len(matrix), len(matrix[0])
    dp = [[0] * col for _ in range(row)]

    # 状态转移
    ans = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]=='0': dp[i][j]=0
            if matrix[i][j]=='1':
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            ans=max(ans,dp[i][j])

    return ans*ans

# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(maximalSquare(matrix))
matrix = [["1"]]
print(maximalSquare(matrix))