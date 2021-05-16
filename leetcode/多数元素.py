# -*- coding:UTF-8 -*-
'''
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''
from collections import Counter


class Solution:
    def majorityElement(self, nums) -> int:
        data = Counter(nums)
        # print(len(data))

        for each in data:
            if data[each] >= float(len(nums)) / 2:
                return each




s = Solution()
print(s.majorityElement([6,5,5]))