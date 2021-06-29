# -*- coding:UTF-8 -*-
# 数组有重复元素
# 元素只能使用1次
# 解题：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/

def combinationSum2(candidates, target):
    if not candidates: return []

    ans, track = [], []

    def trackback(candidates, track, residue, start):
        if residue < 0: return
        if residue == 0:
            ans.append(track[:])
            return

        for i in range(start, len(candidates)):
            # 剪枝
            if candidates[i] > residue: break
            if i > start and candidates[i] == candidates[i - 1]: continue

            track.append(candidates[i])
            trackback(candidates, track, residue - candidates[i], i + 1)
            track.pop()

    candidates.sort()
    trackback(candidates, track, target, 0)
    return ans


candidates = [2, 5, 2, 1, 2]
target = 5
print(combinationSum2(candidates, target))
