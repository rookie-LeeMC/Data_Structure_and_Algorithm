# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/
'''


def countSquares(matrix):
    m, n = len(matrix), len(matrix[0])
    f = [[0] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                f[i][j] = matrix[i][j]
            if matrix[i][j] == 0: f[i][j] = 0
            if matrix[i][j] == 1:
                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
            ans += f[i][j]

    return ans


def countSquares_v2(matrix):
    m, n = len(matrix), len(matrix[0])
    f = [[0] * n for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0: f[i][j] = 0
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    f[i][j]  = matrix[i][j]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

            ans += f[i][j]
    return ans


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
print(countSquares(matrix))
print(countSquares_v2(matrix))
