# -*- coding:UTF-8 -*-
'''
解题
https://blog.csdn.net/weixin_45642918/article/details/106198985
'''


def maxProduct(nums):
    dp = [[0] * 2 for _ in range(len(nums))]
    dp[0][0]=nums[0]
    dp[0][1]=nums[0]

    for i in range(1,len(nums)):
        if nums[i]>0:
            dp[0][0] = max(nums[i],dp[i-1][0]*nums[i])
            dp[0][1] = max(nums[i],dp[i-1][1]*nums[i])
        else:
            dp[0][0] = max(nums[i],dp[i-1][1]*nums[i])
            dp[0][1] = max(nums[i],dp[i-1][0]*nums[i])

