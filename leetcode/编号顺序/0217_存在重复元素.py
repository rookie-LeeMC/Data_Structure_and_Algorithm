# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/contains-duplicate/
'''


def containsDuplicate(nums):
    if len(nums) < 2: return False

    dic = {}
    for i in nums:
        if i not in dic.keys():
            dic[i] = 1
        else:
            return True
    return False
