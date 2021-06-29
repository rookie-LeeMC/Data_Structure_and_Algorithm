# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/


'''


def numDecodings(s):
    if len(s) <= 1: return len(s)

    # 状态定义:f[i]到第i个字符串的解码方式
    # 空字符串可以有1种解码方法，解码出一个空字符串。
    f = [1] + [0] * len(s)

    for i in range(1, len(s) + 1):
        # 仅使用第i个字符解码
        if s[i - 1] != '0':
            f[i] += f[i - 1]
        # 使用之前的进行编码
        if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
            f[i] += f[i - 2]

    return f[-1]
