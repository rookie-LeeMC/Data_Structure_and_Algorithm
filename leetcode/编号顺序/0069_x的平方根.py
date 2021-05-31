# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/sqrtx/
'''


def mySqrt(x):
    if x == 0 or x == 1: return x

    l, r = 1, x - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

print(mySqrt(8))