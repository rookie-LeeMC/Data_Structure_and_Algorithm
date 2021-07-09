# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combination-sum-iii/
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
'''


def combinationSum(k, n):
    if n < 1 or k <= 0: return []

    ans = []
    track = []
    candidates = range(1, 10, 1)

    def trackback(candidates, track):
        # 结束条件
        if sum(track) > n or len(track) > k: return
        if sum(track) == n and len(track) == k:
            tmp = sorted(track)
            if tmp not in ans: ans.append(tmp)
            # ans.append(track[:])
            return

        # 选择回溯
        for i in candidates:
            if i in track: continue
            track.append(i)
            trackback(candidates, track)
            track.pop()

    trackback(candidates, track)

    return ans


def combinationSum3(k, n):
    if not k or not n: return []

    res, track = [], []

    def trackback(nums, start, track):
        if len(track) > k or sum(track) > n: return
        if len(track) == k and sum(track) == n:
            res.append(track[:])
            return

        for i in range(start, len(nums)):
            track.append(nums[i])
            trackback(nums, i + 1, track)
            track.pop()

    trackback([i + 1 for i in range(9)], 0, track)
    return res


k = 3
n = 9
print(combinationSum3(k, n))
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
