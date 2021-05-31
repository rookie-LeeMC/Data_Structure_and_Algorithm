# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/

思路
将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
'''


# 暴力破解
# def search(nums,target):
#     if not nums: return -1
#
#     for i in range(len(nums)):
#         if nums[i] == target: return i
#
#     return -1

def search_old(nums, target):
    if not nums: return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        # 取中判定
        mid = left + (right - left) // 2
        if nums[left] == target: return left
        if nums[right] == target: return right
        if nums[mid] == target: return mid

        if nums[mid] > nums[right]:  # mid在左有序区间
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target and nums[left] > target:
                left = mid + 1
            elif nums[mid] > target and nums[left] < target:
                right = mid - 1

        elif nums[mid] < nums[right]:  # mid在右有序区间
            if nums[mid] < target and nums[right] < target:
                right = mid - 1
            elif nums[mid] < target and nums[right] > target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        elif nums[mid] == nums[right]:
            right -= 1

    return -1


def search(nums, target):
    if not nums: return -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target: return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(search(nums, target))

nums = [1]
target = 0
print(search(nums, target))

nums = [1, 3]
target = 3
print(search(nums, target))
