# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/binary-search/
'''


def search(nums, target):
    if len(nums) == 0: return -1
    if target > nums[-1]: return -1

    # 返回[first, last)内第一个不小于value的值的位置
    def lower_bound(nums, start, end, target):
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return start

    idx = lower_bound(nums, 0, len(nums), target)
    return idx if nums[idx] == target else -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 13
print(search(nums, target))
