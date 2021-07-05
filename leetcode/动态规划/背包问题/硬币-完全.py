# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/coin-change/

https://leetcode-cn.com/problems/coin-change/description/

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
'''


def coinChange(coins, amount):
    if amount == 0: return 0

    # 状态定义
    # dp[i][j]:考虑第i个硬币，当总额为j时的最少硬币个数
    coins_nums = len(coins)
    dp = [[amount + 1] * (amount + 1) for _ in range(coins_nums + 1)]

    # 初始化
    for i in range(coins_nums + 1):
        dp[i][0] = 0

    # 状态转移
    for i in range(1, coins_nums + 1):  # 考虑每个硬币
        for j in range(1, amount + 1):  # 考虑每个总额
            if j < coins[i - 1]:
                # 总额小于当前硬币面额，那么当前面额就不能考虑
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(
                    dp[i - 1][j],  # 不选当前硬币
                    dp[i][j - coins[i - 1]] + 1  # 选当前的硬币
                )

    return dp[-1][-1] if dp[-1][-1] != amount + 1 else -1


def coinChange_space_optimize(coins, amount):
    if amount == 0: return 0

    dp = [(amount + 1)] * (amount + 1)
    dp[0] = 0

    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] = min(
                dp[j],
                dp[j - coins[i]] + 1
            )

    return dp[-1] if dp[-1] != (amount + 1) else -1


coins = [1, 2, 5]
amount = 11
print(coinChange_space_optimize(coins, amount))


def coinChange_v2(coins, amount):
    if not coins or amount < 0: return -1

    coins_num = len(coins)
    # dp[i][j]为考虑第i。。。。
    dp = [[amount + 1] * (amount + 1) for _ in range(coins_num + 1)]
    for i in range(coins_num + 1):
        dp[i][0] = 0

    for i in range(1, coins_num + 1):
        for j in range(1, amount + 1):
            if j < coins[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

    return dp[-1][-1] if dp[-1][-1] != amount + 1 else -1


def coinChange_space_optimize_v2(coins, amount):
    if not coins or amount < 0: return -1
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(len(coins)):
        for j in range(coins[i], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    return dp[-1] if dp[-1] != amount + 1 else -1


coins = [1, 2, 5]
amount = 11
print(coinChange_v2(coins, amount))
print(coinChange_space_optimize_v2(coins, amount))
