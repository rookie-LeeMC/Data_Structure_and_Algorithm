# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

解题：
python为最小堆，存最大的k个数，所以直接乘以-1，将求最小问题，转化成求组大问题
或者
'''


def kthSmallest(matrix, k):
    if not matrix: return None
    if len(matrix) == 1: return matrix[0][k - 1]

    n = len(matrix)
    k1 = n * n - k + 1   # 倒数第几个最大的

    # python最小堆，每行行首放入
    import heapq
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(heap) < k1:
                heapq.heappush(heap, matrix[i][j])
            elif len(heap) == k1:
                heapq.heappush(heap, matrix[i][j])
                heapq.heappop(heap)

    return heap[0]


matrix = [[-5]]
k = 1
print(kthSmallest(matrix, k))

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthSmallest(matrix, k))

matrix = [[1, 2], [1, 3]]
k = 2
print(kthSmallest(matrix, k))
