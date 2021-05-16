# -*- coding:UTF-8 -*-

def numDecodings(s):
    if s == '0': return 0
    if len(s) == 1: return 1

    # 动态规划
    # 定义状态：dp[i]标识已第i个数字结尾的子串 的解码数量

    # 初始化
    dp = [0] * len(s)
    if s[0] == '0':
        dp[0] = 0
    else:
        dp[0] = 1

    if dp[0] == 0:
        dp[1] = 0
    elif s[1] == '0':
        if (s[0] + s[1]) <= '26':
            dp[1] = 1
        else:
            dp[1] = 0
    else:
        if (s[0] + s[1]) <= '26':
            dp[1] = 2
        else:
            dp[1] = 1

    # 转移方程
    for i in range(2, len(s)):
        # s[i]单独参与编码
        if s[i] != '0':
            dp[i] += dp[i - 1]

        # s[i]与s[i-1]参与编码
        if s[i - 1] != '0' and (s[i - 1] + s[i]) <= '26':
            dp[i] += dp[i - 2]

    return dp[-1]


print(numDecodings('12'))
print(numDecodings('226'))
print(numDecodings('10'))
print(numDecodings('27'))
print(numDecodings("2101"))
print(numDecodings('301'))
print(numDecodings('06'))
