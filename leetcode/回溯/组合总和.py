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
'''


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        track = []

        def backtrack(candidates, track):
            # 结束条件
            if sum(track) > target:
                return

            if sum(track) == target:
                tmp = sorted(track)
                if tmp not in res:
                    res.append(tmp[:])
                return

                # 在选择列表里回溯
            for i in candidates:
                track.append(i)
                backtrack(candidates, track)
                track.pop()

        backtrack(candidates, track)
        return res


def combinationSum(candidates, target):
    if not candidates: return []

    ans = []
    track = []

    def trackback(candidates, track):
        if sum(track) > target: return

        # 结束条件
        if sum(track) == target:
            tmp = sorted(track)
            if tmp not in ans:
                ans.append(tmp[:])
            return

        for num in candidates:
            track.append(num)
            trackback(candidates, track)
            track.pop()

    trackback(candidates, track)

    return ans


s = Solution()
print(s.combinationSum([8, 7, 4, 3], 11))

print(combinationSum([8, 7, 4, 3], 11))
