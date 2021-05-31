# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/pascals-triangle/
'''


def generate(numRows):
    if numRows == 0: return []
    if numRows == 1: return [[1]]
    if numRows == 2: return [[1],[1, 1]]

    n = 3
    ans = [[1], [1, 1]]
    while n <= numRows:
        tmp = [1]
        for i in range(len(ans[-1]) - 1):
            tmp.append(ans[-1][i] + ans[-1][i + 1])

        tmp.append(1)
        ans.append(tmp)
        n += 1
    return ans


generate(5)
