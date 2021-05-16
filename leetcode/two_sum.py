# -*- coding:UTF-8 -*-
'''
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''


# def twoSum(nums, target):
#     print()
#     for i in range(len(nums) - 1):
#         diff = target - nums[i]
#         if diff in nums[i + 1:]:
#             return [i, nums.index(diff, i + 1)]

'''
由于要查找差值的同时输出索引，所以使用字典，先查找再插入
字典可以把查找的时间复杂度由o(n)-->o(1)
'''
def twoSum(nums, target):
    dic = {}
    for idx, val in enumerate(nums):
        if (target - val) in dic:
            return [idx, dic[target - val]]
        dic[val] = idx


# print(twoSum([3, 2, 4], 6))
# print('\n'.join([''.join([('111'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))

print('\n'.join([''.join([('xiao'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (
            y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))

# a = range(50000)
#
# t1 = time.time()
# tmp = a.index(49999)
# t2 = time.time()
# print(t2 - t1)
#
# t1 = time.time()
# dic = {}
# for idx, val in enumerate(a):
#     dic[val] = idx
# idx = dic[49999]
# t2 = time.time()
# print(t2 - t1)
