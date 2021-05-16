# -*- coding:UTF-8 -*-

def getMaxSum(nums):
    if len(nums) < 2: return sum(nums)

    # 定义状态
    # dp[i]以第个i元素结尾的最大子序列和

    # 初始化
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    # 递推逻辑

    # 状态转移
    for i in range(1, n):
        if dp[i - 1] < 0:
            dp[i] = nums[i]
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + nums[i]

    print dp

    return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print getMaxSum(nums)

nums = [1]
print getMaxSum(nums)

nums = [0]
print getMaxSum(nums)

nums = [-1]
print getMaxSum(nums)

nums = [-100000]
print getMaxSum(nums)

