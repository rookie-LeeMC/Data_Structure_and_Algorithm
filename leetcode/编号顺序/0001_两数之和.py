# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/two-sum/
'''


def twoSum(nums, target):
    if len(nums) < 1: return None

    n = {}
    for i in range(len(nums)):
        if target - nums[i] not in n.keys():
            n[nums[i]] = i
        else:
            return [i, n[target - nums[i]]]
