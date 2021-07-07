# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/34-zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-irqc/
'''


# 暴力破解
# def searchRange(nums, target):
#     if not nums: return [-1, -1]
#
#     ans = []
#     for i in range(len(nums)):
#         if nums[i] == target: ans.append(i)
#
#     if not ans: return [-1, -1]
#
#     return [ans[0], ans[-1]]


def searchRange(nums, target):
    if not nums: return [-1, -1]

    # 左边界
    def left_bound(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] == target:
                right = mid - 1  # 寻找左边界，要缩短右区间边界
        if left > len(nums) - 1 or nums[left] != target: return -1
        return left

    # 右边界
    def right_bound(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target: return -1
        return right

    return [left_bound(nums), right_bound(nums)]


nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange(nums, target))


def searchRange_v2(nums, target):
    def find_right_bound(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1
        if right < 0 or nums[right] != target: return -1
        return right

    return [find_right_bound(nums, target - 1), find_right_bound(nums, target)]


nums = [5, 7, 7, 8, 8, 10]
target = 6
print(searchRange_v2(nums, target))
