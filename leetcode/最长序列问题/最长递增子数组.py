# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/solution/zui-chang-lian-xu-di-zeng-xu-lie-by-leet-dmb8/

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
'''


# 动态规划
def findLengthOfLCIS_v2(nums) -> int:
    if len(nums) < 2: return len(nums)

    res = 0
    dp = [1] * len(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i] >= nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        res = max(dp[i], res)

    return res


# 贪心算法
# 比较相邻元素，更新元素所在连续子数组的上下界
def findLengthOfLCIS_v2(nums) -> int:
    if len(nums) < 2: return len(nums)

    res, start = 0, 0
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i - 1] >= nums[i]: start = i
        res = max(res, i - start + 1)

    return res
