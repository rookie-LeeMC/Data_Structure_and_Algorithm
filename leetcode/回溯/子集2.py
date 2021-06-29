# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/subsets-ii/submissions/
'''


def subsetsWithDup(nums):
    if not nums: return []

    ans, track = [], []

    def trackback(nums, start):
        if sorted(track) not in ans: ans.append(sorted(track))
        if len(track) == len(nums): return

        for i in range(start, len(nums)):
            track.append(nums[i])
            trackback(nums, i + 1)
            track.pop()

    trackback(nums, 0)

    return ans


print(subsetsWithDup([1, 2, 2]))

a = [6, 3, 2, 4, 1, 2, 3, 4]
print(sorted(a))
print(a)
