# -*- coding:UTF-8 -*-
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]



Python append() 与深拷贝、浅拷贝
https://www.runoob.com/w3cnote/python-append-deepcopy.html
'''


# class Solution:
# def permute(self, nums):
#     res = []
#
#     def backtrack(nums, track):
#         if len(track) == len(nums):
#             res.append(track[:])
#             return
#
#         for i in nums:
#             if i in track: continue
#
#             track.append(i)
#
#             backtrack(nums, track)
#
#             track.pop()
#
#     backtrack(nums, [])
#     return res

#     def permute(self, nums):
#         res = []
#         track = []
#
#         print("res:" + str(id(res)))
#         print("track:" + str(id(track)))
#
#         self.backtrack(nums, track, res)
#         return res
#
#     def backtrack(self, nums, track, res):
#         if len(track) == len(nums):
#             res.append(track[:])
#             print("res:" + str(id(res)))
#             return
#
#         for i in nums:
#             if i in track: continue
#
#             track.append(i)
#             print("track:" + str(id(track)))
#
#             self.backtrack(nums, track, res)
#
#             track.pop()
#             print("track:" + str(id(track)))
#
#
# s = Solution()
# print(s.permute([1, 2, 3]))

# a=[0,1,2]
# b=[]
# b.append(a)
# print(b)
# print(id(a))
# print(id(b))
#
# print('*'*10)
#
# for i in b:
#     print(id(i))
#
# print('*'*10)
#
# a[0]=100
# print(b)
#
# b.append(a[:])
# for i in b:
#     print(id(i))
#
# print('*'*10)
#
# b=b+[a]
# print(id(b))

# a = [1, 1, 1]
# print(id(a))
# print(id(a[:]))

# b = [[0], [0, 0]]
# a = [0, 1]
#
# for i in b:
#     print(a == i)
#
# print('*'*10)
# print(a in b)
#
# print('*'*10)
# print(id(a))
# print(id(a.sort()))
# print(id(sorted(a)))

def permute(nums):
    if not nums: return []
    if len(nums) == 1: return [[nums[0]]]

    ans = []
    track = []

    def trackback(nums, track):
        # 结束条件
        if len(track) == len(nums):
            ans.append(track[:])
            return

        # 选择回溯
        for i in nums:
            if i in track: continue
            track.append(i)
            trackback(nums, track)
            track.pop()

    trackback(nums, track)

    return ans


def permute_2(nums):
    if not nums: return []

    ans = []
    track = []

    def trackback(nums, track):
        if len(track) == len(nums):
            ans.append(track[:])
            return

        for i in nums:
            if i in track: continue
            track.append(i)
            trackback(nums, track)
            track.pop()

    trackback(nums, track)

    return ans


nums = [1, 2, 3]
print(permute(nums))
print(permute_2(nums))
