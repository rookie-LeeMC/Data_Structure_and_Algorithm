# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/coin-change-2/description/

'''


def change(amount, coins):
    if amount == 0: return 0
    if amount < 0 or not coins: return -1

    # 状态定义
    # dp[i]：金额为i时的组合数目

    # 初始化
    dp = [0] * (amount + 1)
    n = len(dp)
    # for coin in coins:
    #     if coin < n: dp[coin] += 1
    # print(dp)

    # 转移方程
    for coin in coins:
        for i in range(coin, n):
            if i == coin:
                dp[i] += 1
            elif dp[i - coin] != 0:
                dp[i] += dp[i - coin]

    return dp[-1]


amount = 5
coins = [1, 2, 5]
print(change(amount, coins))
# 输出: 4

amount = 3
coins = [2]
print(change(amount, coins))
# 输出: 0

amount = 10
coins = [10]
print(change(amount, coins))
# 输出: 1
