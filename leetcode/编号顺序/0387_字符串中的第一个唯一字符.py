# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/first-unique-character-in-a-string/

解题：先用哈希表存储频次，再遍历s，找出频次为1的
'''


def firstUniqChar(s):
    import collections
    freq = collections.Counter(s)

    for i in range(len(s)):
        if freq[s[i]] == 1: return i

    return -1

s = "loveleetcode"
print(firstUniqChar(s))