# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/permutations-ii/
'''


def permuteUnique(nums):
    if not nums: return []
    if len(nums) == 1: return [[nums[0]]]

    ans = []
    track = []

    def trackback(nums, track):
        # 结束条件
        if len(track) == len(nums):
            tmp = []
            for t in track: tmp.append(nums[t])
            if tmp not in ans: ans.append(tmp)
            return

            # 条件回溯
        for i in range(len(nums)):
            if i in track: continue
            track.append(i)
            trackback(nums, track)
            track.pop()

    trackback(nums, track)

    return ans


nums = [1, 1, 2]
print(permuteUnique(nums))
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
