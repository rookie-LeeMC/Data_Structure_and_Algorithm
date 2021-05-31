# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/merge-sorted-array/
解题：
https://leetcode-cn.com/problems/merge-sorted-array/solution/fu-xue-ming-zhu-dong-hua-ti-jie-cong-hou-teq6/
'''


def merge(nums1, m, nums2, n):
    # if n == 0: return nums1
    # if m == 0: return nums2

    i = m - 1
    j = n - 1
    tail = len(nums1) - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[tail] = nums1[i]
            i -= 1
        else:
            nums1[tail] = nums2[j]
            j -= 1
        tail -= 1

    nums1[:j + 1] = nums2[:j + 1]
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))

# [0]
# 0
# [1]
# 1
# nums1 = [4, 5, 6, 0, 0, 0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(merge(nums1, m, nums2, n))
