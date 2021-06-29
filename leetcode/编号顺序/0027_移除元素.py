# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/remove-element/
'''


def removeElement(nums, val):
    '''
    双指针：right指向遍历的元素，left指向赋值的元素
    '''
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1

    return left


def removeElement_v2(nums, val):
    '''
    双指针优化：left、right头尾指针向中间合并
    '''
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1

    return left


nums = [3, 2, 2, 3]
val = 3
print(removeElement_v2(nums, val))
