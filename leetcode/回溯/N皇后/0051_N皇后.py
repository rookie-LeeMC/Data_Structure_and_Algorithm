# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/n-queens/solution/dai-ma-sui-xiang-lu-51-n-queenshui-su-fa-2k32/
'''


def solveNQueens(n: int):
    if not n: return []

    res = []
    board = [["."] * n for _ in range(n)]

    def isValid(board, row, col):
        for i in range(n):
            if board[i][col] == "Q": return False

        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q": return False
            i -= 1
            j -= 1

        i = row - 1
        j = col + 1
        while i >= 0 and j <= n - 1:
            if board[i][j] == "Q": return False
            i -= 1
            j += 1

        return True

    def trackback(board, row, n):
        if row == n:
            tmp_res = []
            for tmp in board:
                tmp_res.append("".join(tmp))
            res.append(tmp_res)

        for col in range(n):
            if not isValid(board, row, col): continue
            board[row][col] = "Q"
            trackback(board, row + 1, n)
            board[row][col] = "."

    trackback(board, 0, n)
    return res


print(solveNQueens(4))
