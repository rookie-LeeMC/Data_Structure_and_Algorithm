# -*- coding:UTF-8 -*-
'''
组合个数
https://leetcode-cn.com/problems/coin-change-2/description/

解题:
记忆化搜索->动态规划->滚动数组
https://leetcode-cn.com/problems/coin-change-2/solution/ji-yi-hua-sou-suo-dong-tai-gui-hua-gun-d-bpht/

理解成多重背包
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


# 动态规划+二维数组
def change_v2(amount, coins):
    if amount <= 0: return 1

    # dp[i][j]:考虑第i个硬币，达到综合j时的组合数目
    coins_nums = len(coins)
    dp = [[0] * (amount + 1) for _ in range(coins_nums + 1)]
    dp[0][0] = 1

    for i in range(1, coins_nums + 1):
        for j in range(amount + 1):
            if j < coins[i - 1]:
                # 金额不足，就不能考虑第i个硬币
                dp[i][j] += dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    return dp[-1][-1]


# 动态规划+滚动数组
def change_v3(amount, coins):
    if amount == 0: return 1

    coins_nums = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(coins_nums):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]

    return dp[-1]


amount = 5
coins = [1, 2, 5]
print(change_v2(amount, coins))
# 输出: 4

amount = 3
coins = [2]
print(change_v2(amount, coins))
# 输出: 0

amount = 10
coins = [10]
print(change_v2(amount, coins))
# 输出: 1
