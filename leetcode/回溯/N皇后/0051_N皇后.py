# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/n-queens/solution/dai-ma-sui-xiang-lu-51-n-queenshui-su-fa-2k32/
'''


def solveNQueens(n):
    if not n: return []
    board = [['.'] * n for _ in range(n)]
    res = []

    def isValid(board, row, col):
        # 判断同一列是否冲突
        for i in range(n):
            if board[i][col] == "Q": return False

        # 判断左上角是否冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q": return False
            i -= 1
            j -= 1

        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j <= n - 1:
            if board[i][j] == "Q": return False
            i -= 1
            j += 1

        return True

    def trackback(borad, row, n):
        if row == n:
            temp_res = []
            for temp in borad:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            res.append(temp_res)

        for col in range(n):
            if not isValid(borad, row, col): continue
            board[row][col] = "Q"
            trackback(board, row + 1, n)
            board[row][col] = "."

    trackback(board, 0, n)
    return res
