# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/ones-and-zeroes/solution/cpython3-1san-wei-dp-2er-wei-dp-by-hanxi-gwli/

解题
https://leetcode-cn.com/problems/ones-and-zeroes/solution/cpython3-1san-wei-dp-2er-wei-dp-by-hanxi-gwli/
'''


def findMaxForm(strs, m, n):
    if not strs: return 0

    # dp[k][i][j]#考虑第i个元素，当i(m)个0，j(n)个1时，最大的子集长度
    # 创建时，j-->i-->k
    strs_len = len(strs)
    dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(strs_len + 1)]

    for k in range(1, strs_len + 1):
        cnt0 = strs[k - 1].count('0')
        cnt1 = strs[k - 1].count('1')

        for i in range(m + 1):  # 不要从1开始遍历，因为可能存在m=0的入参
            for j in range(n + 1):
                if i < cnt0 or j < cnt1:
                    # 空间不足，就不能考虑第k个元素
                    dp[k][i][j] = dp[k - 1][i][j]
                elif i >= cnt0 and j >= cnt1:
                    dp[k][i][j] = max(
                        dp[k - 1][i][j],
                        dp[k - 1][i - cnt0][j - cnt1] + 1  # 选择第k个，先提出到相应空间，然后+1
                    )

    return dp[-1][-1][-1]


def findMaxForm_v2(strs, m, n):
    if not strs: return 0

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for s in strs:
        cnt0 = s.count('0')
        cnt1 = s.count('1')
        for i in range(m, cnt0 - 1, -1):
            for j in range(n, cnt1 - 1, -1):
                dp[i][j] = max(
                    dp[i][j],
                    dp[i - cnt0][j - cnt1] + 1
                )

    return dp[-1][-1]
