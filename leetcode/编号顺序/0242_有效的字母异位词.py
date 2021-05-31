# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/valid-anagram/

解题思路：hash表
'''


def isAnagram(s, t):
    n1 = len(s)
    n2 = len(t)

    if n1 != n2: return False

    d1, d2 = {}, {}
    for i in range(n1):
        d1[s[i]] = d1.get(s[i], 0) + 1
        d2[t[i]] = d2.get(t[i], 0) + 1

    return d1 == d2


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
