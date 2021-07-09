# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combinations/

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
'''


def combine(n, k):
    if k == 0 or n == 0: return []

    # n标定 1...n
    ans = []
    comb = []

    def trackback(n, k, start, comb, ans):
        if len(comb) == k:
            ans.append(comb[:])
            return

        for i in range(start, n + 1):
            comb.append(i)
            trackback(n, k, i + 1, comb, ans)
            comb.pop()

    trackback(n, k, 1, comb, ans)

    return ans


def combine_v1(n, k):
    if n == 0 or k == 0: return []

    nums = [i + 1 for i in range(n)]
    comb = []
    ans = []

    def trackback(nums, start):
        # 递归终止条件
        if len(comb) == k:
            ans.append(comb[:])
            return

            # 回溯
        for i in range(start, len(nums)):
            comb.append(nums[i])
            trackback(nums, i + 1)
            comb.pop()

    trackback(nums, 0)

    return ans


n = 4
k = 2
print(combine(n, k))
print(combine_v1(n, k))
