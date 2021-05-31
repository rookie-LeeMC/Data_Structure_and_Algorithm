# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
'''


def intersect(nums1, nums2):
    import collections
    if not nums1 or not nums2: return []

    ans = []
    dic1 = collections.Counter(nums1)
    dic2 = collections.Counter(nums2)

    for k in dic1.keys():
        if k in dic2.keys():
            ans.extend([k] * min(dic1[k], dic2[k]))

    return ans


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))
