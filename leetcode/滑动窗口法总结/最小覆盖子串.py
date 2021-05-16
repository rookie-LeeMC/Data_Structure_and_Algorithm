# -*- coding:UTF-8 -*-
'''
解题链接：https://www.jianshu.com/p/8d91160be667
左右窗口 题型汇总：https://blog.csdn.net/Dby_freedom/article/details/89066140

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
'''
S = "ADOBECODEBANC"
T = "ABC"

import collections

# 相当于两个计数器
needs = collections.Counter(T)
window = {}
print(needs)

#  记录window中已经有多少字符符合要求了
match = 0

left = 0
right = 0

while right < len(S):
    c1 = S[right]
    if c1 in needs.keys():
        window[c1] = window.get(c1, 0) + 1  # 加入 window
        if window[c1] == needs[c1]: match += 1
    right += 1

    # window 中的字符串已符合 needs 的要求了
    while match == needs[c1]:
        # 更新结果
        # res = minLen(res, window)

        c2 = S[left]
        if c2 in needs.keys():
            window[c2] -= 1
            
