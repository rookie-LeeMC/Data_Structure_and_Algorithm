# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/plus-one/
'''


def plusOne(digits):
    if digits == [0]: return [1]

    plus = 1
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += plus
            plus = 0
            break
        elif digits[i] == 9:
            if plus == 0:
                break
            elif plus == 1:
                digits[i] = 0
                plus = 1

    if plus == 1:
        return [1] + digits
    return digits


digits = [1, 2, 3]
print(plusOne(digits))

digits = [4, 3, 2, 1]
print(plusOne(digits))

digits = [0]
print(plusOne(digits))

digits = [9, 9, 9]
print(plusOne(digits))
