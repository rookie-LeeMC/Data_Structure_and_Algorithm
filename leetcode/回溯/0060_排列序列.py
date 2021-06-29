# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/permutation-sequence/
'''


def getPermutation(n, k):
    if n == 0: return []

    nums = [i + 1 for i in range(n)]
    nums_len = len(nums)
    ans = []
    track = []

    def trackback(nums, track):
        # 递归条件
        if len(track) == nums_len:
            ans.append(track[:])
        if len(ans) == k: return

        # 回溯
        for i in nums:
            if i in track: continue
            track.append(i)
            trackback(nums, track)
            track.pop()

    trackback(nums, track)

    return ans


print(getPermutation(3, 3))
