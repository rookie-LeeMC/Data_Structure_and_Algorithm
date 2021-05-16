# -*- coding:UTF-8 -*-

'''
方法1：https://blog.csdn.net/qq_41765114/article/details/88415541
一、定义状态
dp[i]表示以a[i]结尾的最长递增子序列的长度

二、初始化定义

三、状态递归
dp[i] = max(dp[j])+1   dp[i]>dp[j]
else:   dp[i]=1

四、返回最大值
'''


# 动态规划
def lengthOfLIS(nums):
    n = len(nums)
    if n == 0 or n == 1: return n

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            # 当前的和之前的逐个比较
            # print i,j
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# 滑动窗口
def lengthOfLIS_v2(nums):
    n = len(nums)
    if n == 0 or n == 1: return n

    ans = 0
    tmp = 1
    idx = 1

    while idx < n:
        if nums[idx] > nums[idx - 1]:
            tmp += 1
            ans = max(tmp, ans)
        else:
            tmp = 1
        idx += 1
    return ans


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print lengthOfLIS_v2(nums)
print lengthOfLIS_v2([7, 7, 7, 7, 7, 7, 7])
