# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

解题
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
'''


def maxProfit(prices):
    if len(prices) < 2: return 0

    # 动态规划
    # 定义状态：dp[i][0/1]表示第i天，0状态不持有股票的最大收益，1状态持有股票的最大收益
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = -prices[0]

    # 初始化
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[-1][0]


print(maxProfit([7, 1, 5, 3, 6, 4]))
