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


    for i in range(1,len(prices)):
        min_price=min(min_price,prices[i])
        dp[i] = max(prices[i]-min_price,dp[i-1])

    return dp[-1]

