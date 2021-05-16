# -*- coding:UTF-8 -*-
'''

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

                if (nums[i] + nums[L] + nums[R] > 0): R -= 1
                if (nums[i] + nums[L] + nums[R] < 0): L += 1

        return res


s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 0, 0, 1]))
