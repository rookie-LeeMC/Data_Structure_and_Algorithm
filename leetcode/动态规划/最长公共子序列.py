# -*- coding:UTF-8 -*-
# https://leetcode-cn.com/problems/longest-common-subsequence/
# https://blog.csdn.net/ggdhs/article/details/90713154

def findLCS(text1, text2):
    M, N = len(text1), len(text2)

    if M == 0 or N == 0: return 0

    # dp:(n1+1)*(n2+1)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[M][N]


def longestCommonSubsequence(text1, text2):
    M, N = len(text1), len(text2)
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[M][N]


text1 = "abcba"
text2 = "abcbcba"
# print findLCS(text1, text2)
# print longestCommonSubsequence(text1, text2)

M = 3
N = 2
# dp = [[0] * (N + 1)] * (M + 1)
# for i in range(3):
#     print id(dp[i])
#
# dp = [[0] * (N + 1) for _ in range(M + 1)]
# for i in range(3):
#     print id(dp[i])

a = [0] * 9
for i in range(9):
    print id(a[i])
