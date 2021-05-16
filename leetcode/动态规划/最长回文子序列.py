# -*- coding:UTF-8 -*-
a = [1, 2, 3, 4]


# line[:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分。
# line[::-1]其实就是反转字符串。

def longestPalindromeSubseq(s):
    n = len(s)
    if n == 0 or n == 1: return n

    # 转化成最大公共子序列
    s_rev = s[::-1]
    n1 = len(s_rev)

    dp = [[0] * (n1 + 1) for _ in range(n + 1)]

    for i in range(1,n+1):
        for j in range(1,n1+1):
            if s[i-1] == s_rev[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]

s='bbbab'
print longestPalindromeSubseq(s)