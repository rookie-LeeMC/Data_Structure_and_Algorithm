# -*- coding:UTF-8 -*-
'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
'''

s = 7
nums = [2, 3, 1, 2, 4, 3]


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:


def minSubArrayLen(target, nums):
    s=target
    if sum(nums) < s: return 0

    n = len(nums)

    left, right = 0, 0
    tmp_sum = 0
    ans = len(nums) + 1

    while right < n:
        tmp_sum += nums[right]
        right += 1
        while tmp_sum >= s:
            # 更新长度
            ans = min(ans, right - left)
            tmp_sum -= nums[left]
            left += 1

    return ans


print(minSubArrayLen(s, nums))
