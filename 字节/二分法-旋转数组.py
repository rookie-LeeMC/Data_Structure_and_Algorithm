# -*- coding:UTF-8 -*-

# 旋转数组找最小值
def minArray(nums):
    if len(nums) == 0: return None
    if len(nums) == 1: return nums[0]

    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] == nums[right]:
            right -= 1

    return left


# 搜索旋转数组
def search(nums, target):
    if not nums: return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[left]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return left


print(search([4, 5, 6, 7, 0, 1, 2], 0))
