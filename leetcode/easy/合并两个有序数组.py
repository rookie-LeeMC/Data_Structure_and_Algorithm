# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/merge-sorted-array/
'''


def merge(nums1, m, nums2, n):
    if n == 0: return nums1

    m1 = len(nums1) - 1
    i = m - 1
    j = n - 1

    while i >= 0 and j >= 0:  # 考虑索引覆盖
        if nums1[i] > nums2[j]:
            nums1[m1] = nums1[i]
            # m1 -= 1
            i += 1
        else:
            nums1[m1] = nums1[j]
            j += 1
        m1 -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# 输出：[1,2,2,3,5,6]
print(merge(nums1, m, nums2, n))
