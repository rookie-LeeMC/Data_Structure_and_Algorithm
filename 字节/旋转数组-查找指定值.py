# -*- coding:UTF-8 -*-
'''
二分法
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
'''


def search(nums, target):
    if not nums: return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target: return mid
        if nums[left] == target: return left
        if nums[right] == target: return right

        if nums[left] <= nums[mid]:  # 判断mid是否在左有序区间
            if nums[left] < target < nums[mid]:
                right = mid - 1
            else:
                left += 1
        elif nums[left] > nums[mid]:
            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
