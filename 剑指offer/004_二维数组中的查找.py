# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-b-3/
'''


def findNumberIn2DArray(matrix, target):
    if not matrix: return False

    row = len(matrix)
    col = len(matrix[0])

    # 行索引
    i = row - 1
    # 列索引
    j = 0

    while i >= 0 and j <= col - 1:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1

    return False
