# -*- coding:UTF-8 -*-
'''
https://leetcode-cn.com/problems/n-queens-ii/
'''


def totalNQueens(n):
    if not n: return 0

    board = [['.'] * n for _ in range(n)]
    ans = []

    def isValid(board, row, col):
        # 行
        for i in range(n):
            if board[i][col] == "Q": return False
        # 左上
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q": return False
            i -= 1
            j -= 1

        # 右上
        i = row - 1
        j = col + 1
        while i >= 0 and j <= n - 1:
            if board[i][j] == "Q": return False
            i -= 1
            j += 1

        return True

    def trackback(board, row, n):
        if row == n: ans.append(1)

        for col in range(n):
            if not isValid(board, row, col): continue
            board[row][col] = "Q"  # 放置皇后
            trackback(board, row + 1, n)  # 递归
            board[row][col] = "."  # 撤销皇后

    trackback(board, 0, n)
    return len(ans)

print(totalNQueens(4))