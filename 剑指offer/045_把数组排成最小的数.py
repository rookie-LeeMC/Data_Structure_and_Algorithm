# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
剑指 Offer 45. 把数组排成最小的数，leetcode 179 最大数
'''


def minNumber(nums) -> str:
    def partitions_v2(strs, left, right):
        base = strs[left]

        while left < right:
            while left < right and strs[right] + base >= base + strs[right]: right -= 1
            strs[left] = strs[right]
            while left < right and strs[left] + base <= base + strs[left]: left += 1
            strs[right] = strs[left]
        strs[left] = base
        return left

    def quick_sort(strs, left, right):
        if left < right:
            mid = partitions_v2(strs, left, right)
            quick_sort(strs, left, mid - 1)
            quick_sort(strs, mid + 1, right)

    strs = [str(num) for num in nums]
    quick_sort(strs, 0, len(nums) - 1)

    return "".join(strs)


def partitions(strs, left, right):
    i, j = left, right
    while i < j:
        while i < j and strs[j] + strs[left] >= strs[left] + strs[j]: j -= 1
        while i < j and strs[i] + strs[left] <= strs[left] + strs[i]: i += 1
        strs[i], strs[j] = strs[j], strs[i]
    strs[i], strs[left] = strs[left], strs[i]
    return i
