# -*- coding:UTF-8 -*-
# 数组无重复
# 元素无限取用

def combinationSum(candidates, target):
    if not candidates: return []

    ans, track = [], []

    def trackback(candidates, track, residue, start):
        if residue < 0:
            return
        if residue == 0:
            ans.append(track[:])
            return

        for i in range(start, len(candidates)):
            track.append(candidates[i])
            trackback(candidates, track, residue - candidates[i], i)
            track.pop()

    trackback(candidates, track, target, 0)

    return ans


def combinationSum_v2(candidates, target):
    if not candidates: return []

    ans, track = [], []

    def trackback(candidates, track, residue, start):
        if residue < 0:
            return
        if residue == 0:
            ans.append(track[:])
            return

        for i in range(start, len(candidates)):
            # 剪枝
            # https: // leetcode - cn.com / problems / combination - sum / solution / zu - he - zong - he - hui - su - suan - fa - jian - zhi - me - ed02 /
            if candidates[i] > residue: break
            track.append(candidates[i])
            trackback(candidates, track, residue - candidates[i], i)
            track.pop()

    candidates.sort()
    trackback(candidates, track, target, 0)

    return ans


def combinationSum_v2(candidates, target):
    if not candidates: return []

    ans, track = [], []

    def trackback(candi, track, residue, start):
        if residue < 0: return
        if residue == 0:
            ans.append(track[:])
            return

        for i in range(start, len(candidates) - 1):
            if candidates[i] > residue: break
            track.append


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum_v2(candidates, target))
