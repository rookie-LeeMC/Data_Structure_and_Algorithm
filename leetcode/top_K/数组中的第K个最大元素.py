# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/python3-zui-xiao-dui-215-by-lionking865-3chi/

python是最小堆，容易处理
'''

import heapq


def findKthLargest(nums, k):
    if not nums or k == 0: return None

    # 最小堆长度为k，正好存储最大的k个元素
    heap = nums[0:k]
    # 建堆
    heapq.heapify(heap)

    # 遍历其余元素
    for i in range(k, len(nums)):
        if nums[i] >= heap[0]:  # 如果当前数组值大于堆顶，说明堆叠一定不在topK中
            heapq.heappop(heap)  # 弹出堆顶
            heapq.heappush(heap, nums[i])  # 压入当前数组值
    return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
# ans = 5
print(findKthLargest(nums, k))
