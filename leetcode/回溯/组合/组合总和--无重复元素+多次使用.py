# -*- coding:UTF-8 -*-
'''
39. 组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。

示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

解题链接
https://leetcode-cn.com/problems/combination-sum/solution/zu-he-zong-he-by-leetcode-solution/
'''


def combinationSum(candidates, target):
    if not candidates or not target: return []

    res, track = [], []

    def trackback(candidates, track, start, residu):
        if residu < 0: return
        if residu == 0:
            res.append(track[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > residu: break
            track.append(candidates[i])
            trackback(candidates, track, i, residu - candidates[i])
            track.pop()

    trackback(sorted(candidates), track, 0, target)

    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
