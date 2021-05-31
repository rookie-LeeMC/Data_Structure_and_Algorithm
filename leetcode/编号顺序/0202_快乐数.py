# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/happy-number/
'''


def isHappy(n):
    if n == 0: return False
    if n % 10 == 0: return True

    result = []
    while True:
        a = n // 10
        b = n % 10

        c = a * a + b * b
        if c == 1: return True

        if c not in result:
            result.append(c)
            n=c
        elif c in result:
            return False

print(isHappy(19))
