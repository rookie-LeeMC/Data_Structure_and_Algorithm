# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

解题
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2


def maxProfit(prices):
    n = len(prices)
    buy1 = buy2 = -prices[0]
    sell1 = sell2 = 0
    for i in range(1, n):
        buy1 = max(buy1, -prices[i])
        sell1 = max(buy1 + prices[i], sell1)

        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    return sell2
