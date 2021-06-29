# -*- coding:UTF-8 -*-
'''
解题：状态自动机
https://leetcode-cn.com/problems/string-to-integer-atoi/
'''
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Auto:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'sign', 'number', 'end']
            , 'sign': ['end', 'end', 'number', 'end']
            , 'number': ['end', 'end', 'number', 'end']
            , 'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        # 依据现有状态和字符，判定接受字符后的状态
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'sign':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, s: str) -> int:
        auto = Auto()
        for c in s:
            auto.get(c)
        return auto.sign * auto.ans


s = Solution()
print(s.myAtoi("   -42niiji"))
