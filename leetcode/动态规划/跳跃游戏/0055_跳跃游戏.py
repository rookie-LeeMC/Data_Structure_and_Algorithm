# -*- coding:UTF-8 -*-
'''
解题：动态规划
https://leetcode-cn.com/problems/jump-game/solution/tiao-yue-you-xi-dong-tai-gui-hua-jian-da-ndz1/
'''


def canJump(nums):
    # 状态定义:dp[i]为当前位置可以调到的最远点
    dp = [0] * len(nums)
    # 初始化
    dp[0] = nums[0]
    # 状态转移
    for i in range(1, len(nums)):
        if dp[i - 1] >= i:
            dp[i] = max(
                dp[i - 1]
                , i + nums[i]
            )
        else:
            dp[i] = dp[i - 1]

        if dp[i] >= len(nums) - 1:
            return True

    return dp[-1] >= len(nums) - 1
