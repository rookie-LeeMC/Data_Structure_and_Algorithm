# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/combination-sum-iii/
'''


def combinationSum3(k, n):
    if k == 0 or n < 1: return []

    ans, track = [], []
    nums = range(1, 10, 1)

    def trackback(nums, track, residue, start):
        if residue < 0: return
        if len(track) > k: return

        if sum(track) == n and len(track) == k:
            ans.append(track[:])
            return

        for i in range(start, len(nums)):
            if nums[i] > residue: break
            track.append(nums[i])
            trackback(nums, track, residue - nums[i], i + 1)
            track.pop()

    trackback(nums, track, n, 0)
    return ans


# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
print(combinationSum3(3, 7))
# k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
print(combinationSum3(3, 9))
