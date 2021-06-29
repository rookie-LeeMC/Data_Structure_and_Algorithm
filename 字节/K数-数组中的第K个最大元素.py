# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
'''


def findKthLargest_v2(nums, k):
    if len(nums) < k: return None
    k1 = len(nums) - k  # 计算与索引的关系

    def partitions(nums, left, right):
        i, j = left, right

        while i < j:
            while i < j and nums[j] > nums[left]: j -= 1
            while i < j and nums[i] <= nums[left]: i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]

        return i

    def quick_sort(nums, left, right):
        mid = partitions(nums, left, right)
        if k1 < mid:
            quick_sort(nums, left, mid - 1)
        elif k1 > mid:
            quick_sort(nums, mid + 1, right)

        return nums[k1]

    return quick_sort(nums, 0, len(nums) - 1)


def findKthLargest(nums, k):
    if len(nums) < k: return None

    heap = [i for i in nums[:k]]
    import heapq
    heapq.heapify(heap)

    for i in nums[k:]:
        if i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)

    return heap[0]


print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
