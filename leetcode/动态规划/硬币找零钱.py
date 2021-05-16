# -*- coding:UTF-8 -*-

'''
https://leetcode-cn.com/problems/coin-change/description/

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
'''


def coinChange(coins, amount):
    if not coins or amount < 0: return -1

    # 状态定义
    # dp[i]:金额为i时，最少硬币个数

    # 初始化
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # 状态转移
    # 每个金额下，dp[i] = min(dp[i],dp[i]-conins+1)
    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != (amount + 1) else -1


def coinChange_v3(coins, amount):
    if not coins or amount < 0: return -1

    # 状态定义

    # 初始化
    dp = [[amount + 1] * (amount + 1) for _ in range(len(coins) + 1)]
    row_num = len(dp)
    col_num = len(dp[0])
    for i in range(row_num):
        dp[i][0] = 0
    # for i in range(col_num):
    #     dp[0][i] = -1

    # print(dp)
    for i in range(row_num):
        for j in range(col_num):
            dp[i][j] = min(dp[i][j - coins[i-1]] + 1,  dp[i-1][j])
    return dp[len(coins)][amount] if dp[len(coins)][amount] != (amount + 1) else -1


coins = [1, 2, 5]
amount = 11
print(coinChange_v3(coins, amount))

coins = [2]
amount =3
print(coinChange_v3(coins, amount))
#
# coins = [2]
# amount = 3
# print(coinChange(coins, amount))
#
# coins = [1]
# amount = 0
# print(coinChange(coins, amount))
# coins = [1]
# amount = 1
# print(coinChange(coins, amount))
#
# coins = [1]
# amount = 2
# print(coinChange(coins, amount))
