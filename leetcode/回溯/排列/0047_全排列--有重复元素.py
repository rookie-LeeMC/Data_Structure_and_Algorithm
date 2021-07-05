# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/permutations-ii/

解题汇总
https://leetcode-cn.com/problems/permutations-ii/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-hui-s-ki1h/
'''


# 这是为什么呢，就是上面我刚说的，如果要对树层中前一位去重，就用used[i - 1] == false，如果要对树枝前一位去重用used[i - 1] == true。


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # res用来存放结果
        if not nums: return []
        res = []
        used = [False] * len(nums)

        def backtracking(nums, used, path):
            # 终止条件
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    # 如果同一树层nums[i - 1]使用过则直接跳过
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    backtracking(nums, used, path)
                    path.pop()
                    used[i] = False

        # 记得给nums排序
        backtracking(sorted(nums), used, [])
        return res


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
