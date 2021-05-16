# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/

解题：输出第一行，然后旋转剩下的
https://www.cnblogs.com/gczr/p/8387623.html?share_token=78ef87ba-6676-4e64-a45c-5e6db0bec1c3
'''


def spiralOrder(matrix):
    if not matrix: return []
    if len(matrix) == 1: return matrix[0]
    if len(matrix[0]) == 1: return [matrix[i][0] for i in range(len(matrix))]

    ans = []

    def reverse_matrix(matrix):
        res = []

        row = len(matrix)
        col = len(matrix[0])

        for i in range(col - 1, -1, -1):
            tmp = []
            for j in range(row):
                tmp.append(matrix[j][i])
            res.append(tmp)
        return res

    while matrix:
        ans += matrix.pop(0)

        if len(matrix) == 0: break

        matrix = reverse_matrix(matrix)

    return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
# [1,2,3,4,8,12,11,10,9,5,6,7]

matrix = [[1,2,3,4]]
print(spiralOrder(matrix))

matrix = [[1],[2],[3],[4]]
print(spiralOrder(matrix))