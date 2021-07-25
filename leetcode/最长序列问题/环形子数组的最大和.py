# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/liang-ci-kadanesuan-fa-qiu-jie-by-user7648/
'''


def maxSubarraySumCircular(A):
    if len(A) < 2: return sum(A)

    ans_single, cur = -float('inf'), -float('inf')
    for num in A:
        cur = num + max(cur, 0)
        ans_single = max(cur, ans_single)

    ans_double, cur = float('inf'), float('inf')
    for i in range(1, len(A) - 1):
        cur = A[i] + min(0, cur)
        ans_double = min(ans_double, cur)

    return max(ans_single, sum(A) - ans_double)


print(maxSubarraySumCircular([3, -2, 2, -3]))
print(maxSubarraySumCircular([5, -3, 5]))
