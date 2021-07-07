# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/divide-two-integers/
解题
https://leetcode-cn.com/problems/divide-two-integers/solution/29-liang-shu-xiang-chu-by-zut_luojinchao-a1dp/
https://blog.csdn.net/qq_41231926/article/details/82413883
'''


def divide(dividend, divisor):
    if dividend == 0 or abs(dividend) < abs(divisor): return 0
    if dividend == divisor: return 1
    if dividend == -divisor: return -1

    a = 2 ** 31
    flag = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0
    count = 0

    # *1 *2 *4 *8，一直到比被除数大
    while dividend >= divisor:
        count += 1
        divisor = divisor << 1

    while count > 0:
        count -= 1
        divisor = divisor >> 1  # 先减半

        while dividend >= divisor:
            result += 1 << count
            dividend -= divisor  # 4+2+..（8>4+2+1） 越加越少，并且保证差值至少是除数的一倍

    if flag: result = -result
    if -a <= result <= a - 1:
        return result
    else:
        return a - 1
