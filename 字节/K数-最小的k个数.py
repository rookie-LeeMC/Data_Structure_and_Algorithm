# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/python3-zui-xiao-dui-215-by-lionking865-3chi/

python是最小堆，容易处理
'''


# import random
#
#
# class Solution:
#     def partition(self, nums, l, r):
#         pivot = nums[r]
#         i = l - 1
#         for j in range(l, r):
#             if nums[j] <= pivot:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1], nums[r] = nums[r], nums[i + 1]
#         return i + 1
#
#     def randomized_partition(self, nums, l, r):
#         i = random.randint(l, r)
#         nums[r], nums[i] = nums[i], nums[r]
#         return self.partition(nums, l, r)
#
#     def randomized_selected(self, arr, l, r, k):
#         pos = self.randomized_partition(arr, l, r)
#         num = pos - l + 1
#         if k < num:
#             self.randomized_selected(arr, l, pos - 1, k)
#         elif k > num:
#             self.randomized_selected(arr, pos + 1, r, k - num)
#
#     def getLeastNumbers(self, arr, k):
#         if k == 0:
#             return list()
#         self.randomized_selected(arr, 0, len(arr) - 1, k)
#         return arr[:k]
#

# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/jian-zhi-offer-40-zui-xiao-de-k-ge-shu-j-9yze/
class Solution:
    def getLeastNumbers(self, arr, k):
        if len(arr) <= k: return arr

        def partition(data, left, right):
            #
            base = data[left]

            while left < right:
                while left < right and data[right] > base: right -= 1
                data[left] = data[right]
                while left < right and data[left] <= base: left += 1
                data[right] = data[left]

            data[left] = base
            return left

        def quick_sort(data, left, right):
            mid = partition(data, left, right)
            if k < mid:
                quick_sort(data, left, mid - 1)
            elif k > mid:
                quick_sort(data, mid + 1, right)

            return data[:k]

        return quick_sort(arr, 0, len(arr) - 1)
