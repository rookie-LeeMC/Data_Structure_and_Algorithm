# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combination-sum-iii/
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
'''


def combinationSum3(k, n):
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


k = 3
n = 7
print(combinationSum3(k, n))
# 输出: [[1, 2, 4]]
