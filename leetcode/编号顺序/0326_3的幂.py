# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/power-of-three/
'''


def isPowerOfThree(n):
    if n == 1: return True
    if n < 3: return False

    while n % 3 == 0:
        n = n // 3
        if n == 1: return True

    return False


print(isPowerOfThree(27))
print(isPowerOfThree(45))
