# -*- coding:UTF-8 -*-
'''
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。

示例 1：

输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：

输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
'''

# star分析问题
# s；

import collections


def longestOnes(A, K):
    count = collections.Counter(A)
    n = len(A)
    if n == 0: return 0
    if count['1'] == n: return n
    if count['0'] == n: return K

    left, right = 0, 0
    ans = -1
    num_dic = {1: 0, 0: 0}

    while right < n:
        num_dic[A[right]] += 1

        while num_dic[0] > K:
            num_dic[A[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)
        right += 1

    return ans


A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
print(longestOnes(A, K))
A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3
print(longestOnes(A, K))
