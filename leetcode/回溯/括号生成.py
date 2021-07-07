# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/generate-parentheses/submissions/

题目解法
'''


def generateParenthesis(n):
    if n == 0: return []
    if n == 1: return [['()']]

    ans = []
    track = []

    def trackback(left, right):
        # 结束条件
        # if len(track) > 2 * n: return
        # if len(track) == 2 * n:
        #     ans.append(''.join(track[:]))

        if len(track) == 2 * n:
            ans.append(''.join(track[:]))
            return

        if left <= n:
            track.append('(')
            trackback(left + 1, right)
            track.pop()

        if right < left:
            track.append(')')
            trackback(left, right + 1)
            track.pop()

    trackback(1, 1)

    return ans


n = 3
print(generateParenthesis(n))
# 输出：["((()))","(()())","(())()","()(())","()()()"]
