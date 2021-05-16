# -*- coding:UTF-8 -*-
'''
题型总结
https://blog.csdn.net/Dby_freedom/article/details/97916580

题目链接
https://leetcode-cn.com/problems/reverse-words-in-a-string/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
'''
def reverseWords(s):
    if len(s) == 0 or len(s)==1:return s

    return ' '.join(s.split()[::-1])

s = "  Bob    Loves  Alice   "
print(reverseWords(s))
# 输出："Alice Loves Bob"

s = "   Bob       Loves  Alice   "
print(s.split())