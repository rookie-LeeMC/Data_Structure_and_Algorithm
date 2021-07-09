# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combination-sum-ii/
'''


def combinationSum2(candidates, target):
    if not candidates or not target: return []

    res, track = [], []

    def trackback(candidates, track, start, residu):
        if residu < 0: return
        if residu == 0:
            res.append(track[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > residu: break
            # 重复判定
            if i > start and candidates[i] == candidates[i - 1]: continue

            track.append(candidates[i])
            trackback(candidates, track, i + 1, residu - candidates[i])
            track.pop()

    trackback(sorted(candidates), track, 0, target)
    return res


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
