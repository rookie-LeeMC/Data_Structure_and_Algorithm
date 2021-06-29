# -*- coding:UTF-8 -*-

def lengthOfLIS(nums):
    if len(nums) <= 1: return len(nums)

    # 动态规划:dp[i]以i结尾的最长递增子序列
    dp = [1] * len(nums)  # 每个元素自身都是一个递增子序列

    # 状态转移
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
