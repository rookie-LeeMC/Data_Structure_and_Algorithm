# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

解题：动态规划
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/
'''


def maxProfit(prices):
    if len(prices) == 0: return 0

    n = len(prices)
    # 状态定义：dp[i]表示第i天可以获得的最大利润
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        dp[i] = max(prices[i] - min_price, dp[i - 1])

    return dp[-1]


def maxProfit_v1(prices):
    if len(prices) < 2: return 0

    n = len(prices)
    # 状态定义：dp[i]表示第i天可以获取的最大利润
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        dp[i] = max(prices[i] - min_price, dp[i - 1])

    return dp[-1]


def maxProfit_v2(prices):
    if len(prices) <= 1: return 0
    if len(prices) == 2: return max(0, prices[1] - prices[0])

    min_price = prices[0]
    dp = [0] * len(prices)  # 第i天的最大收益
    for i in range(1, len(prices)):
        if prices[i] < min_price: min_price = prices[i]
        dp[i] = max(dp[i - 1],  # 当天没有任何操作
                    prices[i] - min_price)  # 当天卖出，就要看与过往最小值的差值

    return dp[-1]
