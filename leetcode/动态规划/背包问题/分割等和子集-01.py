# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/partition-equal-subset-sum/
'''


def canPartition(nums):
    if len(nums) <= 1: return False
    if len(nums) == 2: return nums[0] == nums[1]

    nums_sum = sum(nums)
    if nums_sum % 2 == 1: return False

    N = len(nums)
    weight = nums_sum // 2

    # dp[i][j]考虑前i个元素，是否能组成总量为j
    dp = [[False] * (weight + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, weight + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = (dp[i - 1][j]) or (dp[i - 1][j - nums[i - 1]])

    return dp[-1][-1]


# 动态规划+滚动数组：空间优化
def canPartition_cat(nums):
    if len(nums) <= 1: return False
    if len(nums) == 2: return nums[0] == nums[1]

    nums_sum = sum(nums)
    if nums_sum % 2 == 1: return False

    weight = nums_sum // 2
    dp = [False] * (1 + weight)
    dp[0] = True

    for i in range(len(nums)):
        for j in range(weight, nums[i] - 1, -1):
            dp[j] = dp[j] or dp[j - nums[i]]
    return dp[-1]


nums = [1, 5, 11, 5]
print(canPartition_cat(nums))
nums = [1, 2, 3, 5]
print(canPartition_cat(nums))
