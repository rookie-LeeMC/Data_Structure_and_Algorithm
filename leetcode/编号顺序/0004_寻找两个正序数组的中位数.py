# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
'''


def findMedianSortedArrays(nums1, nums2):
    if nums1[-1] == 0 and nums2[-1] == 0: return 0.0

    n1 = len(nums1)
    n2 = len(nums2)

    idx = []
    mod = (n1 + n2) // 2
    if mod == 1:
        idx.append(mod)
    else:
        idx.append(mod - 1)
        idx.append(mod)

    ans = []
    merge = []
    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            merge.append(nums1[i])
            i += 1
        else:
            merge.append(nums2[j])
            j += 1

        if len(merge) - 1 in idx:
            ans.append(merge[-1])


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))
