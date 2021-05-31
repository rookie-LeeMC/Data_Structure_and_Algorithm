# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

解题思路：快慢指针法
快指针遍历，慢指针累加
'''


def removeDuplicates_error(nums):
    if len(nums) < 2: return len(nums)

    ans = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: continue
        ans += 1
    return ans


def removeDuplicates(nums):
    if len(nums) < 2: return len(nums)

    n = len(nums)
    fast, slow = 1, 1
    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    return slow


nums = [1, 1, 2]
print(removeDuplicates(nums))

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
