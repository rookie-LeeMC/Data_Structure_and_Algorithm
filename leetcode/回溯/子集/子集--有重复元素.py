# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/subsets-ii/submissions/
'''



def subsetsWithDup_v2(nums):
    if not nums: return []

    res, track = [], []
    used = [False] * len(nums)

    def trackback(nums, track, start):
        res.append(track[:])
        if len(track) == len(nums): return

        for i in range(start, len(nums)):
            if not used[i]:
                # 采用数层去重
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue

                used[i] = True
                track.append(nums[i])

                trackback(nums, track, i + 1)

                used[i] = False
                track.pop()

    trackback(sorted(nums), track, 0)
    return res


print(subsetsWithDup_v2([1, 2, 2]))
