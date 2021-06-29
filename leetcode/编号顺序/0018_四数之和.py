# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/4sum/
'''


def fourSum(nums, target):
    if len(nums) < 4: return []

    ans = []
    track = []

    def trackback(nums, track, start):
        if len(track) == 4:
            if sum(track) == target and sorted(track) not in ans:
                ans.append(sorted(track))
            return

        for i in range(start, len(nums)):
            track.append(nums[i])
            trackback(nums, track, i + 1)
            track.pop()

    trackback(nums, track, 0)

    return ans


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
