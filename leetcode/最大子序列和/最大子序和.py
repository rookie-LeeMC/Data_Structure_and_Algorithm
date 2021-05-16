# -*- coding:UTF-8 -*-
'''
kadane：求单区间 最大子序列和
'''
def maxSubArray(nums):
    # 特例
    if len(nums) == 0 or len(nums) == 1: return sum(nums)

    # 状态定义
    # dp[i]：以第i个元素结尾的最大连续子数组之和

    # 初始化
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        if dp[i - 1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = nums[i] + dp[i - 1]

    return max(dp)


def maxSubArray(nums):
    # 特例
    if len(nums) == 0 or len(nums) == 1: return sum(nums)

    # 状态定义
    # dp[i]：以第i个元素结尾的最大连续子数组之和

    # 初始化
    ans, cur = -float('inf'), -float('inf')

    for num in nums:
        cur = num + max(0, cur)
        ans = max(cur, ans)

    return ans
