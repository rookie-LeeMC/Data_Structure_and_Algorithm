# -*- coding:UTF-8 -*-
'''

'''


def missingNumber(nums):
    import collections
    f = collections.Counter(nums)

    n = len(nums)
    for i in range(n + 1):
        if i not in f: return i

    return -1


nums = [3, 0, 1]
print(missingNumber(nums))

nums = [0, 1]
print(missingNumber(nums))

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))

nums = [0]
print(missingNumber(nums))
