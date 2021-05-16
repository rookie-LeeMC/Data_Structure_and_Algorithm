# -*- coding:UTF-8 -*-

'''
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
'''


def reverseWords(s):
    if len(s) == 0 or len(s) == 1: return s

    spt= s.split()
    revers = [i[::-1] for i in spt]
    return ' '.join(revers)

s = "Let's take LeetCode contest"
print(reverseWords(s))
