# -*- coding:UTF-8 -*-
def maxSubArray(nums):
    # if not nums: return None
    # if len(nums) == 1: return nums[0]
    #
    # n = len(nums)
    # dp = [0] * n
    # dp[0] = nums[0]
    #
    # for i in range(1, n):
    #     if dp[i - 1] < 0:
    #         dp[i] = nums[i]
    #     else:
    #         dp[i] = dp[i - 1] + nums[i]
    #
    # return max(dp)

    if len(nums) < 2: return sum(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i - 1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]
    return max(dp)


def maxSubArray_v2(nums):
    if len(nums) < 2: return sum(nums)

    cur, ans = -float('inf'), -float('inf')

    for num in nums:
        cur = num + max(0, cur)
        ans = max(cur, ans)

    return ans
