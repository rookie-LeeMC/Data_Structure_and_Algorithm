# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combination-sum-ii/
'''


def combinationSum2(candidates, target):
    if not candidates or sum(candidates) < target: return []

    ans = []
    track = []

    def trackback(candidates, track):
        # 结束条件
        tmp = [candidates[t] for t in track]
        if sum(tmp) > target: return
        if sum(tmp) == target:
            tmp2 = sorted(tmp)
            if tmp2 not in ans: ans.append(tmp2)
            return

        # 选择回溯
        for i in range(len(candidates)):
            if i in track: continue
            track.append(i)
            trackback(candidates, track)
            track.pop()

    trackback(candidates, track)

    return ans


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates, target))
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
