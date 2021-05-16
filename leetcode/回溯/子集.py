# -*- coding:UTF-8 -*-

'''
回溯法解题
https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/


78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
a = [0, 1].sort()


class Solution:
    def subsets(self, nums):
        res = []
        track = []

        def backtrack(select_idx, track):
            # 满足条件，停止回溯
            res.append(track[:])
            if len(track) == len(nums):
                return

            # 在选择列表里回溯
            for i in range(select_idx, len(nums)):
                if nums[i] in track: continue

                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()

        backtrack(0, track)

        return res


s = Solution()
# print(s.subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0]))
print(s.subsets([1, 2, 3]))
