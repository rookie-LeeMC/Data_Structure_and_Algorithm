# -*- coding:UTF-8 -*-
'''
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
'''


def minimumTotal(triangle):
    if not triangle: return 0
    if len(triangle) == 1: return triangle[0][0]

    n = len(triangle)
    f = [[0] * n for _ in range(n)]
    f[0][0] = triangle[0][0]

    for i in range(1, n):
        f[i][0] = f[i - 1][0] + triangle[i][0]
        for j in range(1, i):
            f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        f[i][i] = f[i - 1][i - 1] + triangle[i][i]

    return min(f[n - 1])


def minimumTotal(triangle):
    if not triangle: return 0
    if len(triangle) == 1: return triangle[0][0]

    n = len(triangle)
    f = [[0] * n for _ in range(n)]
    f[0][0] = triangle[0][0]

    for i in range(1, n):
        f[i][0] = f[i - 1][0] + triangle[i][0]
        for j in range(1, i):
            f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        f[i][i] = f[i - 1][i - 1] + triangle[i][i]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
minimumTotal(triangle)
