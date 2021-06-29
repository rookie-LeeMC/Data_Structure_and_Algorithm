# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/target-sum/solution/mu-biao-he-by-leetcode-solution-o0cp/
'''


def findTargetSumWays(nums, target):
    if not nums: return 0

    diff = sum(nums) - target
    if (diff < 0) or (diff % 2 == 1): return 0

    weight = diff // 2
    n = len(nums)

    # dp[i][j]考虑第i个元素，组成综合为j时的组合数
    dp = [[0 for _ in range(weight + 1)] for _ in range(n + 1)]
    # for i in range(n + 1):
    #     dp[i][0] = 1
    dp[0][0] = 1

    # 转移矩阵
    for i in range(1, n + 1):
        for j in range(weight + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]

    return dp[-1][-1]


# ac
def findTargetSumWays_v2(nums, target):
    if not nums: return 0

    diff = sum(nums) - target
    if (diff < 0) or (diff % 2 == 1): return 0

    weight = diff // 2
    n = len(nums)

    dp = [0] * (weight + 1)
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(weight, nums[i - 1] - 1, -1):
            dp[j] += dp[j - nums[i - 1]]

    return dp[-1]


print(findTargetSumWays([1, 1, 1, 1, 1], 3))
print(findTargetSumWays([1], 1))
print(findTargetSumWays([1, 0], 1))

print(findTargetSumWays_v2([1, 1, 1, 1, 1], 3))
print(findTargetSumWays_v2([1], 1))
print(findTargetSumWays_v2([1, 0], 1))
