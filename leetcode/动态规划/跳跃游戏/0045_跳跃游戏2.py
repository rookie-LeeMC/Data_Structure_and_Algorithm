# -*- coding:UTF-8 -*-
'''
解题：动态规划
https://leetcode-cn.com/problems/jump-game-ii/solution/dp-geng-hao-li-jie-by-mo-sheng-ren-18-99t6/

解题：贪心算法
https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
'''


def jump(nums):
    # 状态定义
    dp = [float('inf')] * len(nums)
    dp[0] = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if i - j <= nums[j]: dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

# def jump_v2(nums):
      