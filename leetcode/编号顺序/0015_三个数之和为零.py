# -*- coding:UTF-8 -*-
'''
解题：排序 + 双指针
https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
'''


#
# class Solution:
#     def threeSum(self, nums):
#         res = []
#
#         # track = []
#
#         def backtrack(select_nums, track):
#             # 满足停止条件
#             if track!= [] and sum(track) == 0 and len(track) == 3 :
#                 tmp = sorted(track)
#                 if tmp not in res:
#                     res.append(tmp[:])
#                 return
#
#             for i in range(len(select_nums)):
#                 track.append(select_nums[i])
#
#                 backtrack(select_nums[i + 1:], track)
#
#                 track.pop()
#
#         backtrack(nums, [])
#         return res

class Solution:
    def threeSum(self, nums):
        if nums == None or len(nums) < 3: return []
        if nums == [0, 0, 0]: return [[0, 0, 0]]

        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] > 0: return res
            if i > 0 and nums[i - 1] == nums[i]: continue

            L = i + 1
            R = n - 1

            while L < R:
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])

                    while L < R and nums[L] == nums[L + 1]: L += 1
                    while L < R and nums[R] == nums[R - 1]: R -= 1

                    L += 1
                    R -= 1

                elif (nums[i] + nums[L] + nums[R] > 0): R -= 1
                elif (nums[i] + nums[L] + nums[R] < 0): L += 1

        return res


s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 0, 0, 1]))


def threeSum(nums):
    if len(nums) < 3: return []
    if len(nums) == 3 and sum(nums)==0: return [nums]

    n = len(nums)
    res = []
    nums.sort()

    for i in range(n):
        if nums[i] > 0: return res  # 第一个数大于0，后面比第一个数大，所以不可能为0
        if i > 0 and nums[i] == nums[i - 1]: continue

        l = i + 1
        r = n - 1

        while l < r:
            if (nums[i] + nums[l] + nums[r] == 0):
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1

                while l < r and nums[r] == nums[r - 1]: r -= 1

                l += 1
                r -= 1

            elif (nums[i] + nums[l] + nums[r] > 0): r -= 1
            elif (nums[i] + nums[l] + nums[r] < 0): l += 1

    return res
