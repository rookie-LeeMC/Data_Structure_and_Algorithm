# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/valid-palindrome/
'''


def isPalindrome(s):
    if not s: return False
    if len(s) == 1: return True

    sl = []
    for i in s.lower():
        # 提取数组和字符
        if '0' <= i <= '9' or 'a' <= i <= 'z':
            sl.append(i)
    s = ''.join(sl)

    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))
